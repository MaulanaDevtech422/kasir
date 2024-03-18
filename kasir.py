# Daftar menu makanan ringan beserta harga
menu = {
    1: {"nama": "Keripik Kentang", "harga": 6000},
    2: {"nama": "Kacang Panggang", "harga": 8000},
    3: {"nama": "Popcorn", "harga": 10000},
    4: {"nama": "Es Krim Cone", "harga": 12000},
    5: {"nama": "Churros", "harga": 15000},
    6: {"nama": "Nachos", "harga": 18000},
    7: {"nama": "Pizza Slice", "harga": 20000},
    8: {"nama": "Donat", "harga": 7000},
    9: {"nama": "Singkong Goreng", "harga": 9000},
    10: {"nama": "Pisang Goreng", "harga": 11000},
    11: {"nama": "Bakwan Jagung", "harga": 13000},
    12: {"nama": "Roti Bakar", "harga": 16000}
}

# Fungsi untuk menampilkan daftar menu
def tampilkan_menu():
    print("=== MENU MAKANAN RINGAN ===")
    for nomor, item in menu.items():
        print(f"{nomor}. {item['nama']}: Rp{item['harga']}")

# Fungsi untuk menghitung total pembayaran
def hitung_total(pesanan):
    total = sum(menu[item]["harga"] for item in pesanan)
    return total

# Main program
def main():
    pesanan = []
    tampilkan_menu()
    while True:
        pilihan = input("Masukkan pilihan makanan: ")
        if pilihan.lower() == 'ok':
            break
        elif pilihan.isdigit():
            nomor_pilihan = int(pilihan)
            if nomor_pilihan in menu:
                pesanan.append(nomor_pilihan)
            else:
                print("Nomor makanan tidak valid, silakan pilih nomor yang sesuai.")
        else:
            print("Input tidak valid, silakan masukkan nomor makanan atau ketik 'ok'.")
    total_pembayaran = hitung_total(pesanan)
    print(f"Total pembayaran: Rp{total_pembayaran}")

if __name__ == "__main__":
    main()

#cara install di terminal
# apt update && apt upgrade
# pkg install python3
# pkg install git
# git clone https://github.com/MaulanaDevtech422/kasir
# ls
# cd kasir
# python3 kasir.py
# selesai silahkan mencoba 
