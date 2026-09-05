angka = int(input("Masukkan angka:  "))
if angka % 2 == 0:
  print(f"{angka} adalah bilangan genap")  
else:
    print(f"{angka} adalah bilangan ganjil")


print("-----------------------------------------")


while True:
    print("\n--- CEK BILANGAN GANJIL / GENAP ---")
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")  
    else:
        print(f"{angka} adalah bilangan ganjil")


print("-----------------------------------------")


def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return f"{angka} adalah bilangan Genap."
    else:
        return f"{angka} adalah bilangan Ganjil."
    

def cek_bilangan_prima(angka):
    if angka < 2:
        return f"{angka} bukan bilangan prima."

    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return f"{angka} bukan bilangan prima."
    return f"{angka} adalah bilangan Prima."


def huruf_besar(kalimat):
    return kalimat.upper()


def huruf_kecil(kalimat):
    return kalimat.lower()


print("-----------------------------------------")


import mymodule

print(mymodule.cek_bilangan_prima(7))
print(mymodule.cek_ganjil_genap(14))
print(mymodule.huruf_besar("halo semua"))
print(mymodule.huruf_kecil("HALO SEMUA"))


def main():
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Ganjil Genap")
        print("2. Bilangan Prima")
        print("3. Huruf Besar")
        print("4. Huruf Kecil")
        print("5. Exit")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            angka = int(input("Masukkan angka: "))
            print(mymodule.cek_ganjil_genap(angka))
        elif pilihan == "2":
            angka = int(input("Masukkan angka: "))
            print(mymodule.cek_bilangan_prima(angka))
        elif pilihan == "3":
            kalimat = input("Masukkan kalimat dengan huruf kecil: ")
            print(mymodule.huruf_besar(kalimat))
        elif pilihan == "4":
            kalimat = input("Masukkan kalimat dengan huruf besar: ")
            print(mymodule.huruf_kecil(kalimat))
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
