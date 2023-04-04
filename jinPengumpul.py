from PythonFunction import *

def jinPengumpul(seeds,pasir,air,batu):
    localSeeds = seeds
    #! Random Algorithm
    localpasir,localSeeds = rando(localSeeds,5)
    localbatu,localSeeds = rando(localSeeds,5)
    localair,localSeeds = rando(localSeeds,5)
    print(f"Jin menemukan {localpasir} pasir, {localbatu} batu, dan {localair} air.")
    return localpasir+pasir, localbatu+batu, localair+air, localSeeds