lg="y"
while lg=="y":
    
    kode =['a','b']
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    print("ekspedisi lorena")
    print("kode kota tujuan dari: ")
    print("a. malang -> surabaya ")
    print("b. malang -> bandung ")
    
    pilihan = input(">> Masukkan Kode Tujuan = ")
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 0

    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))
    lg=input("coba lagi ? y/t.  ")
    if lg=="t":
        break 