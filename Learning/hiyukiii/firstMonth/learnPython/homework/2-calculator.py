# basic calculator on the terminal

print("""
1. penambahan
2. pengurangan
3. perkalian
4. pembagian""")
try:
    opsi = float(input("\nmasukan angka sesuai operasi yang akan digunakan: "))
except ValueError:
    print("invalid.")
    exit()
if opsi not in [1,2,3,4]:
    print("opsi tidak valid, masukan operasi yang benar.")
    exit()


try:
    firstNumber = float(input("masukan angka pertama: "))
    secondNumber = float(input("masukan angka kedua: "))
except ValueError:
    print("hanya boleh tipe data angka.")
    exit()

if opsi == 1:
    print(f"{firstNumber} + {secondNumber} = {round(firstNumber+secondNumber, 2)}")
elif opsi == 2:
    print(f"{firstNumber} - {secondNumber} = {round(firstNumber-secondNumber, 2)}")
elif opsi == 3:
    print(f"{firstNumber} x {secondNumber} = {round(firstNumber*secondNumber, 2)}")
elif opsi == 4:
    print(f"{firstNumber} / {secondNumber} = {round(firstNumber/secondNumber, 2)}")

