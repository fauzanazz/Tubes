import PythonFunction as f
import database as db

def jinPengumpul():
    
    #! Random Algorithm
    localpasir= f.rando(5,db.seeds[1][1])
    localbatu= f.rando(5)
    localair= f.rando(5)
    
    #Output
    print(f"Jin menemukan {localpasir} pasir, {localbatu} batu, dan {localair} air.")
    
    #Masukkan data ke database
    db.pasir += localpasir
    db.batu += localbatu 
    db.air += localair
    return

def jinPengumpulOveride(pasir,batu,air):
    
    #! Random Algorithm
    localpasir = f.rando(5)
    localbatu= f.rando(5)
    localair= f.rando(5)
    
    #Masukkan data ke database
    db.pasir += localpasir
    db.batu += localbatu 
    db.air += localair
    
    return localpasir+pasir,localbatu+batu,localair+air