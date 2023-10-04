#function
def pemesanan():
    print("================================")
    print("               FILM             ")
    print("================================")
    print("1. Dilan")
    print("2. Pengabdi Setan")
    print("3. Habibie & Aiunun")
    print("4. Laskar Pelangi")
    print("5. Yowes Ben")
    print("================================")

    while(True):
        film_pilihan = int(input("Masukkan nomor film pilihan : "))
        if film_pilihan==1:
            harga = 50000
            break
        elif film_pilihan==2:
            harga = 50000
            break
        elif film_pilihan==3:
            harga = 50000
            break
        elif film_pilihan==4:
            harga = 50000
            break
        elif film_pilihan==5:
            harga = 50000
            break
        else :
            print("=====Film tidak tersedia, silahkan pilih film lainnya=====")

    jumlah_pembelian = int(input("Masukkan Jumlah Pembelian : "))
    bayar1 = jumlah_pembelian * harga
    jawab = input("Apakah anda ingin membeli paket makanan dan minuman? [y/t] : ")

    if jawab !='y':
        subtotal = bayar1
        list_total_bayar.append([subtotal])

    else:
        print("================================")
        print("             MINUMAN            ")
        print("================================")
        print("Minuman Pilihan : ")
        print("1. Coca Cola ")
        print("2. Lemon Tea")
        print("3. Orange Juice")
        print("4. Coffe")
        print("================================")

        while(True):
            minuman_pilihan = int(input("Masukkan nomor minuman yang anda inginkan : "))

            if minuman_pilihan==1:
                harga : 10000
                break
            elif minuman_pilihan==2:
                harga : 15000
                break
            elif minuman_pilihan==3:
                harga : 15000
                break
            elif minuman_pilihan==4:
                harga : 15000
                break
            else :
                print("=====Minuman Tidak Tersedia, Silahkan Pilih Minuman Lainnya!!=====")

        jumlah2_pembelian = int(input("Masukkan Jumlah Pembelian : "))
        bayar2 = jumlah2_pembelian * harga

        print("================================")
        print("             MAKANAN            ")
        print("================================")
        print("Makanan Pilihan : ")
        print("1. Beef Burger ")
        print("2. Cheese Beef Burger")
        print("3. French Fries")
        print("4. Spaghetti")
        print("5. Popcorn")
        print("================================")

        while(True):
            makanan_pilihan = int(input("Masukkan nomor makanan yang anda inginkan : "))

            if makanan_pilihan==1:
                harga = 25000
                break
            elif makanan_pilihan==2:
                harga = 30000
                break
            elif makanan_pilihan==3:
                harga = 30000
                break
            elif makanan_pilihan==4:
                harga = 30000
                break
            elif makanan_pilihan==5:
                harga = 30000
                break
            else :
                print("=====Makanan Tidak Tersedia, Silahkan Pilih Makanan Lainnya!!=====")

        jumlah3_pembelian = int(input("Masukkan jumlah Pembelian : "))
        bayar3 = jumlah3_pembelian * harga

        subtotal = bayar1 + bayar2 + bayar3
        list_total_bayar.append([subtotal])
        main()

#function
def pembayaran() :
    print()
    print("           - PESANAN -")
    if len(list_total_bayar) == 0:
        print()
        print("\tBELUM ADA PEMESANAN")
        print()
        input("Tekan ENTER untuk kembali ke Menu")
    else:
        total_semua = sum(z[0] for z in list_total_bayar)
        print("----------------------------------------------------------------")
        print("Total harga semua pesanan Anda adalah : Rp.", round(total_semua))
        print("----------------------------------------------------------------")
        print()
        input("Tekan ENTER untuk kembali ke Menu")

#function halaman utama
def main() :
    while True :
        print()
        print("====================================================================")
        print("|                           BIOSKOP JAYA                           |")
        print("|               Aplikasi Pemesanan Tiket Bioskop                   |")
        print("--------------------------------------------------------------------")
        print()
        print("\t[1] Pemesanan\n\t[2] Pembayaran\n\n\t[0] Keluar Aplikasi")
        print()
        pilih1 = input("Silihkan masukkan pilihan Anda : ")
        if pilih1 == "1" :
            pemesanan()
        elif pilih1 == "2" :
            pembayaran()
        elif pilih1 == "0" :
            print("--------------------------------------------------------------------")
            print("                             Terimahkasih                           ")
            print("--------------------------------------------------------------------")
            return True
        else : 
            print()
            print("Input Tidak Dikenal")
            input("Tekan ENTER untuk kembali ke Menu")

#List
list_total_bayar = []

#awal program  
print("==================================================")         
print("          Selamat Datang di Bioskop Jaya")
print("      Kenyamanan Anda Adalah Prioritas Kami")
print("==================================================")
print()
nama = input ("Masukkan Nama Pelanggan : ")
main()