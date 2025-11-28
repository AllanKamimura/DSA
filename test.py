num = "00000010100101000001111010011100"
n = int(num, 2)

print(n)

reverse = 0

for i in range(len(num)):
    reverse = (reverse << 1) | (n & 1)
    n >>= 1

final = "00111001011110000010100101000000"
m = int(final, 2)

print(bin(reverse))
print(final)
