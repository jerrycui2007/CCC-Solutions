# https://dmoj.ca/problem/ccc01j2
# Loop through all numbers in the range until the modular inverse is found
x = int(input())
m = int(input())

modular_inverse = None

for i in range(1, m):
    if (x * i) % m == 1:
        modular_inverse = i

if modular_inverse is None:
    print("No such integer exists.")
else:
    print(modular_inverse)
