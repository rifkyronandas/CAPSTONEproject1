# ========== Text tampilan menu utama ==========

Text = '''
Selamat Datang di Ronans Rent Car

List Menu:
1.Menampilkan Daftar Mobil
2.Menambahkan Mobil
3.Menghapus Mobil
4.Melakukan Pemesanan Mobil
5.Melakukan Pembayaran
6.Keluar Progam
   
'''


# ========== Database Mobil ==========

list_mobil = [["Avanza",5,300000], ["Brio",3,250000],["Innova",2,450000]]

# ========== Fungsi Tampilkan Daftar Mobil ==========

def daftar_mobil(x):
    print("Daftar Mobil")
    print("\nIndex\t|Nama\t|SisaMobil\t|Harga(Rp.)")
    for i in x:
        print(f'{x.index(i)}\t|{i[0]}\t|{i[1]}\t|{i[2]}')



# ========== Fungsi Menambahkan Daftar Mobil ==========

def add_mobil():
    nama = input("Masukkan Nama Mobil yang di inginkan : ")
    stock = int(input("Masukkan Jumlah Kendaraan yang di inginkan :"))
    harga = int(input("Masukkan Harga Kendaraan yang di inginkan :"))
    t = [nama,stock,harga]
    list_mobil.append(t)
    daftar_mobil(list_mobil)
    print('Selamat, Mobil baru berhasil ditambahkan')

# ========== Fungsi Menghapus Mobil ==========

def hapus_mobil():
    daftar_mobil(list_mobil)
    try:
        index = int(input("Masukkan indeks mobil yang ingin dihapus: "))
        if 0 <= index < len(list_mobil):
            removed_car = list_mobil.pop(index)
            print(f"Mobil {removed_car[0]} telah dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Error: {e}")

# ========== Fungsi Pemesanan Mobil ==========

def order_mobil():
    daftar_mobil(list_mobil)
    try:
        index = int(input("Masukkan indeks mobil yang ingin dipesan: "))
        if 0 <= index < len(list_mobil):
            car = list_mobil[index]
            quantity = int(input(f"Masukkan jumlah mobil {car[0]} yang ingin dipesan: "))
            if 0 < quantity <= car[1]:
                print(f"Pemesanan untuk {quantity} mobil {car[0]} berhasil.")
                list_mobil[index][1] -= quantity  # Mengurangi stok mobil yang dipesan
            else:
                print("Jumlah mobil tidak valid.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Error: {e}")


# ========== Fungsi Pembayaran ==========

def payment():
    daftar_mobil(list_mobil)
    try:
        index = int(input("Masukkan indeks mobil yang ingin dibayar: "))
        if 0 <= index < len(list_mobil):
            car = list_mobil[index]
            ordered_quantity = int(input(f"Masukkan jumlah mobil {car[0]} yang ingin dibayar: "))
            if 0 < ordered_quantity <= car[1]:
                payment_quantity = int(input(f"Masukkan jumlah mobil {car[0]} yang ingin dibayar dari pemesanan: "))
                if 0 < payment_quantity <= ordered_quantity:
                    total_payment = payment_quantity * car[2]
                    print(f"Total pembayaran untuk {payment_quantity} mobil {car[0]} adalah Rp. {total_payment}")
                    list_mobil[index][1] -= payment_quantity  # Mengurangi stok mobil yang dibayar
                else:
                    print("Jumlah mobil yang dibayar tidak valid.")
            else:
                print("Jumlah mobil pesanan tidak valid.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Error: {e}")


# ========== Main Code ==========
while True :
    try:
        print(Text)
        i = int(input("Silahkan Masukan Nomor Menu :"))
        if i == 1:
            daftar_mobil(list_mobil)
        elif i == 2:
            add_mobil()
        elif i == 3:
            hapus_mobil()
        elif i == 4:
            order_mobil()
        elif i == 5:
            payment()
        elif i == 6:
            break
        else :
            print("Pilihan hanya 1-5")
    except ValueError:
        print('Input harus berupa angka')
    except Exception as e:
        print(f'Error: {e}')


