from main import users

def login():
    username =  input("Username: ")
    password =  input("Password: ")
    
    if cekPassword(password,cekUsername()):
        print(f"Selamat datang, {username}")
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        return(username)
    elif cekUsername(username) != -1:
        print("Password Salah")
    else:
        print("Username tidak terdaftar!")
        
    return
          
def cekUsername(username):
    for i in range (panjang(users)):
        if users[i][0] == username:
            return i
    return -1

def cekPassword(password,i):
    return users[i][1] == password
