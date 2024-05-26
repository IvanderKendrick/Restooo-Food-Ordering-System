import sys
import os
import uuid
import WConio2 as WConio

clear = lambda: os.system('cls')

foods = []
myCart = []

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

foods.append(Food('Rice', 10000))
foods.append(Food('Kentucky Fried Chicken', 18000))
foods.append(Food('Meat Lover Pizza', 66000))
foods.append(Food('Big Mac', 36000))
foods.append(Food('Curry Ramen', 25000))
foods.append(Food('Onigiri', 18000))
foods.append(Food('Takoyaki', 18000))
foods.append(Food('Rendang', 20000))
foods.append(Food('Otak-otak', 18000))
foods.append(Food('Pempek', 18000))
foods.append(Food('Pudding', 16000))
foods.append(Food('Ice Cream (Vanilla)', 12000))
foods.append(Food('Pancake', 18000))

def dashboard():
    WConio.textcolor(WConio.BLUE)
    print('|>|' * 3 + "Welcome to Restooo ~~~" + '|>|' * 3)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("="*40)
    WConio.textcolor(WConio.YELLOW)
    print(" " * 3 + "Please select the main menu number")
    WConio.textcolor(WConio.LIGHTGRAY)
    print()
    WConio.textcolor(WConio.LIGHTGREEN)
    print('1. Menu makanan')
    print('2. Keranjang saya')
    print('3. Hapus isi keranjang')
    print('4. Total yang perlu dibayar')
    print('5. Pembayaran')
    WConio.textcolor(WConio.LIGHTMAGENTA)
    print('0. Keluar dari sistem')
    WConio.textcolor(WConio.LIGHTGRAY)

def showMenu():
    WConio.textcolor(WConio.LIGHTGREEN)
    print('='*25,'MENU','='*25)
    WConio.textcolor(WConio.LIGHTGRAY)
    a = 0
    i = 0
    while i < 18:
        if i == 0:
            print()
            WConio.textcolor(WConio.LIGHTCYAN)
            print("Carbohydrate")
            WConio.textcolor(WConio.LIGHTGRAY)
        elif i == 2:
            print()
            WConio.textcolor(WConio.LIGHTCYAN)
            print("Western Foods")
            WConio.textcolor(WConio.LIGHTGRAY)
        elif i == 6:
            print()
            WConio.textcolor(WConio.LIGHTCYAN)
            print("Japanese Foods")
            WConio.textcolor(WConio.LIGHTGRAY)
        elif i == 10:
            print()
            WConio.textcolor(WConio.LIGHTCYAN)
            print("Indonesian Foods")
            WConio.textcolor(WConio.LIGHTGRAY)
        elif i == 14:
            print()
            WConio.textcolor(WConio.LIGHTCYAN)
            print("Dessert")
            WConio.textcolor(WConio.LIGHTGRAY)
        else:
            print(str(a+1)  + ". " +foods[a].name, "." * (50 - len(foods[a].name) - 9 - (len(str(a+1)))), "Rp", str(foods[a].price))
            a += 1
        i += 1
    print()
    WConio.textcolor(WConio.LIGHTGREEN)
    print("="*56)
    WConio.textcolor(WConio.LIGHTGRAY)

def addToCart(id,qty):
    myCart.append(Cart(foods[id -1].name, foods[id -1].price, qty))

def showMyCart():
    WConio.textcolor(WConio.LIGHTGREEN)
    print('='*20,"KERANJANG SAYA",'='*20)
    WConio.textcolor(WConio.YELLOW)
    print("Keranjang Saya : ")
    WConio.textcolor(WConio.LIGHTGRAY)
    print()
    for i in range(len(myCart)):
        print(str(i + 1)  + ". " +myCart[i].name + " " + str(myCart[i].qty) + "pcs")
    print()

def pesanError():
    clear()
    showMenu()

def removeFromMyCart(id):
    if myCart:
        if id-1 < len(myCart):
            print('Berhasil menghapus ' + myCart[id-1].name, str(myCart[id-1].qty) + "pcs")
            myCart.pop(id - 1)
        else:
            print("Item tidak ditemukan di keranjang")
    else:
        print("Keranjang kosong")

def print_total():
    total = 0
    for i in range(len(myCart)):
        print(str(i + 1)  + ". " +myCart[i].name + " " + str(myCart[i].qty) + "pcs " + " = " + str(myCart[i].price * myCart[i].qty))
        total += myCart[i].price * myCart[i].qty
    print()
    WConio.textcolor(WConio.LIGHTMAGENTA)
    print("TOTAL = " + str(total))
    WConio.textcolor(WConio.LIGHTGRAY)

def return_total():
    total = 0
    for i in range(len(myCart)):
        total += myCart[i].price * myCart[i].qty
    return total

def struk_tunai(**kwargs):
    WConio.textcolor(WConio.BLUE)
    print('|>|' * 3 + "Welcome to Restooo ~~~" + '|>|' * 3)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("="*40)
    WConio.textcolor(WConio.YELLOW)
    print("Pemesanan atas nama", kwargs["name"])
    WConio.textcolor(WConio.LIGHTGRAY)
    print()
    print_total()
    WConio.textcolor(WConio.LIGHTGREEN)
    print("="*40)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("Cash : Rp" + str(kwargs["nominal"]))
    print("Change : Rp" + str(kwargs["change"]))
    WConio.textcolor(WConio.LIGHTGREEN)
    print("="*40)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("-" * 13, "Terima Kasih", "-" * 13)
    print("-" * 9, "Atas Kunjungan Anda!", "-" * 9)

def struk_nontunai(total, name):
    WConio.textcolor(WConio.BLUE)
    print('|>|' * 3 + "Welcome to Restooo ~~~" + '|>|' * 3)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("="*40)
    WConio.textcolor(WConio.YELLOW)
    print("Pemesanan atas nama", name)
    WConio.textcolor(WConio.LIGHTGRAY)
    print()
    print_total()
    WConio.textcolor(WConio.LIGHTGREEN)
    print("="*40)
    WConio.textcolor(WConio.LIGHTGRAY)
    print()
    print(f"Saldo anda telah terpotong sebesar {str(total)}")
    print()
    WConio.textcolor(WConio.LIGHTGREEN)
    print("="*40)
    WConio.textcolor(WConio.LIGHTGRAY)
    print("-" * 13, "Terima Kasih", "-" * 13)
    print("-" * 9, "Atas Kunjungan Anda!", "-" * 9)

def main_function():
    clear()
    dashboard()
    choose()

def choose():
    print()
    inputUser = input('Silakan pilih nomor menu utama : ')
    if inputUser == '1':
        while True:
            clear()
            showMenu()
            addCart = input("Ingin memasukkan item ke keranjang (Ya/Tidak) ? ")
            while addCart != "Ya" and addCart != "Tidak" and addCart != "ya" and addCart != "tidak":
                WConio.textcolor(WConio.LIGHTRED)
                print("Mohon masukkan perintah dengan benar (Ya/Tidak) !")
                stopClear = input("Silakan tekan enter untuk kembali memasukkkan perintah . . .")
                WConio.textcolor(WConio.LIGHTGRAY)
                pesanError()

                addCart = input("Ingin memasukkan item ke keranjang (Ya/Tidak) ? ")

            if addCart == "Ya" or addCart == 'ya':
                while True:
                    try:
                        clear()
                        showMenu()
                        idFood = int(input('Silakan pilih nomor menu makanan yang diinginkan : '))
                        if idFood < 14 and idFood > 0:
                            while True:
                                try:
                                    qty = int(input("Berapa banyak yang anda inginkan (min 1 - max 50) : "))
                                    if qty >= 1 and qty <= 50:
                                        print("="*56)
                                        addToCart(idFood,qty)
                                        WConio.textcolor(WConio.LIGHTMAGENTA)
                                        stopClear = input("Terima Kasih, sistem telah berhasil menambahkan pesanan anda ke keranjang . . .")
                                        WConio.textcolor(WConio.LIGHTGRAY)
                                        clear()
                                        break

                                    else:
                                        WConio.textcolor(WConio.LIGHTRED)
                                        print("Mohon masukkan jumlah dengan benar (minimal 1, maksimal 50) !")
                                        WConio.textcolor(WConio.LIGHTGRAY)
                                        print()

                                except ValueError:
                                    WConio.textcolor(WConio.LIGHTRED)
                                    print("Mohon masukkan jumlah dengan benar berupa angka/bilangan bulat/int (min 1, max 50) !")
                                    WConio.textcolor(WConio.LIGHTGRAY)
                                    print()

                        else:
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Mohon masukkan nomor menu makanan yang sesuai (antara 1-13) !")
                            WConio.textcolor(WConio.RED)
                            stopClear = input("Silakan tekan enter untuk kembali memasukkkan perintah . . .")
                            WConio.textcolor(WConio.LIGHTGRAY)

                    except ValueError:
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Mohon masukkan nomor menu berupa angka/bilangan bulat/int !")
                        WConio.textcolor(WConio.RED)
                        stopClear = input("Silakan tekan enter untuk kembali memasukkkan perintah . . .")
                        WConio.textcolor(WConio.LIGHTGRAY)
                        continue

                    break

            elif addCart == "Tidak" or addCart == 'tidak':
                break
        main_function()

    elif inputUser == '2':
        clear()
        showMyCart()
        WConio.textcolor(WConio.LIGHTGREEN)
        print("="*56)
        WConio.textcolor(WConio.LIGHTGRAY)
        dashboard()
        choose()
    elif inputUser == '3':
        if myCart:
            while True:
                try:
                    clear()
                    WConio.textcolor(WConio.LIGHTGREEN)
                    print("Menghapus item dalam keranjang :")
                    WConio.textcolor(WConio.YELLOW)
                    print("="*56)
                    WConio.textcolor(WConio.LIGHTGRAY)
                    print_total()
                    print()
                    WConio.textcolor(WConio.LIGHTGREEN)
                    print("0. Kembali ke menu utama")
                    WConio.textcolor(WConio.YELLOW)
                    print("="*56)
                    WConio.textcolor(WConio.LIGHTGRAY)
                    id = int(input('Pilih nomor keranjang yang ingin dihapus : '))
                    if id == 0:
                        main_function()
                    elif id < 0:
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Mohon untuk memasukkan nilai/angka positif !")
                        WConio.textcolor(WConio.LIGHTGRAY)
                        input()
                        continue
                    else:
                        WConio.textcolor(WConio.YELLOW)
                        print("="*56)
                        WConio.textcolor(WConio.LIGHTGRAY)
                        removeFromMyCart(id)
                        WConio.textcolor(WConio.YELLOW)
                        print("="*56)
                        WConio.textcolor(WConio.LIGHTGRAY)
                        input()
                        main_function()
                except ValueError:
                    WConio.textcolor(WConio.LIGHTRED)
                    print("Mohon masukkan nomor keranjang berupa int")
                    WConio.textcolor(WConio.LIGHTGRAY)
                    stopClear = input()
        else:
            WConio.textcolor(WConio.LIGHTRED)
            print("Keranjang anda kosong :( , anda belum memasukkan apapun ke keranjang")
            input("Mohon untuk memesan terlebih dahulu di menu utama no.1 . . .")
            WConio.textcolor(WConio.LIGHTGRAY)
            main_function()
    elif inputUser == '4':
        clear()
        WConio.textcolor(WConio.YELLOW)
        print("="*56)
        WConio.textcolor(WConio.LIGHTGRAY)
        print()
        print_total()
        print()
        WConio.textcolor(WConio.YELLOW)
        print("="*56)
        WConio.textcolor(WConio.LIGHTGRAY)
        dashboard()
        choose()
    elif inputUser == '5':
        if myCart:
            clear()
            WConio.textcolor(WConio.YELLOW)
            name = input('Nama Lengkap Anda : ')
            WConio.textcolor(WConio.LIGHTGRAY)
            WConio.textcolor(WConio.LIGHTGREEN)
            print("="*56)
            WConio.textcolor(WConio.LIGHTGRAY)
            print("Kode pembayaran : ")
            WConio.textcolor(WConio.BROWN)
            print(str(uuid.uuid4()))
            WConio.textcolor(WConio.LIGHTGREEN)
            print("="*56)
            WConio.textcolor(WConio.LIGHTGRAY)

            pembayaran = input("Apakah anda ingin melakukan pembayaran tunai atau nontunai (T/N) ? ")
            while pembayaran != 'T' and pembayaran != 'N':
                print()
                WConio.textcolor(WConio.LIGHTRED)
                print("Mohon memasukkan perintah dengan benar T ( pembayaran tunai ) atau N ( pembayaran non tunai ) ")
                WConio.textcolor(WConio.LIGHTGRAY)
                pembayaran = input("Apakah anda ingin melakukan pembayaran tunai atau nontunai (T/N) ? ")

            if pembayaran == 'T':
                while True:
                    try:
                        print()
                        total = return_total()
                        print_total()
                        nominal = int(input("Mohon masukkan nominal uang anda untuk melakukan pembayaran : "))
                        if total > nominal:
                            WConio.textcolor(WConio.LIGHTRED)
                            print("Mohon maaf, uang anda kurang untuk melakukan pembayaran")
                            print("Mohon untuk memasukkan nominal minimal : Rp" + str(total))
                            WConio.textcolor(WConio.LIGHTGRAY)
                        else:
                            break
                    except ValueError:
                        print()
                        WConio.textcolor(WConio.LIGHTRED)
                        print("Mohon masukkan angka berupa bilangan bulat / int dengan nominal ribuan ( contoh : 50000 )")
                        WConio.textcolor(WConio.LIGHTGRAY)

                change = nominal - total
                if change == 0:
                    WConio.textcolor(WConio.LIGHTCYAN)
                    print("Uang anda pas, Terima Kasih telah melakukan pembayaran atas pesanan anda, semoga anda berbahagia selalu")
                    WConio.textcolor(WConio.LIGHTGRAY)
                    input()
                    clear()
                    struk_tunai(nominal = nominal, change = change, name = name)
                else:
                    print("Uang anda sebesar : Rp" + str(nominal))
                    print("Change : Rp" + str(change))
                    WConio.textcolor(WConio.LIGHTCYAN)
                    print("Terima Kasih telah melakukan pembayaran atas pesanan anda, semoga anda berbahagia selalu")
                    WConio.textcolor(WConio.LIGHTGRAY)
                    input()
                    clear()
                    struk_tunai(nominal = nominal, change = change, name = name)

            elif pembayaran == 'N':
                total = return_total()
                print("Total yang harus dibayarkan : Rp" + str(total))
                WConio.textcolor(WConio.LIGHTMAGENTA)
                print("Terima Kasih telah melakukan pembayaran atas pesanan anda, semoga anda berbahagia selalu")
                WConio.textcolor(WConio.LIGHTGRAY)
                input()
                clear()
                struk_nontunai(total, name)
            input()
            sys.exit()

        else:
            WConio.textcolor(WConio.LIGHTRED)
            print("Keranjang anda kosong :( , anda belum memasukkan apapun ke keranjang")
            input("Mohon untuk memesan terlebih dahulu di menu utama no.1 . . .")
            WConio.textcolor(WConio.LIGHTGRAY)
            main_function()

    elif inputUser == '0':
        sys.exit()
    else:
        print()
        WConio.textcolor(WConio.LIGHTRED)
        print("Mohon masukkan nomor menu dengan benar (0 atau 1-5) . . .")
        input("Tekan enter untuk memasukkan ulang nomor menu . . .")
        WConio.textcolor(WConio.LIGHTGRAY)
        main_function()

main_function()