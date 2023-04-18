# File : main.py

#! Import Modules
import os
import argparse

#! Import SubSystem
import database as db
from PythonFunction import *

#! Import Function
import adminCommands as admin
import jinPembangun as jinBangun
import jinPengumpul as jinKumpul

#* Exit File -------------------------------------------#
run = False

def run():
    return True

#* Args ------------------------------------------------#

parser = argparse.ArgumentParser()
parser.add_argument('nama_folder', nargs='?', default=None, help="Mengecek folder yang berisi data yang akan di load")
args = parser.parse_args()

if not args.nama_folder:
    print("Tidak ada nama folder yang diberikan!")
elif os.path.isdir(args.nama_folder):
    run = run()
    db.seeds,db.users,db.candi,db.bahanBangunan = db.load(args.nama_folder)
    db.jumlahPasir,db.jumlahBatu,db.jumlahAir,db.jumlahJinPembangun,db.jumlahJinPengumpul,db.pasirTerpakai,db.batuTerpakai,db.airTerpakai,db.jumlahCandi,db.candiTermahal,db.candiTermurah = db.hitung()
    print('''Loading...
    Selamat datang di program “Manajerial Candi”
    Silahkan masukkan username Anda
    ''')
else:
    print(f"Folder {args.nama_folder} tidak ditemkan")

#* Input  -----------------------------------------------#

while run:
    phase = input("\033[33m>>> \033[0m")

    if phase == "debug":
        print(f'''Role = {db.role}
                username = {db.username}
                users = {db.users}
                candi = {db.candi}
                bahanBangunan = {db.bahanBangunan}
                seeds = {db.seeds}
                pasir = {db.jumlahPasir}
                batu = {db.jumlahBatu}
                air = {db.jumlahAir}
                jumlahCandi = {db.jumlahCandi}''')
    
    # elif phase == "login":
    #     role = login.login()
        
    # elif phase == "logout":
    #     role = login.logout()
        
    # elif phase == "summonjin":
    #     os.system('cls')
    #     admin.summonJin()
        
    # elif phase == "hapusjin":
    #     admin.hapusJin()
        
    # elif phase == "ubahjin":
    #     admin.ubahJin()
        
    # elif phase == "bangun":
    #     jinBangun.jinPembangun()
        
    # elif phase == "kumpul":
    #     jinKumpul.jinPengumpul()
        
    elif phase == "batchkumpul":
        admin.batchKumpul()
        
    elif phase == "batchbangun":
        admin.batchBangun()
        
    # elif phase == "laporanjin":
    #     admin.laporanJin()
        
    elif phase == "laporancandi":
        admin.laporanCandi()
        
    # elif phase == "hancurkancandi":
    #     roro.hancurkanCandi()
        
    # elif phase == "ayamberkokok":
    #     roro.ayamBerkokok()

    # elif phase == "save":
    #     osCommand.saveFile()
        
    # elif phase == "help":
    #     osCommand.printHelp()
        
    # elif phase == "exit":
    #     osCommand.exitCode()
    #     break
    else:
        print("comman tidak ada")