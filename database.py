import PythonFunction as f

def load(nama_folder):
    
    #* Container  -------------------------------------------------------#
    usersArray = [[''for i in range (4)] for j in range(1000)]
    candiArray = [[''for i in range (6)] for j in range(100)]
    bahanBangunanArray = [[''for i in range (3)]for j in range(3)]
    seedsArray = [[0 for i in range (2)] for j in range(1)]
    
    #* Open data  -------------------------------------------------------#
    users = open(f"{nama_folder}/user.csv", "r")
    candi = open(f"{nama_folder}/candi.csv", "r")
    bahan_bangunan = open(f"{nama_folder}/bahan_bangunan.csv", "r")
    seeds = open(f"{nama_folder}/seeds.csv", "r")

    #* Parse CSV to Array -----------------------------------------------#

    # Users Load
    temp = users.readline()
    for i in range (1000):
        temp = users.readline()
        if (temp == '.'):
            break
        
        k = 0
        row = ''
        for j in range(len(temp)):
            if temp[j] == ';' or temp[j] == '\n':
                usersArray[i][k] = row
                k += 1 
                row = ''
            else:
                row += temp[j]
    users.close()

    # Candi Load
    temp = candi.readline()
    for i in range (100):
        temp = candi.readline()
        
        if (temp == '.'):
            break
        
        k = 0
        row = ''
        for j in range(len(temp)):
            if temp[j] == ';' or temp[j] == '\n':
                candiArray[i][k] = row
                k += 1 
                row = ''
            else:
                row += temp[j]
    candi.close()

    # bahan bangunan Load
    temp = bahan_bangunan.readline()
    for i in range (3):
        temp = bahan_bangunan.readline()
        
        if (temp == '.'):
            break
        
        k = 0
        row = ''
        for j in range(len(temp)):
            if temp[j] == ';' or temp[j] == '\n':
                bahanBangunanArray[i][k] = row
                k += 1 
                row = ''
            elif temp[j] == '\n':
                bahanBangunanArray[i][k] = row
            else:
                row += temp[j]
    bahan_bangunan.close()

    # seeds Load
    temp = seeds.readline()
    for i in range (1):
        temp = seeds.readline()
        
        if (temp == '.'):
            break
        
        k = 0
        row = ''
        for j in range(len(temp)):
            if temp[j] == ';' or temp[j] == '\n':
                seedsArray[i][k] = row
                k += 1 
                row = ''
            else:
                row += temp[j]
    seeds.close()
    return seedsArray, usersArray, candiArray,bahanBangunanArray
#* Local Storage ----------------------------------------------#

role = None; username = None; 
seeds = []; users = []; candi = []; bahanBangunan = []
jumlahCandi = 0

def hitung():
    pasirTerpakai,batuTerpakai,airTerpakai,jumlahCandi,candiTermahal,candiTermurah = hitungJumlahBahanBangunanTerpakai()
    jumlahPasir,jumlahBatu,jumlahAir = hitungJumlahBahanBangunan()
    jumlahJinPembangun,jumlahJinPengumpul = hitungJumlahJin()
    return jumlahPasir,jumlahBatu,jumlahAir,jumlahJinPembangun,jumlahJinPengumpul,pasirTerpakai,batuTerpakai,airTerpakai,jumlahCandi,candiTermahal,candiTermurah

#*--------------------------------------------------------------------------#
#Penghitung jumlah jin
jumlahJinPembangun = 0
jumlahJinPengumpul = 0

def hitungJumlahJin():
    jumlahJinPembangun = 0
    jumlahJinPengumpul = 0
    for i in range(1000):
        if users[i][2] == "jin_pembangun":
            jumlahJinPembangun += 1
        elif users[i][2] == "jin_pengumpul":
            jumlahJinPembangun += 1
    return jumlahJinPembangun,jumlahJinPengumpul
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah bahan bangunan
jumlahPasir = 0
jumlahBatu = 0
jumlahAir = 0

def hitungJumlahBahanBangunan():
    jumlahPasir = 0
    jumlahBatu = 0
    jumlahAir = 0
    for i in range(3):
        if bahanBangunan[i][0] == "pasir":
            jumlahPasir += int(bahanBangunan[i][2])
        elif bahanBangunan[i][0] == "batu":
            jumlahBatu += int(bahanBangunan[i][2])
        elif bahanBangunan[i][0] == "air":
            jumlahAir += int(bahanBangunan[i][2])
    return jumlahPasir,jumlahBatu,jumlahAir
        
# Penghitung jumlah bahan bangunan Terpakai
pasirTerpakai = 0
batuTerpakai = 0
airTerpakai = 0
jumlahCandi = 0
candiTermahal = (0,0)
candiTermurah = (0,0)

def hitungJumlahBahanBangunanTerpakai():
    pasirTerpakai = 0
    batuTerpakai = 0
    airTerpakai = 0
    jumlahCandi = 0
    candiTermahal = (0,0)
    candiTermurah = (0,0)
    for i in range(100):
        pasirTerpakai += int(candi[i][2])
        batuTerpakai += int(candi[i][3])
        airTerpakai += int(candi[i][4])
        
        if candi[i][5] != '0': 
            jumlahCandi += 1
        
        if i == 1:
            candiTermahal = (int(candi[i][5]),i)
            candiTermurah = (int(candi[i][5]),i)
        
        if candiTermahal[0] < int(candi[i][5]):
            candiTermahal = (int(candi[i][5]),i)
            
        if candiTermurah[0] > int(candi[i][5]):   
            candiTermurah = (int(candi[i][5]),i)
    return pasirTerpakai,batuTerpakai,airTerpakai,jumlahCandi,candiTermahal,candiTermurah
        
        
#*--------------------------------------------------------------------------#
# Penghitung jumlah Candi

#*--------------------------------------------------------------------------#
# Algoritma Jin Terajin

#*--------------------------------------------------------------------------#
# Algrotima Jin Termalas


