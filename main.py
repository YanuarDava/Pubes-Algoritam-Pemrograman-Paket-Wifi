import glob # library untuk mencari file .txt
import os # library untuk clear tampilan

# Struktur Data Yang Akan Disimpan
TEMPLATE = {
    "nama": " "*50,
    "nohp": " "*50,
    "mbps": " "*50,
    "tagihan": " "*50,
}

# Menu Awal
def menu():
    os.system("cls")
    print("Selamat Datang Di Program".center(60))
    print("Pemabyaran/Daftar Wifi".center(59) + "\n")
    print("""
            ===================================
            | Nomer | Menu                    |
            ===================================
            |   1   | Masuk Kemenu User       |
            |   2   | Masuk Kemenu Admin      |
            ===================================
            """)

# Read Paket
def read_produk():
    os.system("cls")
    daftar_paket = glob.glob('paket wifi/*.txt')    
    pjng_file = len(daftar_paket)

    # Tabel Atas
    print("="*56)
    print("Berikut Daftar Produk Wifi Kami".center(53))
    print("="*56)
    # Tengah Tabel
    for data in range(pjng_file):
        daftar_paket[data] = daftar_paket[data].replace(".txt"," ")
        print(daftar_paket[data])
    # Bawah Tabel 
    print("="*56)

    # panggil Fungsi untuk Memilih Paket
    pilih_paket()

# User Memilih Paket dan Kecepatan Wifinya
def pilih_paket():
    paket_yg_dipilih = input("Masukkan Nama Paket\t: ") + ".txt"
    os.system("cls")
    with open(paket_yg_dipilih,"r") as file:
        data = file.readlines()
        pjng = len(data)
        
        no = 1
        # Atas Tabel
        print("="*25)
        print("Berikut Harga Paket Kami")
        print("="*25)
        # Bawah Tabel
        for content in data:
            content = content.split(",")
            kecepatan_wifi = content[0].replace('\n', '')
            harga_paket = content[1].replace('\n', '')
            print(f"Kecepatan {no}\t: {kecepatan_wifi}")
            print(f"Harga Paket {no}\t: Rp{harga_paket} ribu/bulan")
            print("="*25)
            no+=1
    
    pilihan = int(input("Masukkan Nomor Pilihan Anda\t:"))
    simpan_pesanan(pilihan, paket_yg_dipilih)

# Menyimpan Pesanan Kedalam File data.txt
def simpan_pesanan(pilihan, paket_yg_dipilih):
    os.system("cls")
    nama = input("Masukkan Nama Anda       : ")
    nomor = input("Masukkan Nomor Hp Anda   : ")

    with open(paket_yg_dipilih,"r+") as file:
        data = file.readlines()
        for index,data in enumerate(data):
            data = data.split(",")
            pilihan -= 1
            if index == pilihan:
                break

    kecepatan_wifi = data[0]
    tagihan = data[1].replace("\n","")
    
    # struktur data di copy dari template
    database = TEMPLATE.copy()
    
    database["nama"] = nama + TEMPLATE["nama"][len(nama):]
    database["nohp"] = nomor  + TEMPLATE["nohp"][len(nomor):]
    database["mbps"] = kecepatan_wifi  + TEMPLATE["mbps"][len(kecepatan_wifi):]
    database["tagihan"] = tagihan  + TEMPLATE["tagihan"][len(tagihan):]

    data_str = f"{database['nama']},{database['nohp']},{database['mbps']},{database['tagihan']}\n"

    with open("data.txt","a") as file:
        file.write(data_str)

    struk_belanja(nama, nomor, kecepatan_wifi, tagihan)

# Print Data Customer dan Paket Yang Di pesan
def struk_belanja(nama, nomor, kecepatan_wifi, tagihan):
    os.system("cls")
    print("="*17)
    print("Berikut Data Anda")
    print("="*17)
    print(f"Nama  : {nama}")
    print(f"No.Hp : {nomor}")
    
    print("="*18)
    print("Paket Yang Dipesan")
    print("="*18)
    print(f"Kecepatan Wifi : {kecepatan_wifi}")
    tagihan = tagihan.replace("\n", "")
    print(f"Tagihan        : Rp{tagihan.replace(' ', '')} ribu/bulan")

# Menu Admin
def menu_admin():
    os.system("cls")
    print("Selamat Datang Di Program".center(60))
    print("Pembayaran/Daftar Wifi".center(59) + "\n")
    print("""
            ===================================
            | Nomer | Menu                    |
            ===================================
            |   1   | Read Data               |
            |   2   | Sort Data               |
            |   3   | Update Data             |
            |   4   | Delete Data             |
            |   5   | Exit                    |
            ===================================
            """)

# Read Seluruh Data Dalam file data.txt   
def read_data():
    with open("data.txt","r") as file:
        data = file.readlines()
        # Bagian Atas Tabel
        print("========================================================================")
        print(f"No | Nama            | Nomor           | Mbps            | Tagihan     |")
        print("========================================================================")
        index = 1
        # Content Di Tabel
        for content in data:
            content = content.split(",")
            nama = content[0]
            nomor = content[1]
            kecepatan_wifi = content[2]
            tagihan = content[3]   
            print(f"{index:2} | {nama:.15} | {nomor:.15} | {kecepatan_wifi:.15} | Rp{tagihan:.10}|")
            index+=1
        # Bagian Bawah Tabel
        print("========================================================================")
        x = input(" ")

# Sorting Data .txt
def sort_data():
    with open("data.txt","r") as file:
        data = file.readlines()
        data.sort()
        # Bagian Atas Tabel
        print("========================================================================")
        print(f"No | Nama            | Nomor           | Mbps            | Tagihan     |")
        print("========================================================================")
        index = 1
        # Content Di Tabel
        for content in data:
            content = content.split(",")
            nama = content[0]
            nomor = content[1]
            kecepatan_wifi = content[2]
            tagihan = content[3]   
            print(f"{index:2} | {nama:.15} | {nomor:.15} | {kecepatan_wifi:.15} | Rp{tagihan:.10}|")
            index+=1
        # Bagian Bawah Tabel
        print("========================================================================")
        x = input(" ")

# Update Data
def update_data():
    read_data()
    pilih = int(input("Masukkan No Data Yang Ingin Di Update\t: "))
    pilih-=1
    with open("data.txt","r") as file:
        data = file.readlines()
        for index,data in enumerate(data):
            data_split = data.split(",")
            if index == int(pilih):
                break
    
    nama = data_split[0].replace(" ", "")
    nomor = data_split[1].replace(" ", "")
    mbps = data_split[2]
    tagihan = data_split[3].replace(" ", "")
    struk_belanja(nama, nomor, mbps, tagihan)

    print("\n1. Update Nama\n2. Update Nomor")
    usr_opsi = input("Masukkan Data Yang Ingin Di Update [1,2]\t: ")
    match usr_opsi:
        case "1": nama = input("Masukkan Nama Baru\t: ")
        case "2": nomor = input("Masukkan Nomor Handphone Baru\t: ")

    tagihan = tagihan.replace("\n","")
    
    # Struktur Data Disalin Dari Template Dan Ditulis Kedalam data.txt
    database = TEMPLATE.copy()
    
    database["nama"] = nama + TEMPLATE["nama"][len(nama):]
    database["nohp"] = nomor + TEMPLATE["nohp"][len(nomor):]
    database["mbps"] = mbps + TEMPLATE["mbps"][len(mbps):]
    database["tagihan"] = tagihan + TEMPLATE["tagihan"][len(tagihan):]

    data_str = f"{database['nama']},{database['nohp']},{database['mbps']},{database['tagihan']}\n"
    with open("data.txt","r+",encoding="utf-8") as file:
        file.seek(pilih * (len(data_str)))
        file.write(data_str)

# cancel Data
def cancel_pesanan():
    read_data()
    pilih = int(input("Masukkan Nomer Data Yang Ingin Di Delete\t: "))
    pilih-=1
    
    with open("data.txt","r") as file:
        data = file.readlines()
        for index,data in enumerate(data):
            data_split = data.split(",")
            if index == int(pilih):
                break
    
    nama = data_split[0].replace(" ", "")
    nomor = data_split[1].replace(" ", "")
    mbps = data_split[2]
    tagihan = data_split[3].replace(" ", "")
    struk_belanja(nama, nomor, mbps, tagihan)

    opsi = input("Yakin Ingin Dihapus (y/n)\t: ")

    if opsi == "y":
        with open("data.txt","r") as file:
            data = file.readlines()
            
            with open("data.txt","w") as file:
                for index,data in enumerate(data):
                    if index != pilih:
                        file.write(data)

# Program Di Mulai Dari Sini
while True:
    menu()
    user_options = input("Masukkan Opsi\t: ")
    while True:    
        if user_options == "1":
            read_produk()
            brek = input("Apakah Selesai (y/n): ")
            if brek == "y":
                break
        elif user_options == "2":
            menu_admin()
            user_option = input("Pilih Opsi\t: ")
            match user_option:
                case "1": read_data()
                case "2": sort_data()
                case "3": update_data()
                case "4": cancel_pesanan()
                case "5": break
        

