x = int(input("Podaj liczbe:"))
for i in range(x + 1):
    print(" " * (x - i) + "X" * i)