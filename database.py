from PythonFunction import *

#* Open data  -------------------------------------------------------#
users = open("Assets/user.csv", "r")
candi = open("Assets/candi.csv", "r")
bahan_bangunan = open("Assets/bahan_bangunan.csv", "r")
seeds = open("Assets/seeds.csv", "r")

#* Parse CSV to Array -----------------------------------------------#

# Users
readfile = users.read() # input File

# Algoritma CSV to array
users = (bagiArrayString(readfile,'\n'))

# Container

usersOutput = ['' for i in range (panjang(users)-1)]
for i in range (panjang(users)-1):
    usersOutput[i] = (bagiArrayString(users[i],';'))



# Candi
readfile = candi.read() # input File

# Algoritma CSV to array
candi = (bagiArrayString(readfile,'\n'))

# Container
candiOutput = ['' for i in range (panjang(candi)-1)]
for i in range (panjang(candi)-1):
    candiOutput[i] = (bagiArrayString(candi[i],';'))



# Bahan bangunan
readfile = bahan_bangunan.read() # input File

# Algoritma CSV to array
bahan_bangunan = (bagiArrayString(readfile,'\n'))

# Container
bahanBangunanOutput = ['' for i in range (panjang(bahan_bangunan)-1)]
for i in range (panjang(bahan_bangunan)-1):
    bahanBangunanOutput[i] = (bagiArrayString(bahan_bangunan[i],';'))
    
    
    
# Seeds
readfile = seeds.read() # input File

# Algoritma CSV to array
seeds = (bagiArrayString(readfile,'\n'))

# Container
seedsOutput = ['' for i in range (panjang(seeds)-1)]
for i in range (panjang(seeds)-1):
    seedsOutput[i] = (bagiArrayString(seeds[i],';'))

#*--------------------------------------------------------------------------#
#Penghitung jumlah jin
jumlahJinPemabangun = 0
jumlahJinPengumpul = 0
for i in range(1,panjang(usersOutput[2])):
    if users[i][2] == "jin_pembangun":
        jumlahJinPemabangun += 1
    elif users[i][2] == "jin_pengumpul":
        jumlahJinPemabangun += 1
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah bahan bangunan
pasir = 0
batu = 0
air = 0
for i in range(panjang(bahanBangunanOutput)):
    if bahanBangunanOutput[i][0] == "pasir":
        pasir += int(bahanBangunanOutput[i][2])
    elif bahanBangunanOutput[i][0] == "batu":
        batu += int(bahanBangunanOutput[i][2])
    elif bahanBangunanOutput[i][0] == "air":
        air += int(bahanBangunanOutput[i][2])
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah Candi
jumlahCandi = 0
for i in candiOutput:
    jumlahCandi += 1