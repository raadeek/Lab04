import random

n = 7
m = 10

a = [0] * n
for i in range(n):
    a[i] = [0] * m

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(0, 20)

for row in a:
    print(row)
