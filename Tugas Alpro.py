srv = str(input("Masukan service = "))
ipk = str(input("Masukan IPK = "))

if srv == "Telkomsel" and ipk >= "3" and ipk <= "4" :
    print("Selamat Anda mendapatkan Iphone X")
elif srv != "Telkomsel" and ipk >= "3" and ipk <= "4" :
    print("Selamat Anda mendapatkan Samsung J Series")
elif srv == "Telkomsel" and ipk >= "2,5" and ipk <= "3" :
    print("Selamat Anda mendapatkan PS4")
elif srv != "Telkomsel" and ipk >= "2,5" and ipk <= "3" :
    print("Selamat Anda mendapatkan Voucher menginap di Hotel Ibis TSM")
elif srv == "Telkomsel" and ipk >= "2" and ipk <= "2,5" :
    print("Selamat Anda mendapatkan Voucher menginap di Daarut Tauhid")
elif srv != "Telkomsel" and ipk >= "2" and ipk <= "2,5" :
    print("Selamat Anda mendapatkan Voucher klinik psikolog")
else :
    print("Maaf belum beruntung, Terima kasih")