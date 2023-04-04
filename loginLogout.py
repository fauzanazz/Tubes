from PythonFunction import *

def login(user):
    username =  input("Username: ")
    password =  input("Password: ")
    
    if cekPassword(password,cekUsername(username,user),user):
        print(f"\nSelamat datang, {username}")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        return(username)
    elif cekUsername(username) != -1:
        print("\nPassword Salah")
    else:
        print("Username tidak terdaftar!")
        
    return
          
def cekUsernameJin(username,user):
    for i in range (3,panjang(user)):
        if user[i][0] == username:
            return i
    return -1

def cekUsername(username,user):
    for i in range (1,panjang(user)):
        if user[i][0] == username:
            return i
    return -1

def cekPassword(password,i,user):
    return user[i][1] == password

def logout():
    role = None
    return role