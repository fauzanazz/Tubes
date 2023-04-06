# roroCommands.py
import database as db
import PythonFunction as f


#* Hancurkan Candi -----------------------------------------------#
def hancurkanCandi():
    while True:
        idCandi = masukkanInteger()
        
        #Verifikasi
        try:
            db.candi = f.remove(db.candi,idCandi)
        except:
            print("\nTidak ada candi dengan ID tersebut.")
            return
        
        verifikasi = input(f"Apakah anda yakin ingin menghancurkan candi ID:{idCandi} (Y/N)? ")
    
        if verifikasi == "Y":
            #* Algoritma menghapus data jin
            db.candi = f.remove(db.candi,idCandi)
            print("Candi Telah berhasil dihancurkan.")
            
        elif verifikasi == "N":
            print("Candi tidak jadi dihancurkan.")
            
        else:
            print("Input tidak Valid.") 

        return

def masukkanInteger():
    masukan = input("Masukkan ID candi: ")
    try:
        masukan = int(masukan)
    except:
    #! Case Handler masukan bukan Integer
        print("\nError masukan bukan Integer")
        masukan = masukkanInteger()
        
    while int(masukan) < 0:
        print(f"\nTidak ada jenis jin bernomor \"{masukan}\"!")
        masukan = input("Masukkan ID candi:  ")
        try:
            masukan = int(masukan)
        except:
        #! Case Handler masukan bukan Integer
            print("\nError masukan bukan Integer")
            masukan = masukkanInteger()
            
    return masukan   

#* Ayam Berkokok -----------------------------------------------#
def ayamBerkokok():
    return
