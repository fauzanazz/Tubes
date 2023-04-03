def summonjin():
    print('''
    Jenis Jin yang dapat dipanggil:
     (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
     (2) Pembangun - Bertugas membangun candi
     ''')
    
    while True:
        jenisJin = input()
        if jenisJin < 3 and jenisJin > 0:
            break
        print(f"Tidak ada jenis jin bernomor \"{jenisJin}\"!")
    
    match jenisJin:
        case 1:
            1