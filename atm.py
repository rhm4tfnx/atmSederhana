import sys
from time import sleep
from colorama import Fore,Back,Style

green = Fore.GREEN
blue = Fore.BLUE
cyan = Fore.CYAN
red = Fore.RED
tebal = Style.BRIGHT

banner = f'''{green}{tebal}\t\t\t\n Bank Jago bin Bansos
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
def lagu(s):
	for x in s + "\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(0.1)
def cekSaldo():
    global saldo
    print(green,'saldo anda sekarang adalah : ',saldo)

def informasi():
    print(f'''Kau adalah hidup ku lengkapi diriku oh sayang ku kau begitu sempurna
    Nama : Rahmat Hidayat
    TTL : Masih di sini
    No Handphone : 6283136045762
    ''')

    laguu = f'''\n\n\n\n\n
   Kelak kau 'kan menjalani hidupmu sendiri
Melukai kenangan yang telah kita lalui
Yang tersisa hanya aku sendiri di sini
Kau akan terbang jauh menembus awan
Memulai kisah baru tanpa diriku
Seandainya kau tau ku tak ingin kau pergi
Meninggalkanku sendiri bersama bayanganku
Seandainya kau tau aku 'kan selalu cinta
Jangan kau lupakan kenangan kita selama ini
Kelak kau 'kan menjalani hidupmu sendiri
Melukai kenangan yang telah kita lalui
Kau akan terbang jauh menembus awan
Memulai kisah baru tanpa diriku
Seandainya kau tau ku tak ingin kau pergi
Meninggalkanku sendiri bersama bayanganku
Seandainya kau tau aku 'kan selalu cinta
Jangan kau lupakan kenangan kita selama ini
Selama ini
Seandainya kau tau ku tak ingin kau pergi
Oh-oo
Meninggalkanku sendiri bersama bayanganku
Seandainya kau tau aku 'kan selalu cinta
Jangan kau lupakan kenangan kita selama ini
Ha-aa-oo
Selama ini 
    '''

    print(Fore.LIGHTYELLOW_EX,'Sedikit lagu nih hehe \nMau ga? ')
    start = input('siap? [n/y]')
    if start == 'y':
        lagu(laguu)
    elif start == 'n':
        print('yahh :(')
    else:
        exit
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
        print('Input anda salah')

def needpin():
    print(f'''{tebal}{cyan}
    \t Selamat Datang di ATM khusus bang jago
    ''')

    __pin = 117325
    print('pin nya 117325')
    nanya = int(input('Masukkan pin anda : '))
    if nanya == __pin:
        while True:
            mulai()
    else:
        print(red,'Pin yang anda masukkan salah')

while True:
    needpin()
