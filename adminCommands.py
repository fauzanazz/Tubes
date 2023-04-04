# adminCommands.py

import database as db
from loginLogout import cekUsernameJin
from PythonFunction import *


#* Summon Jin -----------------------------------------------#

def summonJin(users):
    print('''
    Jenis Jin yang dapat dipanggil:
     (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
     (2) Pembangun - Bertugas membangun candi
     ''')
    
    while True:
        jenisJin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        try:
            jenisJin = int(jenisJin)
        except:
        #! Case Handler input bukan Integer
            print("Error Input bukan Integer")
            jenisJin = 0
        jenisJin = int(jenisJin)
        
        #! Case Handler input salah
        while jenisJin > 2 or jenisJin < 1:
            print(f"\nTidak ada jenis jin bernomor \"{jenisJin}\"!")
            jenisJin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            try:
                jenisJin = int(jenisJin)
            except:
            #! Case Handler input bukan Integer
                print("Error Input bukan Integer")
                jenisJin = 0
            
        
        match jenisJin:
            case 1:
                print(f"\nMemilih jin \"Pengumpul\"")
                jenisJin = "jin_pengumpul"
            case 2:
                print(f"Memilih jin \"Pembangun\"")
                jenisJin = "jin_pengumpul"
        
        username = input("Masukkan username jin: ")
        while cekUsernameJin(username,users) != -1:
            print(f"Username \"{username}\" sudah diambil!")
            username = input("Masukkan username jin: ")
        
        password = input("Masukkan password jin: ")
        while not cekValidPassword(password):
            print("Password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")
        
        # Tambahkan user ke array user
        user = tambahArrayString(users,[[username,password,jenisJin]])
        
        print(f'''\n
        Mengumpulkan sesajen...
        Menyerahkan sesajen...
        Membacakan mantra...\n
        Jin {username} berhasil dipanggil!
              ''')
        return user
        
def cekValidPassword(password):
    return panjang(password) >= 5 and panjang(password) <= 25
        
        
        
#* Hapus Jin -----------------------------------------------#   
                  
def hapusJin(users,candi):
    usernameJin = input("Masukkan username jin: ")
    
    #* Buat Algoritma mencari username Jin
    if cekUsernameJin(usernameJin,users) > 0:
        index = cekUsernameJin(usernameJin,users)
        # Verifikasi
        verifikasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {usernameJin} (Y/N)? ")
    
        if verifikasi == "Y":
            #* Algoritma menghapus data jin
            user = remove(users,index)
            candiOutput = hapusCandi(candi, usernameJin)
            # del db.usersOutput[cekUsernameJin(usernameJin)]
            print("Jin Telah berhasil dihapus dari alam gaib.")
            
        elif verifikasi == "N":
            print("Jin tidak jadi di hapus.")
            
        else:
            print("Input tidak Valid.")
    else:
        #! Bila Tidak, ada keluarkan case Handler
        print("Tidak ada jin dengan username tersebut.")
    
    return user,candiOutput

def hapusCandi(candi, usernamejin):
    localCandi = candi
    for i in range(panjang(candi)):
        if candi[i][1] == usernamejin:
            localCandi = remove(localCandi,i)
    return localCandi
    
    
    
#* Ubah Jin -----------------------------------------------#

def ubahJin(users):
    usernameJin = input("Masukkan username jin: ")
    #* Buat Algoritma mencari username Jin
    if cekUsernameJin(usernameJin,users) > 0:
        index = cekUsernameJin(usernameJin,users)
        jenisJin = users[index][2]
        if jenisJin == "jin_pembangun":
            formats1 = "Pembangun"
            formats2 = "Pengumpul"
            ubah = "jin_pengumpul"
        else:
            formats1 = "Pengumpul"
            formats2 = "Pembangun"
            ubah = "jin_pembangun"
            
        verifikasi = input(f"Jin ini bertipe \"{formats1}\". Yakin ingin mengubah ke tipe \"{formats2}\" (Y/N)? ")
        if verifikasi == "Y":
            #* Algoritma mengubah tipe jin
            users[index][2] = ubah
            
        elif verifikasi == "N":
            print("Jin tidak jadi di ubah.")
            
        else:
            print("Input tidak Valid.")
    else:
        #! Bila Tidak ada, keluarkan case Handler
        print("Tidak ada jin dengan username tersebut.")
    return
    
    

#* Batch Kumpul -----------------------------------------------#

def batchKumpul(users, bahanBangunan):
    
    if not cekJinPengumpul(users):
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return
    
    print(f"Mengerahkan {jumlahJinPengumpul} jin untuk mengumpulkan bahan.")
    
    for i in range(jumlahJinPengumpul):
        print
        
    
    
    return

def cekJinPengumpul(users):
    return jumlahJinPengumpul(users) > 0

def jumlahJinPengumpul(users):
    jumlahJinPengumpul = 0
    for i in range(3,panjang(users)):
        if users[i][2] == "jin_pengumpul":
            jumlahJinPengumpul += 1
    return jumlahJinPengumpul



#* Batch Bangun -----------------------------------------------#
def batchBangun(users, candi, bahanBangunan):
    
    if not cekJinPengumpul():
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return
    
    
    
    return

def cekJinPembangun(users):
    return jumlahJinPembangun(users) > 0

def jumlahJinPembangun(users):
    jumlahJinPembangun = 0
    for i in range(3,panjang(users)):
        if users[i][2] == "jin_pembangun":
            jumlahJinPembangun += 1
    return jumlahJinPembangun

def cekJinPembangun():
    return db.jumlahJinPengumpul > 0



#* Laporan Jin -----------------------------------------------#
def laporanJin():
    return



#* Laporan Candi -----------------------------------------------#
def laporanCandi():
    return



#* Hancurkan Candi -----------------------------------------------#
def hancurkanCandi():
    return
