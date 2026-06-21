inTheCart = []
totalCost = 0
iteration = 0

while True:
    # input user
    toBuy = str(input("barang apa yang mau kamu beli ('q' untuk keluar): "))
    # exit
    if toBuy == 'q':
        print("terimakasih!")
        break    
    # tidak bisa membeli digit (yakali jir)
    while toBuy.isdigit() == True or toBuy == "":
        print("tidak bisa angka atau kosong.")
        toBuy = input("barang apa yang mau kamu beli ('q' untuk keluar): ")

    try:
        productPrice = float(input(f"masukan harga {toBuy}($): "))
    except ValueError:
        print("tidak valid.")
        continue

    totalCost += productPrice
    inTheCart.append(toBuy)
    iteration += 1

print("\n=== PEMBELIAN ===")
for x in range(0, iteration):
    print(inTheCart[x], end=" ")

print(f"\ntotal harga: {totalCost}")