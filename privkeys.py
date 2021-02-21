#!/usr/bin/python3

import sha3
import binascii
from ecdsa import SigningKey, SECP256k1
from itertools import combinations
import json
import urllib.request

string = 'c85366032e21c1f61a5353f3f4bad5703deba1b3261ba0f4374a9c672f461af9'
splitstring = string.split('5')

letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
privkeys = []
for c in combinations(letters, 4):
    privkeys.append(splitstring[0]+c[0]+splitstring[1]+c[1]+splitstring[2]+c[2]+splitstring[3]+c[3]+splitstring[4])

print(len(privkeys))
	
for privkey in privkeys:
    key = 'T1CV34VTN7W568WKC1ZIWH4PMFVKASM5DH'
    private = binascii.unhexlify(privkey)
    keccak = sha3.keccak_256()
    keccak.update(SigningKey.from_string(private, curve=SECP256k1).get_verifying_key().to_string())
    address = "0x{0}".format(keccak.hexdigest()[24:])
    #//print("Public Address: {0}".format(address))
    url="https://api.etherscan.io/api?module=account&action=balance&address="+address+"&tag=latest&apikey=" + key
    response = urllib.request.urlopen(url)
    data = response.read()
    values = json.loads(data.decode("utf-8"))
    if values["status"] != "1":
        print("Privkey: "+privkey+" Address: "+ address +" Balance: ERROR!!! "+ values["message"])
    else:
        print("Privkey: "+privkey+" Address: "+ address +" Balance: "+ values["result"])
        
    if  int(values["result"]) > 0:
        f= open("foundKeys.txt","a+")
        f.write("Privkey: "+privkey+" Address: "+ address + "\r\n")