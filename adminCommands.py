# adminCommands.py

import database as db
import jinPembangun as jinBangun
import jinPengumpul as jinKumpul
import PythonFunction as f

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
    for i in range(2,101):
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
    for i in range(100):
        if db.users[i][2] == "jin_pembangun":
            indexCandi = jinBangun.cekIndexbatch(tempCandi)
            butuhPasir, butuhBatu, butuhAir, tempCandi = jinBangun.jinPembangunOveride(i,tempCandi,butuhAir,butuhPasir,butuhAir,indexCandi)
                
    
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
    for i in range(100):
        if db.users[i][2] == "jin_pembangun":
            jumlahJinPembangun += 1
    return jumlahJinPembangun


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
