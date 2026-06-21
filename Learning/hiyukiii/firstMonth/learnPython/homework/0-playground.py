totalAngka = 0

while True:
    try:
        angkaUser = int(input("masukan angka: "))
        if angkaUser == 4060 or 0:
            print("dadah!")
            break
    except ValueError:
        print("tidak bisa selain angka.")
    totalAngka += angkaUser


print(f"total angka: {totalAngka}")