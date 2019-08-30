def show_menu():  
    print("- - - - - -  MENU - - - - - -")
    print("[1] Cek Saldo")
    print("[2] Top Up Saldo")
    print("[3] Pembelian")

    menu = input("PILIH MENU> ")
    print(menu)

    if  menu == 1 :
        print("Cek saldo")
        print("Rp. 1.500.000,00")
    elif menu == 2 :
        print("Top Up Saldo")
        q = int(input("Input : "))
        print(q)
        p = 1500000
        saldo = q + p
        print("saldo: ",saldo)
    elif menu == 3 :
        print("Pembelian")
        x = int(input("Check Out: "))
        print(x)
        saldo = 1500000
        saldo_akhir = saldo - x
        print("saldo_akhir: ",saldo_akhir)
        if x<saldo_akhir :
            print("Transaksi berhasil!")
        if x>saldo_akhir :
            print("Saldo anda tidak cukup!")
    else:
        print("WRONG")


    menu_lainnya = input("Transaksi Lainnya ? (Ketik Ya/Tidak) : ")
    print(menu_lainnya)

    if menu_lainnya == "Ya" :
        print("- - - - - -  MENU - - - - - -")
        print("[1] Cek Saldo")
        print("[2] Top Up Saldo")
        print("[3] Pembelian")

        menu = input("PILIH MENU> ")
    else:
        print("Terima Kasih")

    if  menu == 1 :
        print("Cek saldo")
        r = saldo_akhir
        print(r)
    elif menu == 2 :
        print("Top Up Saldo")
        q = int(input("Input : "))
        print(q)
        p = 1500000
        saldo = q + p
        print("saldo: ", saldo)
    elif menu == 3 :
        print("Pembelian")
        x = int(input("Check Out: "))
        print(x)
        saldo_akhir = saldo - x
        print("saldo_akhir: ", saldo_akhir)
        if x<saldo_akhir :
            print("Transaksi berhasil!")
        if x>saldo_akhir :
            print("Saldo anda tidak cukup!")
    else:
        print("WRONG")

    menu_lainnya = input("Transaksi Lainnya ? (Ketik Ya/Tidak) : ")
    print(menu_lainnya)

    if menu_lainnya == "Ya" :
        print("- - - - - -  MENU - - - - - -")
        print("[1] Cek Saldo")
        print("[2] Top Up Saldo")
        print("[3] Pembelian")

        menu = input("PILIH MENU> ")
    else:
        print("Terima Kasih")

    if  menu == 1 :
        print("Cek Saldo")
        r = saldo_akhir
        print(r)
    elif menu == 2 :
        print("Top Up Saldo")
        q = int(input("Input : "))
        print(q)
        p = 1500000
        saldo = q + p
        print("Saldo: ", saldo)
    elif menu == 3 :
        print("Pembelian")
        x = int(input("Check Out: "))
        print(x)
        saldo_akhir = saldo - x
        print("saldo_akhir: ", saldo_akhir)
        if x<saldo_akhir :
            print("Transaksi berhasil!")
        if x>saldo_akhir :
            print("Saldo anda tidak cukup!")

    else:
        print("WRONG")

    menu_lainnya = input("Transaksi Lainnya ? (Ketik Ya/Tidak) : ")
    print(menu_lainnya)

    if menu_lainnya == "Ya" :
        print("- - - - - -  MENU - - - - - -")
        print("[1] Cek Saldo")
        print("[2] Top Up Saldo")
        print("[3] Pembelian")

        menu = input("PILIH MENU> ")
    else:
        print("Terima Kasih")
show_menu()