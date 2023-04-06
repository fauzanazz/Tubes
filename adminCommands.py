# adminCommands.py

import database as db
import loginLogout as login
import jinPembangun as jinBangun
import jinPengumpul as jinKumpul
import PythonFunction as f


#* Summon Jin -----------------------------------------------#

def summonJin():
    print('''
    Jenis Jin yang dapat dipanggil:
     (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
     (2) Pembangun - Bertugas membangun candi
     ''')
    
    while True:
        jenisJin = masukkanInteger()            
        
        match jenisJin:
            case 1:
                print(f"\nMemilih jin \"Pengumpul\"")
                jenisJin = "jin_pengumpul"
            case 2:
                print(f"\nMemilih jin \"Pembangun\"")
                jenisJin = "jin_pembangun"
        
        username = input("Masukkan username jin: ")
        while login.cekUsernameJin(username) != -1:
            print(f"Username \"{username}\" sudah diambil!")
            username = input("Masukkan username jin: ")
        
        password = input("Masukkan password jin: ")
        while not cekValidPassword(password):
            print("Password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")
        
        # Tambahkan user ke array user
        db.users = f.tambahArrayString(db.users,[[username,password,jenisJin]])
        
        print(f'''\n
        Mengumpulkan sesajen...
        Menyerahkan sesajen...
        Membacakan mantra...\n
        Jin {username} berhasil dipanggil!
              ''')
        return
        
def cekValidPassword(password):
    return f.panjang(password) >= 5 and f.panjang(password) <= 25
        
def masukkanInteger():
    masukan = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
    try:
        masukan = int(masukan)
    except:
    #! Case Handler masukan bukan Integer
        print("\nError masukan bukan Integer")
        masukan = masukkanInteger()
        
    while int(masukan) > 2 or int(masukan) < 1:
        print(f"\nTidak ada jenis jin bernomor \"{masukan}\"!")
        masukan = input("Masukkan nomor jenis jin yang ingin dipanggil:  ")
        try:
            masukan = int(masukan)
        except:
        #! Case Handler masukan bukan Integer
            print("\nError masukan bukan Integer")
            masukan = masukkanInteger()
            
    return masukan        
        
#* Hapus Jin -----------------------------------------------#   
                  
def hapusJin():
    usernameJin = input("Masukkan username jin: ")
    
    #* Buat Algoritma mencari username Jin
    if login.cekUsernameJin(usernameJin) > 0:
        index = login.cekUsernameJin(usernameJin)
        # Verifikasi
        verifikasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {usernameJin} (Y/N)? ")
    
        if verifikasi == "Y":
            #* Algoritma menghapus data jin
            db.users = f.remove(db.users,index)
            hapusCandi(usernameJin)
            # del db.usersOutput[cekUsernameJin(usernameJin)]
            print("Jin Telah berhasil dihapus dari alam gaib.")
            
        elif verifikasi == "N":
            print("Jin tidak jadi di hapus.")
            
        else:
            print("Input tidak Valid.")
    else:
        #! Bila Tidak, ada keluarkan case Handler
        print("Tidak ada jin dengan username tersebut.")
    
    return

def hapusCandi(usernamejin):
    for i in range(f.panjang(db.candi)):
        if db.candi[i][1] == usernamejin:
            db.candi = f.remove(db.candi,i)
    return
    
    
    
#* Ubah Jin -----------------------------------------------#

def ubahJin():
    usernameJin = input("Masukkan username jin: ")
    #* Buat Algoritma mencari username Jin
    if login.cekUsernameJin(usernameJin) > 0:
        index = login.cekUsernameJin(usernameJin)
        jenisJin = db.users[index][2]
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
            db.users[index][2] = ubah
            print("Jin telah berhasil diubah")
            
        elif verifikasi == "N":
            print("Jin tidak jadi di ubah.")
            
        else:
            print("Input tidak Valid.")
    else:
        #! Bila Tidak ada, keluarkan case Handler
        print("Tidak ada jin dengan username tersebut.")
    return
    
    

#* Batch Kumpul -----------------------------------------------#

def batchKumpul():
    
    if not cekJinPengumpul():
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return
    
    #let
    jumlahJinPengumpul = hitungJinPengumpul()
    
    
    print(f"Mengerahkan {jumlahJinPengumpul} jin untuk mengumpulkan bahan.")
    
    localPasir = 0
    localBatu = 0
    localAir = 0
    
    for i in range(jumlahJinPengumpul):
        localPasir,localBatu,localAir = jinKumpul.jinPengumpulOveride(localPasir,localBatu,localAir)
    
    print(f"Jin menemukan total {localPasir} pasir, {localBatu} batu, {localAir} air.")

    return


def cekJinPengumpul():
    return hitungJinPengumpul() > 0


def hitungJinPengumpul():
    jumlahJinPengumpul = 0
    for i in range(3,f.panjang(db.users)):
        if db.users[i][2] == "jin_pengumpul":
            jumlahJinPengumpul += 1
    return jumlahJinPengumpul



#* Batch Bangun -----------------------------------------------#
def batchBangun():
    
    if not cekJinPembangun():
        print("Kumpul gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return
    
    # Let
    jumlahJinPembangun = hitungJinPembangun()
    tempCandi = []
    butuhAir = 0
    butuhPasir = 0
    butuhBatu = 0
    
    # Random Algorithm 
    for i in range(1,f.panjang(db.users)):
            if db.users[i][2] == "jin_pembangun":
                butuhPasir, butuhBatu, butuhAir, tempCandi = jinBangun.jinPembangunOveride(i,tempCandi,butuhAir,butuhPasir,butuhAir,i) 
                
    
    print(f"Mengerahkan {jumlahJinPembangun} jin untuk membangun candi dengan total bahan {butuhPasir} pasir, {butuhBatu} batu, {butuhAir} air.")
    
    # Cek kondisi
    if jinBangun.cekJumlahBahanBangunan(butuhPasir,butuhAir,butuhBatu) and jinBangun.cekJumlahCandi():
    
        db.candi = f.tambahArrayString(db.candi,tempCandi)
        print(f"Jin berhasil membangun total {jumlahJinPembangun} candi.")
        db.pasir -= butuhPasir 
        db.batu -= butuhBatu
        db.air -= butuhAir
        jinBangun.reloadDataCandi()
        return
    
    elif jinBangun.cekJumlahBahanBangunan(butuhPasir,butuhAir,butuhBatu) and not jinBangun.cekJumlahCandi():
        print("Candi tidak bisa dibangun!")
        
    else:
        kurangPasir = butuhPasir - db.pasir
        kurangBatu = butuhBatu - db.batu
        kurangAir = butuhAir - db.air
        print(f"Bangun gagal. kurang {kurangPasir} pasir, {kurangBatu} batu, {kurangAir} air.")
        
    return

def cekJinPembangun():
    return hitungJinPembangun() > 0

def hitungJinPembangun():
    jumlahJinPembangun = 0
    for i in range(3,f.panjang(db.users)):
        if db.users[i][2] == "jin_pembangun":
            jumlahJinPembangun += 1
    return jumlahJinPembangun


#* Laporan Jin -----------------------------------------------#
def laporanJin():
    
    # if db.role != "bandung_bondowoso":
    #     print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    #     return


    print(f'''
> Total Jin       : {db.jumlahJinPemabangun+db.jumlahJinPengumpul}
> Total jin Pengumpul : {db.jumlahJinPengumpul}
> Total jin Pembangun : {db.jumlahJinPemabangun}
> Jin Terajin         :
> Jin Termalas        :
> Jumlah Pasir        : {db.pasir} unit
> Jumlah Air          : {db.air} unit
> Jumlah Batu         : {db.batu} unit
          ''')
    return

#* Laporan Candi -----------------------------------------------#
def laporanCandi():
    
    # if db.role != "bandung_bondowoso":
    #     print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    #     return
    
    print(f'''
> Total Candi                   : {db.jumlahCandi}
> Total Pasir yang digunakan    : {db.pasirTerpakai}
> Total Batu yang digunakan     : {db.batuTerpakai}
> Total Air yang digunakan      : {db.airTerpakai}''')
    if db.jumlahCandi != 0:
        print(f'''> ID Candi Termahal             : {db.candiTermahal[1]} (Rp {db.candiTermahal[0]})
> ID Candi Termurah             : {db.candiTermurah[1]} (Rp {db.candiTermurah[0]})
              ''')
    else:
        print(f'''> ID Candi Termahal             : -
> ID Candi Termurah             : -
              ''')
    
    return
