import sys
from time import sleep
from colorama import Fore,Back,Style

green = Fore.GREEN
blue = Fore.BLUE
cyan = Fore.CYAN
red = Fore.RED
tebal = Style.BRIGHT

banner = f'''{cyan}{tebal}\t\t\t\n Bank Jago bin Bansos
1. Tarik Tunai      2. Tambah Saldo
3. Informasi saldo  4. Informasi Pemilik

'''
saldo = 0

def tarik():
    print(red)
    global saldo
    berjalan('''
    100000 >< 200000
    500000 >< 1000000
    ''')
    
    jumlah_tarik = int(input('Masukkan jumlah : '))
    berjalan('Mohon Tunggu')
    print("Transaksi Berhasil")
    saldo -= jumlah_tarik
    print('Saldo anda sekarang adalah :',saldo)

def tambah():
    print(blue)
    global saldo
    jumlah_tambah = int(input('Masukkan jumlah : '))
    berjalan('Mohon Tunggu .......')
    print('Transaksi berhasil')
    saldo += jumlah_tambah
    print('saldo anda sekarang adalah :',saldo)

def berjalan(s):
	for x in s + "\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(0.05)

def cekSaldo():
    global saldo
    print(green,'saldo anda sekarang adalah : ',saldo)

def informasi():
    print(green,'Pemilik nya adalah saya')

try:
    while (True):
        def mulai():
            berjalan(banner)
            pilih = input('Masukkan pilihan anda : ')
            if pilih == '1':
                tarik()
            elif pilih == '2':
                tambah()
            elif pilih == '3':
                cekSaldo()
            elif pilih == '4':
                informasi()
            else:
                print('YAng bener cantik')        

        mulai()
except Exception as er:
    print(er)
