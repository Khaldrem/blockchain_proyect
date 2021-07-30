from hashlib import sha256

x = 5
y = 0

# hash (x * y)
# Find hash string terminated in 0

while sha256(f'{x * y}'.encode()).hexdigest()[-1] != '0':
    y += 1

print(f'Solution is y={y}')
print(f'hash is: {sha256(f"{x * y}".encode()).hexdigest()}')