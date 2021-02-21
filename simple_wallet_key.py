# -*- coding: utf-8 -*-
"""

@author: iceland
"""

import re

walletHandle = open("backupwallet.dat", "rb")
wallet = walletHandle.read()

#privKeys_re_c=re.compile(b'\x30\x81\xD3\x02\x01\x01\x04\x20(.{32})', re.DOTALL)
privKeys_re_c=re.compile(b'\x02\x01\x01\x04\x20(.{32})', re.DOTALL)
privKeys=set(privKeys_re_c.findall(wallet))

print("Found %d privKeys" % len(privKeys))