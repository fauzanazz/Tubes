# File : main.py

#! Import Modules
import os
import numpy as np
import argparse

#! Import SubSystem
import database as db
from PythonFunction import *

#! Import Function
from loginLogout import *
from osCommand import *
from adminCommands import *
from roroCommands import *
from jinPembangunan import *
from jinPengumpul import *

#* Exit File -------------------------------------------#
run = True

def doNotRun():
    run = False
    return run

#* Args ------------------------------------------------#

parser = argparse.ArgumentParser()
parser.add_argument('nama_folder', help="Mengecek folder yang berisi data yang akan di load",type=str)
args = parser.parse_args()
if not args.nama_folder:
    print("Tidak ada nama folder yang diberikan!")
    run = doNotRun()
    
if os.path.exists(args.nama_folder):
    print('''Loading...

Selamat datang di program “Manajerial Candi”
Silahkan masukkan username Anda
''')
else:
    print(f"Folder {args.nama_folder} tidak ditemukan")
    run = doNotRun()

# * Color Class ----------------------------------------#

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#* Local Storage ----------------------------------------------#
role = None; users = db.usersOutput; 
bahanBangunan = db.bahanBangunanOutput; candi = db.candiOutput
seeds = db.seedsOutput; pasir = db.pasir
batu = db.batu; air = db.air; jumlahCandi = db.jumlahCandi

#* Input  -----------------------------------------------#

while run:
    phase = input(f"{style.YELLOW}>>> {style.ENDC}")

    match phase:
        case "debug":
            print(f'''Role = {role}
                  users = {users}
                  candi = {candi}
                  bahanBangunan = {bahanBangunan}
                  seeds = {seeds}
                  pasir = {pasir}
                  batu = {batu}
                  air = {air}
                  jumlahCandi = {jumlahCandi}''')
        
        case "login":
            role = login(users)
            
        case "logout":
            role = logout()
            
        case "summonjin":
            os.system('cls')
            users = summonJin(users)
            
        case "hapusjin":
            (users,candi) = hapusJin(users,candi)
            
        case "ubahjin":
            ubahJin(users)
            
        case "bangun":
            jinPembangun(seeds)
            
        case "kumpul":
            pasir,batu,air,seeds[1][1] = jinPengumpul(int(seeds[1][1]),pasir,batu,air)
            
        case "batchkumpul":
            batchKumpul()
            
        case "batchbangun":
            batchBangun()
            
        case "laporanjin":
            laporanJin()
            
        case "laporancandi":
            laporanCandi()
            
        case "hancurkancandi":
            hancurkanCandi()
            
        case "ayamberkokok":
            ayamBerkokok()
    
        case "save":
            saveFile(users,candi,bahanBangunan,seeds,air,pasir,batu)
            
        case "help":
            printHelp()
            
        case "exit":
            exitCode(users,candi,bahanBangunan,seeds,air,pasir,batu)
            break