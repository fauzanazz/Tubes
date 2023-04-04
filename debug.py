from PythonFunction import *
import numpy as np
import os

# System call
# os.system("")

# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
# for style in range(8):
#     for fg in range(30,38):
#         s1 = ''
#         for bg in range(40,48):
#             format = ';'.join([str(style), str(fg), str(bg)])
#             s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#         print(s1)
#     print('\n')
    
# print("\x1b[7;30;44m Seng seng seng \x1b[0m")

# print_format_table()

# class style():
#     BLACK = '\033[30m'
#     RED = '\033[31m'
#     GREEN = '\033[32m'
#     YELLOW = '\033[33m'
#     BLUE = '\033[34m'
#     MAGENTA = '\033[35m'
#     CYAN = '\033[36m'
#     WHITE = '\033[37m'
#     UNDERLINE = '\033[4m'
#     RESET = '\033[0m'
    
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# print(style.YELLOW + "Hello, World!" + style.RESET)
# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
# print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")


# RNG  
# a = 1231
# m = (2**31)
# c = 0
# seeds = 230404
# x = [0 for i in range(2)]
# countarray = [0 for i in range (7)]
# for i in range(100):
#     x[0] = ((a*seeds)+c)%m
#     rng = (((x[0]/(2*10**9))*5)+1)//1
#     seeds = x[0]
#     print(rng)
#     countarray[int(rng)] += 1

# print(countarray)
# users = open("Assets/user.csv", "r")
# readfile = users.read() # input File

# # Algoritma CSV to array
# users = (bagiArrayString(readfile,'\n'))

# # Container
# usersOutput = ['' for i in range (panjang(users))]
# for i in range (panjang(users)):
#     usersOutput[i] = (bagiArrayString(users[i],';'))

# print(usersOutput)

# users = open("Assets/user.csv", "r")
# candi = open("Assets/candi.csv", "r")
# bahan_bangunan = open("Assets/bahan_bangunan.csv", "r")


# # Users
# readfile = bahan_bangunan.read() # input File

# # Algoritma CSV to array
# users = (bagiArrayString(readfile,'\n'))

# # Container
# usersOutput = ['' for i in range (panjang(users))]
# for i in range (panjang(users)):
#     usersOutput[i] = (bagiArrayString(users[i],';'))
    
# print(usersOutput)

# print(np.asarray(usersOutput))
# np.savetxt('Assets/test.csv', usersOutput, delimiter=';',fmt='%s')
# def remove(arr,index):
#     output = [0 for i in range(panjang(arr)-1)]
#     for i in range(index+1):
#         output[i] = arr[i]
#     for i in range(index,panjang(arr)-1):
#         output[i] = arr[i+1]
#     return output
# print(remove([[1,2,3],[2,3,4],[3,4,5]],2))

# print(tambahArrayString([1,2,3],[3,4,4]))


# x = ((1231*230404)+0) % (2**31)
# seeds = x
# rng = ((x/(2*10**9))*5)//1

# if rng > 1:
#     rng = 1

# print(rng)

bahan_bangunan = open("Assets/bahan_bangunan.csv", "r")
readfile = bahan_bangunan.read() # input File

# Algoritma CSV to array
bahan_bangunan = (bagiArrayString(readfile,'\n'))

# Container
bahanBangunanOutput = ['' for i in range (panjang(bahan_bangunan)-1)]
for i in range (panjang(bahan_bangunan)-1):
    bahanBangunanOutput[i] = (bagiArrayString(bahan_bangunan[i],';'))

print (readfile)
print (bahanBangunanOutput)
# print (bagiArrayString(bahanBangunanOutput[0],';'))
# print (bagiArrayString(bahanBangunanOutput[1],';'))
# print (bagiArrayString(bahanBangunanOutput[2],';'))
# print (bagiArrayString(bahanBangunanOutput[3],';'))