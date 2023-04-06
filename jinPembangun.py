import PythonFunction as f
import database as db

def cekJumlahBahanBangunan(butuhPasir,butuhAir,butuhBatu):
    if db.pasir - butuhPasir < 0:
        return False
    if db.air - butuhAir < 0:
        return False
    if db.batu - butuhBatu < 0:
        return False
    
    return True


def cekJumlahCandi():
    return 100 - db.jumlahCandi > 0
            
def cekIndex():
    for i in range(f.panjang(db.candi)):
        if db.candi[i][0] == i== i:
            i += 1
            continue
    return i

def cekIndexbatch():
    index = None
    for i in range(f.panjang(db.candi)):
        if db.candi[i][0] == i:
            i += 1
            continue
        break
    return i
            
def jinPembangun():
    
    #! Random Algoritma
    butuhPasir = f.rando(5)
    butuhBatu = f.rando(5)
    butuhAir = f.rando(5)
    
    #Cek Cukup atau tidak.
    if cekJumlahBahanBangunan(butuhPasir,butuhAir,butuhBatu) and cekJumlahCandi():
        hargaCandi = 10000 * butuhPasir + 15000 * butuhBatu + 7500 * butuhAir
        index = cekIndex()
            
        db.candi = f.tambahArrayString(db.candi,[[index,db.username,butuhPasir,butuhAir,butuhBatu,hargaCandi]])
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {99 - db.jumlahCandi}")
        
        #Save value ke database
        db.pasir -= butuhPasir
        db.batu -= butuhBatu
        db.air -= butuhAir
        db.jumlahCandi += 1
        reloadDataCandi()
        return 
    
    elif cekJumlahBahanBangunan(butuhPasir,butuhAir,butuhBatu) and not cekJumlahCandi():
        print("Candi tidak bisa dibangun!")
        print(f"Sisa candi yang  perlu dibangun: {100 - db.jumlahCandi}")
        
    else:
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")   
        
    return

def jinPembangunOveride(index,tempCandi,localpasir,localair,localbatu,plusIndex):
    
    #! Random Algoritma
    butuhPasir= f.rando(5)
    butuhBatu= f.rando(5)
    butuhAir= f.rando(5)
    hargaCandi = 10000 * butuhPasir + 15000 * butuhBatu + 7500 * butuhAir

    localCandi = tempCandi
    index = cekIndexbatch()
    localCandi = f.tambahArrayString(localCandi,[[index+plusIndex,db.users[index][0],butuhPasir,butuhAir,butuhBatu,hargaCandi]])
    
        
    return butuhPasir+localpasir, butuhBatu+localbatu, butuhAir+localair, localCandi

def reloadDataCandi():
    db.pasirTerpakai = 0
    db.batuTerpakai = 0 
    db.airTerpakai = 0
    db.jumlahCandi = 0
    if f.panjang(db.candi) > 2:
        for i in range(1,f.panjang(db.candi)):
            db.pasirTerpakai += int(db.candi[i][2])
            db.batuTerpakai += int(db.candi[i][3])
            db.airTerpakai += int(db.candi[i][4])
            db.jumlahCandi += 1
            
        if i == 1:
            db.candiTermahal = (int(db.candi[i][5]),i)
            db.candiTermurah = (int(db.candi[i][5]),i)
        
        if db.candiTermahal[0] < int(db.candi[i][5]):
            db.candiTermahal = (int(db.candi[i][5]),i)
            
        if db.candiTermurah[0] > int(db.candi[i][5]):   
            db.candiTermurah = (int(db.candi[i][5]),i)
        