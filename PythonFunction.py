# pythonFunction.py

#! Fungsi Bagi Array String
# Kegunaanya untuk membagi inputan CSV yang masih dalam bentuk string panjang menjadi array dalam array yang sesuai dengan baris dan kolomnya.
#* param array dimasukkan array, dan param pembagi dimasukkan sebagai Char yang membagi setiap kolom datanya.

# Implementasi :
# bagiArrayString(nama;deskripsi;jumlah,';').
#* Array pada param kali ini adalah array of char atau yang sering disebut string.
# [['nama', 'deskripsi', 'jumlah']].
# Data diatas dapat diakses menggunakan namaVariabel[i][j].
# Variabel i menunjukkan baris ke-i dalam csv.
# Variabel j menunjukkan kolom dalam csv, dalam hal ini j = 0 = nama ; j = 1 = deskripsi ; j = 2 = jumlah.

def bagiArrayString(array,pembagi):
    arrayOutput = ''
    temp = ''
    for char in array:
        #print(char)
        if char == pembagi:
            arrayOutput = tambahArrayString(arrayOutput,toArray(temp))
            temp = ''
        else:
            temp += char
    arrayOutput = tambahArrayString(arrayOutput,toArray(temp))
    return arrayOutput

#*--------------------------------------------------------------------------------------#

#! Fungsi Tambah Array String
# Kegunannya untuk menggabungkan 2 buah array menjadi satu array.
#* Param array1 dan array2 dimasukkan array dimana array1 yang akan berada didepan.

# Implementasi:
# tambahArrayString(['udin'],['ganteng'])
# ['udin', 'ganteng']

def tambahArrayString(array1,array2):
    sumArray = ['' for i in range (panjang(array1) + panjang(array2))]
    for i in range (panjang(array1)):
        sumArray[i] = array1[i]
    for i in range(panjang(array1),panjang(array1)+panjang(array2)):
        sumArray[i] = array2[i-panjang(array1)]
    return sumArray

#*---------------------------------------------------------------------------------------#

#! Fungsi To Array
# Kegunannya untuk memasukkan suatu value ke array baru
#* Param value adalah value yang akan dimasukkan ke array baru .

# Implementasi:
# toArray(udin)
# [udin]

def toArray(value):
    array = [value]
    return array
#*---------------------------------------------------------------------------------------#
#! Fungsi Panjang
# Kegunannya untuk menghitung panjang dari suatu variabel
#* Param x adalah diisi dengan variabel yang akan dicari panjangnya.

# Implementasi:
# panjang([1,2,3,3,2])
# 5

def panjang(x):
    sum = 0
    for i in (x):
        sum += 1
    return sum
#*---------------------------------------------------------------------------------------#
#! Fungsi Remove
# Kegunannya untuk menghapus elemen suatu array.
#* Param arr adalah array yang akan di hapus elemennya, param index adalah integer index dari arr yang akan kita hapus.

# Implementasi:
# remove([[1,2,3],[1,3,4],[5,7,8]],1)
# [[1,2,3],[5,7,8]]

def remove(arr,index):
    output = [0 for i in range(panjang(arr)-1)]
    for i in range(index):
        output[i] = arr[i]
    for i in range(index,panjang(arr)-1):
        output[i] = arr[i+1]
    return output
#*---------------------------------------------------------------------------------------#
#! Fungsi random
# Kegunannya untuk Mengeluarkan angka random sesuai range (0..range)
#* Param seeds adalah angka spesial yang menentukan pola linear randomNumber, param range adalah pengali untuk menentukan range dari (0..range)

# Implementasi:
# rando(seeds,5)
# 0.0

# Variable Perubah dan fungsi LNG
# a = 1231; m = 2**31; c = 0;
# x = ((a*seeds)+c) % m

# LNG Algorithm
def rando(seeds,range):
    x = ((1231 * seeds) + 0) % (2**31)
    localseeds = x
    rng = ((x/(2*10**9))) #Pembulatan agar mendekati range (0..1)
    
    #! Case Handler bila rng > 1, agar tidak lewat range yang ditentukan.
    if rng > 1:
        rng = 1
        
    rng = rng * range
    return int(rng),localseeds