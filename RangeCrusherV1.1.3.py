from time import sleep
from bitcoin import *
import re
import random
from tqdm import tqdm
print ("Range Crusher V1.1.3")
print("By B3daL, Telegram: @b3dal")
print("*Please use [freshaddress.txt] as Your DB*")
print ("================")
def line_count(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
g = line_count("Address.txt")
print ("Total Address in Your File: ", g)
print ("================")
A=str(input("Target Addr or Pattern: "))
b=int(input("Min Range: "))
c=int(input("Max Range: "))
d=int(input("Magnitude: "))
print ("================")
x=2**b
y=2**c
m0=int((y+x)/2)
m1=int((y+x)/2)
with open ("Address.txt","r") as M:
	for line in M:
		list = M.read().split()
list = set(list)
j=0
pbar=tqdm(initial=j)
while True:
	   x=x+d
	   y=y-d
	   m0=m0+d
	   m1=m1-d
	   r0=random.randint(x+1,m1-1)
	   r1=random.randint(m0+1,y-1)
	   myhexx = "%064x" % x
	   privx = myhexx[:64]
	   pubkey1x = encode_pubkey(privtopub(privx), "bin")
	   pubkey12x = encode_pubkey(privtopub(privx), "bin_compressed")
	   addrx = pubtoaddr(pubkey1x)
	   addrx2 = pubtoaddr(pubkey12x)
	   myhexy = "%064x" % y
	   privy = myhexy[:64]
	   pubkey1y = encode_pubkey(privtopub(privy), "bin")
	   pubkey12y = encode_pubkey(privtopub(privy), "bin_compressed")
	   addry = pubtoaddr(pubkey1y)
	   addry2 = pubtoaddr(pubkey12y)
	   myhexm0 = "%064x" % m0
	   privm0 = myhexm0[:64]
	   pubkey1m0 = encode_pubkey(privtopub(privm0), "bin")
	   pubkey12m0 = encode_pubkey(privtopub(privm0), "bin_compressed")
	   addrm0 = pubtoaddr(pubkey1m0)
	   addrm02 = pubtoaddr(pubkey12m0)
	   myhexm1 = "%064x" % m1
	   privm1 = myhexm1[:64]
	   pubkey1m1 = encode_pubkey(privtopub(privm1), "bin")
	   pubkey12m1 = encode_pubkey(privtopub(privm1), "bin_compressed")
	   addrm1 = pubtoaddr(pubkey1m1)
	   addrm12 = pubtoaddr(pubkey12m1)
	   myhexr0 = "%064x" % r0
	   privr0 = myhexr0[:64]
	   pubkey1r0 = encode_pubkey(privtopub(privr0), "bin")
	   pubkey12r0 = encode_pubkey(privtopub(privr0), "bin_compressed")
	   addrr0 = pubtoaddr(pubkey1r0)
	   addrr02 = pubtoaddr(pubkey12r0)
	   myhexr1 = "%064x" % r1
	   privr1 = myhexr1[:64]
	   pubkey1r1 = encode_pubkey(privtopub(privr1), "bin")
	   pubkey12r1 = encode_pubkey(privtopub(privr1), "bin_compressed")
	   addrr1 = pubtoaddr(pubkey1r1)
	   addrr12 = pubtoaddr(pubkey12r1)
	   ADD = str(addrx+addrx2+addry+addry2+addrm0+addrm02+addrm1+addrm12+addrr0+addrr02+addrr1+addrr12)
	   if re.search (A,ADD) or addrx in list or addrx2 in list or addry in list or addry2 in list or addrm0 in list or addrm02 in list or addrm1 in list or addrm12 in list or addrr0 in list or addrr02 in list or addrr1 in list or addrr12 in list:
	       print("")
	       print ("========X=======")
	       print (privx)
	       print (addrx)
	       print (addrx2)
	       print ("========Y=======")
	       print (privy)
	       print(addry)
	       print (addry2)
	       print ("========M0======")
	       print (privm0)
	       print (addrm0)
	       print (addrm02)
	       print ("========M1======")
	       print(privm1)
	       print (addrm1)
	       print (addrm12)
	       print ("========R1======")
	       print (privr1)
	       print (addrr1)
	       print(addrr12)
	       print ("========R0======")
	       print (privr0)
	       print (addrr0)
	       print (addrr02)
	       print ("========End=======")
	       break
	   else:
	   	pbar.update(12)