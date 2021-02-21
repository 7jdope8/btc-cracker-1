import web3
from web3.auto import w3

print("Loading...")
with open("eth.txt","r") as m:
    add = m.read().split()
add= set(add)

while True:
  acct = w3.eth.account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
  addr = acct.address
  key = acct.privateKey.hex()
  if addr in add:
     print("found!!!", addr, " ", key)
     s1 = addr
     s2 = key
     f=open(u"win.txt","a")
     f.write(s1)
     f.write(":"+s2)      
     f.close()
     break
  else:
      print("ethpy...", addr, key)
