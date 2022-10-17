# string
print("Hello World!")
# integer
print(4)
print(5+5)
# perhitungan
print(5*5)
# variable
nama = "zahrul"
angka = 15
print(nama)
print(angka)
# memperbarui variable
name="zahrul"
name='addin'
print(name)
nomor = 5
nomor *= 5
print(nomor)
# penggabungan string
print('Nama Saya ' + 'Zahrul')
# konversi tipe int ke str
AAA = 10
print('angka dari variable AAA adalah ' + str(AAA))
# konversi tipe str ke int
BBB = '15'
hasil = 10 * int(BBB)
print('angka dari variable BBB adalah ' + str(hasil))
# statemen if
nilai = 80
if nilai > 75:
    print('Bagus')
# statement else
nilai = 50
if nilai > 75:
    print('Bagus')
else:
    print('Remedial')
# statement elif
nilai = 40
if nilai > 90:
    print('Nilai kamu A')
elif nilai > 80 :
    print('Nilai kamu B')
elif nilai > 60 :
    print('Nilai kamu C')
else:
    print('Nilai Kamu D')

# penggabungn kondisi -And
jam = 7
if jam > 6 and jam < 8:
    print('selamat pagi')

 #Or
hour = 15
if hour == 12 or hour == 15:
    print('Sore hari') 

#Not
masuk = 9
if not masuk == 11:
    print('terlambat') 