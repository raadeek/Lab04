import random

n = 3
m = 3

a = [0] * n
for i in range(n):
    a[i] = [0] * m

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0, 20)

for row in a:
    print(row)

suma = 0

for i in range(n):
    for j in range(i + 1, m):
        suma = suma + a[i][j]
print(suma)