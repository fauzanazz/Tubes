def ubahTipeJin():
    usernameJin = input("Masukkan username jin: ")
    #* Buat Algoritma mencari username Jin
    #! Bila Tidak ada keluarkan case Handler
    print("Tidak ada jin dengan username tersebut.")
    
    # Verifikasi
    verifikasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?")
    if verifikasi.upper() == "Y":
        #*Algoritma menghapus data jin
        print("Jin Telah berhasil dihapus dari alam gaib.")
    elif verifikasi.upper() == "N":
        print("Jin tidak jadi di hapus.")
    else:
        print("Input tidak Valid.")