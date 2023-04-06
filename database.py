import PythonFunction as f

#* Open data  -------------------------------------------------------#
users = open("Assets/user.csv", "r")
candi = open("Assets/candi.csv", "r")
bahan_bangunan = open("Assets/bahan_bangunan.csv", "r")
seeds = open("Assets/seeds.csv", "r")

#* Parse CSV to Array -----------------------------------------------#

# Users
readfile = users.read() # input File

# Algoritma CSV to array
users = (f.bagiArrayString(readfile,'\n'))

# Container

usersOutput = ['' for i in range (f.panjang(users)-1)]
for i in range (f.panjang(users)-1):
    usersOutput[i] = (f.bagiArrayString(users[i],';'))



# Candi
readfile = candi.read() # input File

# Algoritma CSV to array
candi = (f.bagiArrayString(readfile,'\n'))

# Container
candiOutput = ['' for i in range (f.panjang(candi)-1)]
for i in range (f.panjang(candi)-1):
    candiOutput[i] = (f.bagiArrayString(candi[i],';'))



# Bahan bangunan
readfile = bahan_bangunan.read() # input File

# Algoritma CSV to array
bahan_bangunan = (f.bagiArrayString(readfile,'\n'))

# Container
bahanBangunanOutput = ['' for i in range (f.panjang(bahan_bangunan)-1)]
for i in range (f.panjang(bahan_bangunan)-1):
    bahanBangunanOutput[i] = (f.bagiArrayString(bahan_bangunan[i],';'))
    
    
    
# Seeds
readfile = seeds.read() # input File

# Algoritma CSV to array
seeds = (f.bagiArrayString(readfile,'\n'))

# Container
seedsOutput = ['' for i in range (f.panjang(seeds)-1)]
for i in range (f.panjang(seeds)-1):
    seedsOutput[i] = (f.bagiArrayString(seeds[i],';'))

#* Local Storage ----------------------------------------------#

role = None; username = None; 
users = usersOutput; bahanBangunan = bahanBangunanOutput; candi = candiOutput
seeds = seedsOutput;

#*--------------------------------------------------------------------------#
#Penghitung jumlah jin
jumlahJinPemabangun = 0
jumlahJinPengumpul = 0
for i in range(1,f.panjang(usersOutput[2])):
    if users[i][2] == "jin_pembangun":
        jumlahJinPemabangun += 1
    elif users[i][2] == "jin_pengumpul":
        jumlahJinPemabangun += 1
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah bahan bangunan
pasir = 0
batu = 0
air = 0

for i in range(f.panjang(bahanBangunanOutput)):
    if bahanBangunanOutput[i][0] == "pasir":
        pasir += int(bahanBangunanOutput[i][2])
    elif bahanBangunanOutput[i][0] == "batu":
        batu += int(bahanBangunanOutput[i][2])
    elif bahanBangunanOutput[i][0] == "air":
        air += int(bahanBangunanOutput[i][2])

# Penghitung jumlah bahan bangunan Terpakai
pasirTerpakai = 0
batuTerpakai = 0
airTerpakai = 0
jumlahCandi = 0
candiTermahal = (0,0)
candiTermurah = (0,0)


if f.panjang(candi) > 2:
    for i in range(1,f.panjang(candi)):
        pasirTerpakai += int(candi[i][2])
        batuTerpakai += int(candi[i][3])
        airTerpakai += int(candi[i][4])
        jumlahCandi += 1
        
        if i == 1:
            candiTermahal = (int(candi[i][5]),i)
            candiTermurah = (int(candi[i][5]),i)
        
        if candiTermahal[0] < int(candi[i][5]):
            candiTermahal = (int(candi[i][5]),i)
            
        if candiTermurah[0] > int(candi[i][5]):   
            candiTermurah = (int(candi[i][5]),i)
            
    # if candiTermahal == candiTermurah:
    #     candiTermahal = "-"
    #     candiTerrmurah = "-"      
        
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah Candi

#*--------------------------------------------------------------------------#
# Algoritma Jin Terajin

#*--------------------------------------------------------------------------#
# Algrotima Jin Termalas


