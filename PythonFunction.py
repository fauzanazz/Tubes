# #! Fungsi isElementArray
# # Kegunannya untuk Mengecek apakah suatu value merupakan element dari target
# #* Param value untuk input apa yang akan dicari, dan param target adalah dimana input akan di cek

# # Implementasi:
# # isElementArray(alfabet,'a',24)
# # True

def isElementArray(target,value,range):
    for i in range(range):
        if target[i] == value:
            return True
    return False

#! Fungsi random
# Kegunannya untuk Mengeluarkan angka random sesuai range (0..range)
#* Param seeds adalah angka spesial yang menentukan pola linear randomNumber, param range adalah pengali untuk menentukan range dari (0..range)

# Implementasi:
# rando(seeds,5)
# 0.0

# Variable Perubah dan fungsi LNG
# a = 1231; m = 2**31; c = 0;
# x = ((a*seeds)+c) % m

#*---------------------------------------------------------------------------------------#

# LNG Algorithm
def rando(range,seeds):
    x = ((1231 * int(seeds)) + 0) % (2**31)
    seeds = x
    rng = ((x/(2*10**9))) #Pembulatan agar mendekati range (0..1)
    
    #! Case Handler bila rng > 1, agar tidak lewat range yang ditentukan.
    if rng > 1:
        rng = 1
        
    #* Pengali range     
    rng = (rng * range)+1
    
    #! Case Handler bilangan rng melewati range dibatas 1 angka
    if rng > range:
        rng = range,seeds