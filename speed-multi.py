import codecs
import btc_address
import random

def gen_btc_address(key):
    f = " "; 
    address = btc_address.gen(key)
    print("Public Key:"+62*f+"Address:")
    print(address)
    print("Hex Key:" + key)
  
    
def gen_private_keys_A(start, end):
    for i in range(start, end + 1):
        key = '%064x' % i
        gen_btc_address(key)
          
        
def gen_group_A():
  start =  0x000000000000000000000000000000000000000000000000b800000000000000
  end =    0x000000000000000000000000000000000000000000000000bFFFFFFF00000000
  gen_private_keys_A(start, end)


def gen_weak_keys():
    gen_group_A()


if __name__ == "__main__":
    gen_weak_keys()
    file = open("find_addresses.txt","r")
    for line in searchfile:
        if address in line:
            # Auto saves to Cracked Private Key List.txt
            print("Found Match = "+ key +" - Address = " + address + "\n")
            f = open("Found.txt", 'a')
            f.write("Found = " + key + " - Address = " + address + "\n")
            f.close()
