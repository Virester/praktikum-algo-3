#Mohammad Akhmal Firdaus
#0640020000034
#Praktikum 3

a = int(input("Masukkan panjang sisi segitiga pertama : "))
b = int(input("Masukkan panjang sisi segitiga kedua : "))
c = int(input("Masukkan panjang sisi segitiga ketiga : "))

if a == b and a == c and b == c and a+b>c and a+c>b and b+c>a:
    print("Dari sisi tersebut jenis segitiga adalah segitiga sama sisi")
elif a == b or a == c or b == c and a+b>c and a+c>b and b+c>a:
    print("Dari sisi tersebut jenis segitiga adalah segitiga sama kaki")

elif  a+b>c and a+c>b and b+c>a:
    print("Dari sisi tersebut jenis segitiga adalah segitiga sembarang")
else:
    print("Ini bukan segitiga")