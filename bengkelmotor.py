lg="y"
while lg=="y":
    
   kode=['a','b','c','d','e']
   merk=['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L',]
   harga=[53000,50000,54000,45000,46000]
   print(">>bengkel motor UD milik Bu Sung Hin<<")
   print(">>list harga oli<<")
   print(">>a. Duration SW20 1L = Rp 53.000 ")
   print(">>b. Castrol Magnatec 1L = Rp 50.000")
   print(">>c. Federal Supreme XX 1L = Rp 54.000")
   print(">>d. Yamalube 1L = Rp 45.000")
   print(">>e. Shell 1L = Rp 46.000")
   print("          ")
   
   pilihan = input(">>masukan kode oli yang mau dibeli = ")
   jumlah = int(input(">>jumlah oli = "))
   if pilihan=="a":
       idx = 0
   elif pilihan=="b":
       idx = 1
   elif pilihan=="c":
       idx = 2
   elif pilihan=="d":
       idx = 3
   elif pilihan=="e":
       idx = 4
   else:
       idx = 0

   print("        ")
   print (">>merk       = "+merk[idx])
   print (">>harga      = "+"Rp "+str(harga[idx]))
   print (">>jumlah oli = "+str(jumlah))
   print("   ")
   
   total=jumlah*harga[idx]
   ppn=total*0.01
   bayar=total+ppn
   
   print("--------------------------------------")
   print(">>total semua oli    = Rp"+str(total))
   print(">>pajak ppn 1%       = Rp"+str(ppn))
   print(">>yang harus dibayar = Rp"+str(bayar))
   print("--------------------------------------")
   
   if bayar>=200000:
    diskon=bayar*0.05
    hargadiskon=bayar-diskon
    print(">>diskon 5%")
    print(">>total bayar = Rp"+str(hargadiskon))
   print("--------------------------------------")
 
   lg=input("beli lagi? y/t. ")
   if lg=="t":
       break