from pybitcointools import *
import random
import multiprocessing
from multiprocessing import Pool

print("Loading...")
with open("list.txt","r") as m:
    add = m.read().split()
add= set(add)

r = 0
cores=4

def seek(r):
 while True:
    seed = random_electrum_seed()
    mprivkey = electrum_stretch(seed)
#    masterprivkey = bip32_master_key(seed)
    mpubkey = '04'+electrum_mpk(mprivkey)
    addr = pubkey_to_address(mpubkey)
    offset0 = dbl_sha256('0:0:'+mpubkey[2:].decode('hex'))
    offset1 = dbl_sha256('1:0:'+mpubkey[2:].decode('hex'))
    offset2 = dbl_sha256('2:0:'+mpubkey[2:].decode('hex'))
    offset3 = dbl_sha256('3:0:'+mpubkey[2:].decode('hex'))
    offset4 = dbl_sha256('4:0:'+mpubkey[2:].decode('hex'))
    offset5 = dbl_sha256('5:0:'+mpubkey[2:].decode('hex'))
    offset6 = dbl_sha256('6:0:'+mpubkey[2:].decode('hex'))
    offset7 = dbl_sha256('7:0:'+mpubkey[2:].decode('hex'))
    offset8 = dbl_sha256('8:0:'+mpubkey[2:].decode('hex'))
    offset9 = dbl_sha256('9:0:'+mpubkey[2:].decode('hex'))
    offset10 = dbl_sha256('10:0:'+mpubkey[2:].decode('hex'))
    offset11 = dbl_sha256('11:0:'+mpubkey[2:].decode('hex'))
    offset12 = dbl_sha256('12:0:'+mpubkey[2:].decode('hex'))
    offset13 = dbl_sha256('13:0:'+mpubkey[2:].decode('hex'))
    offset14 = dbl_sha256('14:0:'+mpubkey[2:].decode('hex'))
    offset15 = dbl_sha256('15:0:'+mpubkey[2:].decode('hex'))
    offset16 = dbl_sha256('16:0:'+mpubkey[2:].decode('hex'))
    offset17 = dbl_sha256('17:0:'+mpubkey[2:].decode('hex'))
    offset18 = dbl_sha256('18:0:'+mpubkey[2:].decode('hex'))
    offset19 = dbl_sha256('19:0:'+mpubkey[2:].decode('hex'))
    offset20 = dbl_sha256('0:1:'+mpubkey[2:].decode('hex'))
    offset21 = dbl_sha256('1:1:'+mpubkey[2:].decode('hex'))
    offset22 = dbl_sha256('2:1:'+mpubkey[2:].decode('hex'))
    offset23 = dbl_sha256('3:1:'+mpubkey[2:].decode('hex'))
    offset24 = dbl_sha256('4:1:'+mpubkey[2:].decode('hex'))
    offset25 = dbl_sha256('5:1:'+mpubkey[2:].decode('hex'))
    offset26 = dbl_sha256('6:1:'+mpubkey[2:].decode('hex'))
    offset27 = dbl_sha256('7:1:'+mpubkey[2:].decode('hex'))
    offset28 = dbl_sha256('8:1:'+mpubkey[2:].decode('hex'))
    offset29 = dbl_sha256('9:1:'+mpubkey[2:].decode('hex'))
	
    priv0 = add_privkeys(mprivkey,offset0)
    priv1 = add_privkeys(mprivkey,offset1)
    priv2 = add_privkeys(mprivkey,offset2)
    priv3 = add_privkeys(mprivkey,offset3)
    priv4 = add_privkeys(mprivkey,offset4)
    priv5 = add_privkeys(mprivkey,offset5)
    priv6 = add_privkeys(mprivkey,offset6)
    priv7 = add_privkeys(mprivkey,offset7)
    priv8 = add_privkeys(mprivkey,offset8)
    priv9 = add_privkeys(mprivkey,offset9)
    priv10 = add_privkeys(mprivkey,offset10)
    priv11 = add_privkeys(mprivkey,offset11)
    priv12 = add_privkeys(mprivkey,offset12)
    priv13 = add_privkeys(mprivkey,offset13)
    priv14 = add_privkeys(mprivkey,offset14)
    priv15 = add_privkeys(mprivkey,offset15)
    priv16 = add_privkeys(mprivkey,offset16)
    priv17 = add_privkeys(mprivkey,offset17)
    priv18 = add_privkeys(mprivkey,offset18)
    priv19 = add_privkeys(mprivkey,offset19)
    priv20 = add_privkeys(mprivkey,offset20)
    priv21 = add_privkeys(mprivkey,offset21)
    priv22 = add_privkeys(mprivkey,offset22)
    priv23 = add_privkeys(mprivkey,offset23)
    priv24 = add_privkeys(mprivkey,offset24)
    priv25 = add_privkeys(mprivkey,offset25)
    priv26 = add_privkeys(mprivkey,offset26)
    priv27 = add_privkeys(mprivkey,offset27)
    priv28 = add_privkeys(mprivkey,offset28)
    priv29 = add_privkeys(mprivkey,offset29)

    pub0 = add_pubkeys(mpubkey,privkey_to_pubkey(offset0))
    pub1 = add_pubkeys(mpubkey,privkey_to_pubkey(offset1))
    pub2 = add_pubkeys(mpubkey,privkey_to_pubkey(offset2))
    pub3 = add_pubkeys(mpubkey,privkey_to_pubkey(offset3))
    pub4 = add_pubkeys(mpubkey,privkey_to_pubkey(offset4))
    pub5 = add_pubkeys(mpubkey,privkey_to_pubkey(offset5))
    pub6 = add_pubkeys(mpubkey,privkey_to_pubkey(offset6))
    pub7 = add_pubkeys(mpubkey,privkey_to_pubkey(offset7))
    pub8 = add_pubkeys(mpubkey,privkey_to_pubkey(offset8))
    pub9 = add_pubkeys(mpubkey,privkey_to_pubkey(offset9))
    pub10 = add_pubkeys(mpubkey,privkey_to_pubkey(offset10))
    pub11 = add_pubkeys(mpubkey,privkey_to_pubkey(offset11))
    pub12 = add_pubkeys(mpubkey,privkey_to_pubkey(offset12))
    pub13 = add_pubkeys(mpubkey,privkey_to_pubkey(offset13))
    pub14 = add_pubkeys(mpubkey,privkey_to_pubkey(offset14))
    pub15 = add_pubkeys(mpubkey,privkey_to_pubkey(offset15))
    pub16 = add_pubkeys(mpubkey,privkey_to_pubkey(offset16))
    pub17 = add_pubkeys(mpubkey,privkey_to_pubkey(offset17))
    pub18 = add_pubkeys(mpubkey,privkey_to_pubkey(offset18))
    pub19 = add_pubkeys(mpubkey,privkey_to_pubkey(offset19))
    pub20 = add_pubkeys(mpubkey,privkey_to_pubkey(offset20))
    pub21 = add_pubkeys(mpubkey,privkey_to_pubkey(offset21))
    pub22 = add_pubkeys(mpubkey,privkey_to_pubkey(offset22))
    pub23 = add_pubkeys(mpubkey,privkey_to_pubkey(offset23))
    pub24 = add_pubkeys(mpubkey,privkey_to_pubkey(offset24))
    pub25 = add_pubkeys(mpubkey,privkey_to_pubkey(offset25))
    pub26 = add_pubkeys(mpubkey,privkey_to_pubkey(offset26))
    pub27 = add_pubkeys(mpubkey,privkey_to_pubkey(offset27))
    pub28 = add_pubkeys(mpubkey,privkey_to_pubkey(offset28))
    pub29 = add_pubkeys(mpubkey,privkey_to_pubkey(offset29))

    addr0 = pubkey_to_address(pub0)
    addr1 = pubkey_to_address(pub1)
    addr2 = pubkey_to_address(pub2)
    addr3 = pubkey_to_address(pub3)
    addr4 = pubkey_to_address(pub4)
    addr5 = pubkey_to_address(pub5)
    addr6 = pubkey_to_address(pub6)
    addr7 = pubkey_to_address(pub7)
    addr8 = pubkey_to_address(pub8)
    addr9 = pubkey_to_address(pub9)
    addr10 = pubkey_to_address(pub10)
    addr11 = pubkey_to_address(pub11)
    addr12 = pubkey_to_address(pub12)
    addr13 = pubkey_to_address(pub13)
    addr14 = pubkey_to_address(pub14)
    addr15 = pubkey_to_address(pub15)
    addr16 = pubkey_to_address(pub16)
    addr17 = pubkey_to_address(pub17)
    addr18 = pubkey_to_address(pub18)
    addr19 = pubkey_to_address(pub19)
    addr20 = pubkey_to_address(pub20)
    addr21 = pubkey_to_address(pub21)
    addr22 = pubkey_to_address(pub22)
    addr23 = pubkey_to_address(pub23)
    addr24 = pubkey_to_address(pub24)
    addr25 = pubkey_to_address(pub25)
    addr26 = pubkey_to_address(pub26)
    addr27 = pubkey_to_address(pub27)
    addr28 = pubkey_to_address(pub28)
    addr29 = pubkey_to_address(pub29)

    if addr in add:
        print ("found!!!",addr, mprivkey)
        s1 = addr
        s2 = mprivkey
        f=open(u"y2.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr0 in add:
        print ("found!!!",addr0, priv0, seed)
        s1 = addr0
        s2 = priv0
        f=open(u"y4.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr1 in add:
        print ("found!!!",addr1, priv1, seed)
        s1 = addr1
        s2 = priv1
        f=open(u"y5.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr2 in add:
        print ("found!!!",addr2, priv2, seed)
        s1 = addr2
        s2 = priv2
        f=open(u"y6.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr3 in add:
        print ("found!!!",addr3, priv3, seed)
        s1 = addr3
        s2 = priv3
        f=open(u"y7.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr4 in add:
        print ("found!!!",addr4, priv4, seed)
        s1 = addr4
        s2 = priv4
        f=open(u"y8.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr5 in add:
        print ("found!!!",addr5, priv5, seed)
        s1 = addr5
        s2 = priv5
        f=open(u"y9.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr6 in add:
        print ("found!!!",addr6, priv6, seed)
        s1 = addr6
        s2 = priv6
        f=open(u"y11.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr7 in add:
        print ("found!!!",addr7, priv7, seed)
        s1 = addr7
        s2 = priv7
        f=open(u"y14.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr8 in add:
        print ("found!!!",addr8, priv8, seed)
        s1 = addr8
        s2 = priv8
        f=open(u"y16.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr9 in add:
        print ("found!!!",addr9, priv9, seed)
        s1 = addr9
        s2 = priv9
        f=open(u"y18.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr10 in add:
        print ("found!!!",addr10, priv10, seed)
        s1 = addr10
        s2 = priv10
        f=open(u"y20.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr11 in add:
        print ("found!!!",addr11, priv11, seed)
        s1 = addr11
        s2 = priv11
        f=open(u"y22.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        breakk
    if addr12 in add:
        print ("found!!!",addr12, priv12, seed)
        s1 = addr12
        s2 = priv12
        f=open(u"y24.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr13 in add:
        print ("found!!!",addr13, priv13, seed)
        s1 = addr13
        s2 = priv13
        f=open(u"y26.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr14 in add:
        print ("found!!!",addr14, priv14, seed)
        s1 = addr14
        s2 = priv14
        f=open(u"y28.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr15 in add:
        print ("found!!!",addr15, priv15, seed)
        s1 = addr15
        s2 = priv15
        f=open(u"y30.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr16 in add:
        print ("found!!!",addr16, priv16, seed)
        s1 = addr16
        s2 = priv16
        f=open(u"y32.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr17 in add:
        print ("found!!!",addr17, priv17, seed)
        s1 = addr17
        s2 = priv17
        f=open(u"y34.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr18 in add:
        print ("found!!!",addr18, priv18, seed)
        s1 = addr18
        s2 = priv18
        f=open(u"y36.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr19 in add:
        print ("found!!!",addr19, priv19, seed)
        s1 = addr19
        s2 = priv19
        f=open(u"y38.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr20 in add:
        print ("found!!!",addr20, priv20, seed)
        s1 = addr20
        s2 = priv20
        f=open(u"y40.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr21 in add:
        print ("found!!!",addr21, priv21, seed)
        s1 = addr21
        s2 = priv21
        f=open(u"y42.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr22 in add:
        print ("found!!!",addr22, priv22, seed)
        s1 = addr22
        s2 = priv22
        f=open(u"y44.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr23 in add:
        print ("found!!!",addr23, priv23, seed)
        s1 = addr23
        s2 = priv23
        f=open(u"y46.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr24 in add:
        print ("found!!!",addr24, priv24, seed)
        s1 = addr24
        s2 = priv24
        f=open(u"y48.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr25 in add:
        print ("found!!!",addr25, priv25, seed)
        s1 = addr25
        s2 = priv25
        f=open(u"y50.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr26 in add:
        print ("found!!!",addr26, priv26, seed)
        s1 = addr26
        s2 = priv26
        f=open(u"y51.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr27 in add:
        print ("found!!!",addr27, priv27, seed)
        s1 = addr27
        s2 = priv27
        f=open(u"y52.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr28 in add:
        print ("found!!!",addr28, priv28, seed)
        s1 = addr28
        s2 = priv28
        f=open(u"y53.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    if addr29 in add:
        print ("found!!!",addr29, priv29, seed)
        s1 = addr29
        s2 = priv29
        f=open(u"y54.txt","a")
        f.write(s1)
        f.write(" : "+s2)
        f.close()
        break
    else:
	print "electrum..", seed, addr0, addr1, addr20, addr21


if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()			
