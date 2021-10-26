pilihan = "ya"
while pilihan == "ya":
    print("""
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
                    KONVERSI SUHU      
___________________________________________________            
         
              1. Fahrenheit ke Celsius
              2. Kelvin ke Celsius
              3. Reamur ke Celsius
___________________________________________________
    """)
    pilih = str(input("Pilih Konversi Suhu? (Misal : 1, 2, dan 3) : "))
    if pilih == "1" :
        suhu = int(input("Masukkan Suhu Fahrenheit : "))
        hasil =((suhu - 32) * 5 / 9)
        jenis_suhu = "F"
        konversi_suhu = "°C"    
    elif pilih == "2" :
        suhu = int(input("Masukkan Suhu Kelvin : "))
        hasil = (suhu - 273.15)        
        jenis_suhu = "K"
        konversi_suhu = "°C"
    elif pilih == "3" :
        suhu = int(input("Masukkan Suhu Reamur : "))
        hasil = ((5 / 4 * suhu))
        jenis_suhu = "R"
        konversi_suhu = "°C"
    else :
        print("Inputan Anda Tidak Tersedia!")
    print()
    print("_ _ _ _ _ _ _ _ Konversi Suhu", jenis_suhu, "ke", konversi_suhu, "_ _ _ _ _ _ _ ")
    print()
    print(suhu, jenis_suhu, "=" , float(hasil), konversi_suhu)
    print("___________________________________________________")
    pilihan = input("Apakah ingin menghitung ulang? ya atau tidak : ")
print ("___________________________________________________")
print ()
print ("           Terima Kasih Telah Mengkonversi!!            ")
