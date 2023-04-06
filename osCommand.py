import numpy as np
import database as db

def printHelp():
    print(f'''
    ============HELP============
    
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          ''')
    return

def saveFile(): 
    # Masukkan batu,pasir,air ke array bahanBangunan
    toArraybahanBangunan()
    np.savetxt('Assets/user.csv', db.users, delimiter=';',fmt='%s')
    np.savetxt('Assets/candi.csv', db.candi, delimiter=';',fmt='%s')
    np.savetxt('Assets/bahan_bangunan.csv', db.bahanBangunan, delimiter=';',fmt='%s')
    np.savetxt('Assets/seeds.csv', db.seeds, delimiter=';',fmt='%s')
    return

def toArraybahanBangunan():
    db.bahanBangunan[1][2] = db.air
    db.bahanBangunan[2][2] = db.pasir
    db.bahanBangunan[3][2] = db.batu
    return
    

def exitCode():
    answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while answer != "y" and answer != "n":
        answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
            
    match answer:
        case "y":
            saveFile()
            return
        case "n":
            return
