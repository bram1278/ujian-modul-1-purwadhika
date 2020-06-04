# Soal 1 - Konversi Waktu (30 Poin)
# Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

# HH : Hours, 2 digits, range: 00 - 99

# MM : Minutes, 2 digits, range: 00 - 59

# SS : Seconds, 2 digits, range: 00 - 59

# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

# def timeConverter(seconds):
#       .....
 

# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05
# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

# Masukkan detik : ujian
# Invalid Input!

# Masukkan detik : 20.5
# Invalid Input!
# Catatan:

# Untuk Student BSD & Bandung Commit & push source code project ke Github Anda, buatlah repo dengan nama Konversi_Waktu. Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan operational_bdg@purwadhika.com

# Untuk Student Jakarta Kirim File Exam dengan nama Konversi_Waktu.py ke email : nurrokim@purwadhika.com dan operational_jkt@purwadhika.com

try:
    waktu = int(input("Masukkan detik :")) # input user
    
    def hitungwaktu(x): # fungsi untuk menghitung input user berapa jam, menit, dan detiknya
        import math # import dari tool math
        
        hitungjam = math.floor(x/3600) # menghitung jam dengan pembagian ke bawah dari waktu/3600
        sisajam = x % 3600 # menghitung sisa hasil pembagian waktu terhadap jam
        hitungmenit = math.floor(sisajam/60) # menghitung menit dengan pembagian ke bawah dari waktu/60
        sisamenit = sisajam % 60 # menghitung sisa hasil pembagian waktu terhadap menit
        hitungdetik = math.floor(sisamenit/1) # menghitung detik dengan pembagian ke bawah dari waktu/60
        return (hitungjam, hitungmenit, hitungdetik) # function mengembalikan tiga output: hitungjam, hitungmenit, dan hitungdetik
    
    if 0 <= waktu <= 359999: # waktu adalah angka integer positif dan bernilai maksimal 359999
        proses = hitungwaktu(waktu) # variabel proses menggunakan function 'hitungwaktu' dengan input 'waktu'
        print(f"Konversi : {proses[0]} : {proses[1]} : {proses[2]}") # memprint hasil konversi
    else: # jika user menginput angka negatif atau lebih dari 359999
        print('Invalid Input')

except: # jika user menginput string atau float
    print('Invalid Input')