p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
compressed_key = '04d6597d465408e6e11264c116dd98b539740e802dc756d7eb88741696e20dfe7d3588695d2e7ad23cbf0aa056d42afada63036d66a1d9b97070dd6bc0c87ceb0d'
y_parity = int(compressed_key[:2]) - 2
x = int(compressed_key[2:], 16)
a = (pow(x, 3, p) + 7) % p
y = pow(a, (p+1)//4, p)
if y % 2 != y_parity:
    y = -y % p    
print("KeyX: %064x"%x)
print("KeyY: %064x"%y)