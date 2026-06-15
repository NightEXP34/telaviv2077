import time #hmm.. library baru
import math

while True:
    try:
        userTime = int(input("\nberapa lama timer dijalankan (detik): "))
        while userTime < 0:
            print("tidak bisa negatif.")
            userTime = int(input("\nberapa lama timer dijalankan (detik): "))
        break
    except KeyboardInterrupt:
        print("\nexit")
        break
    except ValueError:
        print("harus merupakan angka")
        continue

for i in range(userTime, -1, -1):
    detik   = i%60 #jika X melebihi 60, maka hanya mengitung sisa. dan di anggap sudah 1 menit.
    menit   = (i/60)%60 #karena 1 menit = 60 detik, dan jika melebihi 60, maka menghitung sisa. di anggap sudah 1 jam.
    jam     = i/3600 #6x6
    print(f"{math.floor(jam):02}:{math.floor(menit):02}:{math.floor(detik):02}")
    time.sleep(1) #delay 1 detik, mirip delay(1000) di arduino.

print("waktu habis!")