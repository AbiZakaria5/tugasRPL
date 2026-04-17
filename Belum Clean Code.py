n = input("Nama: ")
b = float(input("Berat: "))
t = float(input("Tinggi: "))

h = t/100
x = b/(h*h)

if x < 18.5:
    k = "kurus"
elif x < 25:
    k = "normal"
elif x < 30:
    k = "gemuk"
else:
    k = "obesitas"

print(n, x, k)