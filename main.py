# File : main.py

#! Import Modules
import os
import numpy as np
import argparse

#! Import SubSystem
import database as db
from PythonFunction import *

#! Import Function
import loginLogout as login
import osCommand as osCommand
import adminCommands as admin
import roroCommands as roro
import jinPembangun as jinBangun
import jinPengumpul as jinKumpul

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

#* Input  -----------------------------------------------#

while run:
    phase = input(f"{style.YELLOW}>>> {style.ENDC}")

    match phase:
        case "debug":
            print(f'''Role = {db.role}
                  username = {db.username}
                  users = {db.users}
                  candi = {db.candi}
                  bahanBangunan = {db.bahanBangunan}
                  seeds = {db.seeds}
                  pasir = {db.pasir}
                  batu = {db.batu}
                  air = {db.air}
                  jumlahCandi = {db.jumlahCandi}''')
        
        case "login":
            role = login.login()
            
        case "logout":
            role = login.logout()
            
        case "summonjin":
            os.system('cls')
            admin.summonJin()
            
        case "hapusjin":
            admin.hapusJin()
            
        case "ubahjin":
            admin.ubahJin()
            
        case "bangun":
            jinBangun.jinPembangun()
            
        case "kumpul":
            jinKumpul.jinPengumpul()
            
        case "batchkumpul":
            admin.batchKumpul()
            
        case "batchbangun":
            admin.batchBangun()
            
        case "laporanjin":
            admin.laporanJin()
            
        case "laporancandi":
            admin.laporanCandi()
            
        case "hancurkancandi":
            roro.hancurkanCandi()
            
        case "ayamberkokok":
            roro.ayamBerkokok()
    
        case "save":
            osCommand.saveFile()
            
        case "help":
            osCommand.printHelp()
            
        case "exit":
            osCommand.exitCode()
            break