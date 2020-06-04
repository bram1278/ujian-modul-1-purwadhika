# Soal 3 - Mengurai dan Merajut Kata (40 Poin)
# Buatlah sebuah file python yang berisi 2 buah return function, dengan 1 argumen yang dapat digunakan untuk mengurai & merajut sebuah string

# fungsi urai(...) akan mengurai string. contoh output yang diharapkan adalah sebagai berikut:

# # Function Initialization :
# def urai(...):
#     ......
 
# def rajut(...):
#     ......
    
    
# # Use the function

# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))

# # Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
# Sedangkan fungsi rajut(...) akan merajut kembali string yang terurai menjadi bentuk kata asalnya. contoh output yang diharapkan adalah sebagai berikut:

# # Use the function

# print(rajut('CCoCodCode'))
# print(rajut('PPyPytPythPythoPython'))
# print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

# # Output:

# Code
# Python
# Purwadhika

# Catatan:

# Untuk Student BSD & Bandung Commit & push source code project ke Github Anda, buatlah repo dengan nama Urai_Rajut_Kata. Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan operational_bdg@purwadhika.com

# Untuk Student Jakarta Kirim File Exam dengan nama Urai_Rajut_Kata.py ke email : nurrokim@purwadhika.com dan operational_jkt@purwadhika.com

kata = input("Masukkan kata : ") # input user berupa kata yang akan diurai dan dirajut
kataakhir = '' # variabel untuk mencetak string hasil penguraian dengan fungsi 'urai'
katalist = list(kata) # input user dibuat menjadi list   
panjangkata = len(katalist) # hitung berapa jumlah karakter yang diinput user

def urai(x,y,z): # fungsi untuk mengurai input user      
    for i in range(0,(x + 1)):
        for j in range(0,i):
            z += y[j]
    return(z)
    
akhir = urai(panjangkata,katalist,kataakhir) # variabel 'akhir' memanggil fungsi 'urai'
print(f'Hasil penguraian kata {kata} adalah {akhir}')

katalist2 = list(akhir) # variabel untuk mencetak string hasil perajutan dengan fungsi 'rajut'
panjangkata2 = len(katalist2) # hitung berapa jumlah karakter hasil penguraian dengan fungsi 'urai'
selisihkata = panjangkata2 - panjangkata # hitung selisih dari 'panjangkata2 - panjangkata' agar didapatkan jumlah karakter terakhir seperti pada input 'kata'

def rajut(x,y): # fungsi untuk merajut hasil penguraian dari fungsi 'urai'   

    for i in range(0,x):
        y.remove(y[0]) # remove digunakan untuk menghapus y[0] atau katalist2[0] karena index akan bergeser setiap kali remove dilakukan

    panjangkata3 = len(y) 
    kataakhir2 = '' # variabel untuk mencetak string terakhir dari list 'y' atau 'katalist2' yang dikenakan remove

    for i in range(0,panjangkata3):
        kataakhir2 += y[i]
    return(kataakhir2) # fungsi mengembalikan output 'kataakhir2'

akhir2 = rajut(selisihkata,katalist2) # variabel 'akhir2' memanggil fungsi 'rajut'
print(f'Hasil perajutan {akhir} adalah {akhir2}') # print hasil perajutan dengan fungsi 'rajut'