print("Podaj imiona:")
new = input("")
a = new.split(",")
for i in range(len(a)):
    if a[i][-1] == "a":
        print(a[i], end = " ")

