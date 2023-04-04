import numpy as np
import database as db

def printHelp():
    print(f'''
    ============HELP============
    
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          ''')
    return

def saveFile(users,candi,bahanBangunan,seeds,air,pasir,batu):
    # Masukkan batu,pasir,air ke array bahanBangunan
    bahanBangunan = toArraybahanBangunan(bahanBangunan,air,pasir,batu)
    np.savetxt('Assets/user.csv', users, delimiter=';',fmt='%s')
    np.savetxt('Assets/candi.csv', candi, delimiter=';',fmt='%s')
    np.savetxt('Assets/bahan_bangunan.csv', bahanBangunan, delimiter=';',fmt='%s')
    np.savetxt('Assets/seeds.csv', seeds, delimiter=';',fmt='%s')
    return

def toArraybahanBangunan(bahanBangunan,air,pasir,batu):
    localBahanBangunan = bahanBangunan
    localBahanBangunan[1][2] = air
    localBahanBangunan[2][2] = pasir
    localBahanBangunan[3][2] = batu
    return localBahanBangunan
    

def exitCode(users,candi,bahanBangunan,seeds,air,pasir,batu):
    answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while answer != "y" and answer != "n":
        answer = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
            
    match answer:
        case "y":
            saveFile(users,candi,bahanBangunan,seeds,air,pasir,batu)
            return
        case "n":
            return
