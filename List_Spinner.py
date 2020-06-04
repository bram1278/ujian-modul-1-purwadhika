# Soal 2 - List Spinner (30 Poin)
# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

# List Awal

# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# Function

# # Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))
# List Output

# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]

# Catatan:

# Untuk Student BSD & Bandung Commit & push source code project ke Github Anda, buatlah repo dengan nama List_Spinner. Kemudian lampirkan url link repo Github Anda via email ke khumaeni@purwadhika.com dan operational_bdg@purwadhika.com

# Untuk Student Jakarta Kirim File Exam dengan nama List_Spinner.py ke email : nurrokim@purwadhika.com dan operational_jkt@purwadhika.com

a1 = [1, 2, 3] # membuat list awal a1
a2 = [4, 5, 6] # membuat list awal a2
a3 = [7, 8, 9] # membuat list awal a3

print("List Awal") # memprint tampilan list awal
print(f"[ {a1} ,")
print(f"[ {a2} ,")
print(f"[ {a3} ]")

def counterclock(x1,x2,x3): # fungsi untuk menggeser list awal
    for i in range(0, 3):
        x1[i] = 3 + (i * 3)
        x2[i] = 2 + (i * 3)
        x3[i] = 1 + (i * 3)
    return (x1, x2, x3) # fungsi mengembalikan tiga output

proses = counterclock(a1,a2,a3) # variabel 'proses' memanggil fungsi 'counterclock'
print("List Akhir") # memprint tampilan list akhir
print(f"[ {proses[0]} ,")
print(f"[ {proses[1]} ,")
print(f"[ {proses[2]} ]")
