# -*- coding: utf-8 -*-
"""

@author: iceland
"""
import hashlib
import binascii

#Address: 17w8w8ZHdqkSYFkhAMfHJaEqCHgHm9egKv
#Target tx : 451c3c76feb9fbba587111d09967850f6442b6a1b9f58679f18532daf76f85da
#r1 = 049238d04bb2a330f5a7d7fef515ac236f1150be6a88c01b814d0232e5207640
#s1 = 2c65aa08424ccd50a095b599f7c07180e60ccfbf6b7bd6e9bd157a8ae623f1f8
#z1 = fdd69255d5c89d1a9dc559ea5275815dbb5a9b4be30fe1a9ba102b1fd16dba0b
#pubkey = 02c6495c510ed187e6f7b4479fb62a12e653108fd8bc1443c1faefa80b5b3875d9

def value_code_hex(intvalue_in_shi):
    return binascii.unhexlify(hex(intvalue_in_shi)[2:].zfill(16))[::-1].hex()

total_utxo = 3000000000  # in satoshi
fee = 200000             # in satoshi
target_z = 'fdd69255d5c89d1a9dc559ea5275815dbb5a9b4be30fe1a9ba102b1fd16dba0b'

st_scr = '01000000b266fd1dcf2035e8cf66649345d61bd1d746b7c0714b01ecebd43b5e86f13684\
010000001976a9144c0dd6c944b6ed2f63aa4727784e1c70e5695c4e88acffffffff'
out_number = str(2).zfill(2)    # 02
pkscr1 = '1976a914fc6123f4bfd3a840b4387ab90e9801e98fb17cf888ac'
pkscr2 = '1976a9147f3910ef17e786f3d81368231d5e55db8407e41388ac'
end_scr = '0000000001000000'

# start search of k : 1 till 30 BTC

for k in range(1,total_utxo-fee):
    v1 = total_utxo - fee - k
    v2 = k
    value1 = value_code_hex(v1)
    value2 = value_code_hex(v2)

    mess = st_scr + out_number + value1 + pkscr1 + value2 + pkscr2 + end_scr
    z_current = hashlib.sha256(hashlib.sha256(bytearray.fromhex(mess)).digest()).hexdigest()
    if z_current == target_z:
        print('\n==== Work DONE with value2 = ' + str(v2) + ' value1 = ' + str(v1))
        break
    if k % 1000000 == 0:
        print('completed : ' + str(k) + ' options')
print('\n=============== Entire Search Completed =================')

