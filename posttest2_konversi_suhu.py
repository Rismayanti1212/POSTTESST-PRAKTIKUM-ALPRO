# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:10:55 2021

@author: Chimaa
"""

pilihan = "ya"
while pilihan == "ya":
    print("""
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
                     KONVERSI SUHU      
___________________________________________________            
         
              a. Fahrenheit ke Celius
              b. Kelvin ke Celcius
              c. Reamur ke Celcius
___________________________________________________
    """)
    pilih = str(input("Pilih Konversi suhu? (Misal : a, b, dan c) : "))
    if pilih == "a" :
        suhu = int(input("Masukkan suhu Fahrenheit : "))
        hasil =((suhu - 32) * 5 / 9)
        jenis_suhu = "F"
        konversi_suhu = "°C"    
    elif pilih == "b" :
        suhu = int(input("Masukkan suhu Kelvin : "))
        hasil = (suhu - 273)
        jenis_suhu = "K"
        konversi_suhu = "°C"
    elif pilih == "c" :
        suhu = int(input("Masukkan suhu Reamur : "))
        hasil = ((5 / 4 * suhu))
        jenis_suhu = "R"
        konversi_suhu = "°C"
    else :
        print("Inputan tidak sesuai!!")
    print()
    print("_ _ _ _ _ _ _ _ Konversi suhu", jenis_suhu, "ke", konversi_suhu, "_ _ _ _ _ _ _ ")
    print()
    print(suhu, jenis_suhu, "=" , float(hasil), konversi_suhu)
    print("___________________________________________________")
    pilihan = input("Apakah ingin menghitung ulang? ya atau tidak : ")
print ("___________________________________________________")
print ()
print ("           Terima Kasih Telah Mengkonversi!!            ")


    
        
        
