a, b = input("podaj 2 boki prostokata odzdzielone spacja:").split()
a = int(a)
b = int(b)
if a < 0 or b < 0:
    print("zle dane:")
else:
    print("pole prostokata to :", a * b," a obwod to:", a*2+b*2)