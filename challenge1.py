kkm = 75

biologi = 60
matematika = 70
ips = 80
agama = 90

total = (biologi + matematika + ips + agama) / 4
print (int(total))

if total < kkm or total == 74:
    print ("Nilai Anda C")
elif total >= 75 and total <= 79:
    print ("Nilai Anda B")
elif total >= 80 and total <= 100:
    print ("Nilai Anda A")
else :
    print ("ERROR")
