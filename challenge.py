def hitung_hb():
    print("== Menghitung HB ==")
    harga_produk_1 = int(input("Masukkan harga produk 1: "))
    harga_produk_2 = int(input("Masukkan harga produk 2: "))

    total_harga = harga_produk_1 + harga_produk_2
    print("Total harga : ", total_harga)
    diskon = int((total_harga * 30) / 100)
    print("Diskon : ", diskon)
    total_harga_setelah_diskon = total_harga - diskon
    print("Harga setelah diskon : ", total_harga_setelah_diskon)

    hdb = total_harga_setelah_diskon + 224
    print("HDB : ", hdb)
    return hdb #mengembalikan nilai hdb

def hitung_hc():
    print("== Menghitung HC ==")
    harga_produk_1 = int(input("Masukkan harga produk 1: "))
    harga_produk_2 = int(input("Masukkan harga produk 2: "))

    total_harga = harga_produk_1 + harga_produk_2
    print("Total harga : ", total_harga)
    diskon = int((total_harga * 30) / 100)
    print("Diskon : ", diskon)
    total_harga_setelah_diskon = total_harga - diskon
    print("Harga setelah diskon : ", total_harga_setelah_diskon)

    hdc = total_harga_setelah_diskon + 224
    print("HDC : ", hdc)
    return hdc #mengembalikan nilai hdc

def main():
    hdb = hitung_hb()
    while hdb < 350:
        print("Nilai kurang dari 350, CEK HC")
        hdc = hitung_hc()
        
        if hdc <= 350:
            print("HDC kurang dari/sama dengan 350, hitung total belanja hdb dan hdc: ")
            tb = hdb + hdc + 224
            print("Total belanja : ", tb)
            break
        if hdc >= 350:
            print("Nilai lebih dari 350, kembali CEK HC")

    while hdb >= 350:
        print("Nilai lebih dari 350, CEK HB")
        hdb = hitung_hb()

main()
