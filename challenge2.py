print("Menghitung Gaji Dosen")

gaji_pokok = int(input("Masukan Gaji Pokok : "))

sks = int(input("Masukan SKS Permanen : "))
total_sks = sks * 28000
jam = int(input("Masukan Jam Masuk Perbulan : "))
total_jam = jam * 16000
mahasiswa = int(input("Masukan Jumlah Mahasiswa Bimbingan : "))
total_dpa = mahasiswa * 10000

print("")
print("Gaji untuk Total SKS Permanen : ", total_sks)
print("Gaji untuk Total Jam Masuk : ", total_jam)
print("Gaji Jumlah Mahasiswa Bimbingan : ", total_dpa)
gaji_ngajar = total_sks + total_jam + total_dpa
print("")

print("")
print("Gaji Pokok : Rp." ,gaji_pokok)
print("Gaji Mengajar : Rp." ,gaji_ngajar)
print("")

infaq_pokok = int((gaji_pokok * 2)/100)
infaq_ngajar = int((gaji_ngajar * 3)/100)
print("Potongan Gaji Infaq Pokok : Rp." ,infaq_pokok)
print("Potongan Gaji Infaq Mengajar : Rp.",infaq_ngajar)

total_gaji_pokok = int(gaji_pokok - infaq_pokok)
total_gaji_ngajar = int(gaji_ngajar - infaq_ngajar)

print("")
print("Jumlah Gaji Pokok Setelah dipotong Infaq 2%: Rp.",total_gaji_pokok)
print("Jumlah Gaji Mengajar setelah dipotong Infaq 3% : Rp.",total_gaji_ngajar)

gaji_bersih = int(total_gaji_pokok + total_gaji_ngajar)
print("")
print("Gaji Pokok Kotor : ", gaji_pokok)
print("Gaji Mengajar Kotor : ", gaji_ngajar)
print("")
print ("Gaji Bersih : Rp." ,gaji_bersih)

