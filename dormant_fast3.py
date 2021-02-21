# -*- coding: utf-8 -*-
"""
@author: iceland
"""

import bit
import time
import os
import random
import hashlib
from bitcoinlib.encoding import addr_bech32_to_pubkeyhash, change_base


################# Initialization Phase #########################
print("\n-----------------------Starting------------------------------------\
      \nThis program can check 8 Types of Address.\
      \n[Legacy Compressed BTC, Legacy UnCompressed BTC, Segwit BTC, Bech32 BTC, Legacy LTC, Zcash t1, Zcash t3, DASH]")

################ Used Functions #############################
def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()  # 6% faster than bit.crypto

def bech32_to_hash160(address):
    return change_base(addr_bech32_to_pubkeyhash(address), 256, 16)

def read_h160_file():
    with open('my_combined_altcoin_h160_file.txt', 'r') as f:
        h160_list = f.read().rstrip('\n').split('\n')
    print('-------------------------------------------------------------------\n')
    return h160_list
            
def save_h160_file(h160_list):
    with open('my_combined_altcoin_h160_file.txt', 'a') as f:
        for line in h160_list:
            f.write(line + '\n')

def read_allcoin_address_file():
    
    ################# Reading Phase #########################
    with open('sample.txt') as f:
            coin_list = f.read().rstrip('\n').split('\n')
    print('\nLoaded ' + str(len(coin_list)) +' address from file')
    
    ################ Preparation Phase #############################
    legacy_btc_list = [x for x in coin_list if x[0] == '1']  # BTC Legacy Address
    segwit_btc_list = [x for x in coin_list if x[0] == '3']  # BTC Segwit Address
    bech32_btc_list = [x for x in coin_list if x[0] == 'b' and len(x) < 45]      # BTC bech32. ignore multisig address.
    
    Legacy_ltc_list = [x for x in coin_list if x[0] in {'L','M'} and len(x) < 35]  # LTC Legacy Address
    zcash_t1_list = [x for x in coin_list if x[0] == 't' and x[1] == '1']  # Zcash t1 Address
    zcash_t3_list = [x for x in coin_list if x[0] == 't' and x[1] == '3']  # Zcash t3 Address
    dash_list = [x for x in coin_list if x[0] == 'X']  # DASH coin Address
    
    print(str(len(legacy_btc_list))+' Legacy BTC, '
          +str(len(segwit_btc_list))+ ' Segwit BTC, '
          +str(len(bech32_btc_list))+' bech32 BTC, '
          +str(len(Legacy_ltc_list))+' Legacy LTC, \n'
          +str(len(zcash_t1_list))+' Zcash t1, '
          +str(len(zcash_t3_list))+' Zcash t3, '
          +str(len(dash_list))+' DASH coin address found in the file')
    
    print('\nIgnored : '+str(len(coin_list)-len(legacy_btc_list)-len(segwit_btc_list)-len(bech32_btc_list)
        -len(Legacy_ltc_list)-len(zcash_t1_list)-len(zcash_t3_list)-len(dash_list))
        +' Address. (Improper format or multisig address with more than 1 key.)\n')
    
    print('Converting the dormant address of all coins to Hash160 for faster lookup')
    print('-------------------------------------------------------------------\n')
    h160_list = [bit.base58.b58decode_check(address)[1:].hex() for address in legacy_btc_list]
    h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in segwit_btc_list])
    h160_list.extend([bech32_to_hash160(address) for address in bech32_btc_list])
    h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in Legacy_ltc_list])
    h160_list.extend([bit.base58.b58decode_check(address)[2:].hex() for address in zcash_t1_list])
    h160_list.extend([bit.base58.b58decode_check(address)[2:].hex() for address in zcash_t3_list])
    h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in dash_list])
    save_h160_file(h160_list)
    return h160_list

################ H160 File Check ############################
valid = os.path.isfile('my_combined_altcoin_h160_file.txt')
if valid == True:
    print('\nFound the hash160 file: "my_combined_altcoin_h160_file.txt". Will be used directly')
    h160_list = read_h160_file()
else:
    print('\nNot Found my_combined_altcoin_h160_file.txt. Will convert Address file into hash160. \
          \nIt will save to this file in the First Run. Next run will directly read from this file.')
    h160_list = read_allcoin_address_file()
h160_list = set(h160_list)

################ Computation Phase #############################

st = time.time()
k = 1
incr_print = 50000
m = random.randint(1, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140)  # 256 bit range

while True:
    priv = bit.Key.from_int(m)
    cpub = priv.public_key
    upub = priv._pk.public_key.format(compressed=False)
    crmd = HASH160(cpub)
    urmd = HASH160(upub)
    segwit_rmd = HASH160(b'\x00\x14' + crmd)
    
    if crmd.hex() in h160_list or urmd.hex() in h160_list or segwit_rmd.hex() in h160_list:
        print("========= Key Found ========\n PrivateKey: " + priv.to_wif())

        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + priv.to_hex())
        f.write('\nPrivateKey (wif): ' + priv.to_wif())
        f.write('\n==================================')
        f.close()
        break
    else:
        if (k % incr_print) == 0:
            m = random.randint(1, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140)  # 256 bit range
            print ('  {:0.2f} Address/s    :: Total Address Searched: {}'.format(3*incr_print/(time.time() - st), 3*k), end='\r')
            st = time.time()
    k += 1
    m += 1
