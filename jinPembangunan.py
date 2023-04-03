def cekJumlahBahanBangunan(jumlahYangDiperlukan,jumlahYangDimiliki):
    for i in range (3):
        if jumlahYangDimiliki[i] < jumlahYangDiperlukan[i]:
            return False
    return True
            
def jinPembangun():
    #! Random Algoritma
    
    if cekJumlahBahanBangunan() and JumlahCandiSisa != 0:
        print("Candi berhasil dibangun.")
        print(f"Sisa candi yang perlu dibangun: {jumlahCandiSisa}")
    elif cekJumlahBahanBangunan():
        print("Candi tidak bisa dibangun!")
        print(f"Sisa candi yang  perlu dibangun: {jumlahCandiSisa}")
    else:
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
        