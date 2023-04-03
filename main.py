# File : main.py

from login import login
from PythonFunction import *


phase = input()

users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

# Open data
users = open("Assets/user.csv", "r")
candi = open("Assets/candi.csv", "r")
bahan_bangunan = open("Assets/bahan_bangunan.csv", "r")

# Parse CSV to Array
for i in users:
    users[i] = bagiArray(users[i],';')
    
    
    
    
    
# users = load("Assets/user.csv")
# candi = load("Assets/candi.csv")
# bahan_bangunan = load("Assets/bahan_bangunan.csv")


# match phase:
#     case "login":
#         login()
#     case "logout":
#         logout()
#     case "summonjin":
#         summonJin()
#     case "hapusjin":
#         hapusJin()
#     case "ubahjin":
#         ubahJin()
#     case "bangun":
#         jinPembangun()
#     case "kumpul":
#         jinPengumpul()
#     case "batchkumpul":
#         batchKumpul()
#     case "batchbangun":
#         batchBangun()
#     case "laporanjin":
#         laporanJin()
#     case "laporancandi":
#         laporanCandi()
#     case "hancurkancandi":
#         hancurkanCandi()
#     case "ayamberkokok":
#         ayamBerkokok()
#     case "save":
#         saveFile()
#     case "help":
#         printHelp()
#     case "exit":
#         exitCode()
        



