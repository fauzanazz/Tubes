import PythonFunction as f
import database as db

def login():
    username =  input("Username: ")
    password =  input("Password: ")
    
    if cekPassword(password,cekUsername(username)):
        print(f"\nSelamat datang, {username}")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        index = cekUsername(username)
        db.role = db.users[index][2]
        return()
    elif cekUsername(username) != -1:
        print("\nPassword Salah")
    else:
        print("Username tidak terdaftar!")
    return
          
def cekUsernameJin(username):
    for i in range (3,f.panjang(db.users)):
        if db.users[i][0] == username:
            return i
    return -1

def cekUsername(username):
    for i in range (1,f.panjang(db.users)):
        if db.users[i][0] == username:
            return i
    return -1

def cekPassword(password,i):
    return db.users[i][1] == password

def logout():
    db.role = None
    return