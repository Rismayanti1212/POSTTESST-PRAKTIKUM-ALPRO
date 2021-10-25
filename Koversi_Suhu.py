# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:10:55 2021

@author: Chimaa
"""

pilihan = "ya"
while pilihan == "ya":
    print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
><><><><><><>      KONVERSI SUHU      <><><><><><><
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
              a. Fahrenheit ke Celius
              b. Kelvin ke Celcius
              c. Reamur ke Celcius
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
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
    print("=-=-=-=-=-=-=-= Konversi suhu", jenis_suhu, "ke", konversi_suhu, "=-=-=-=-=-=-=-=")
    print(suhu, jenis_suhu, "=" , float(hasil), konversi_suhu)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    pilihan = input("Apakah ingin menghitung ulang? ya atau tidak : ")
print ("Terima Kasih")
#math.ceil(value)
#math.floor(value)
#import math


    
        
        
