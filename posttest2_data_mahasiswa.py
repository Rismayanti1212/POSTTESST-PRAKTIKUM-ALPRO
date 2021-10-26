pilihan = "ya"
while pilihan == "ya" :
    print("""
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
                    DATA MAHASISWA    
___________________________________________________   
        """)
    print ("           Silahkan Input Data Anda!             ")
    nama = str(input("Isi Nama Anda : "))
    nim = int(input("Isi NIM Anda : "))
    print ("""Program Studi
1. Teknik Industri
3. Teknik Lingkungan
4. Teknik Kimia
5. Teknik Elektro
6. Teknik Geologi
7. Informatika
8. Sistem Informasi
9. Arsitektur
    """)
    daftar_prodi = {
            1 : "Teknik Pertambangan", 
            2 : "Teknik Industri", 
            3 : "Teknik Lingkungan",
            4 : "Teknik Kimia",
            5 : "Teknik Elekro",
            6 : "Teknik Geologi",
            7 : "Informatika",
            8 : "Sistem Informasi",
            9 : "Arsitektur" }
    prodi = int(input("Pilih Prodi Anda berdasarkan daftar di atas : "))
    semester = int(input("Semester Berapa Anda Sekarang : "))
    ip = float(input("Isi Indeks Prestasi Anda : "))
    print ("___________________________________________________")
    print ("                    Data Anda                      ")
    print ("___________________________________________________")
    
    data_mahasiswa = [nama, nim, (daftar_prodi[prodi]), semester, ip]
    
    print("Nama            :", (data_mahasiswa[0]))
    print("NIM             :", (data_mahasiswa[1]))
    print("Program Studi   :", (data_mahasiswa[2]))
    
    if semester >= 1 and semester <= 14 :
        print("Semester        :", (data_mahasiswa[3]))
    else :
        print("Semester        : -")
        
    if ip >= 0 and ip <= 4.0 :
        print("Indeks Prestasi :", (data_mahasiswa[4]))
    else :
        print("Indeks Prestasi : -")
        
    print ("___________________________________________________")
    pilihan = input("Apakah ingin mendata lagi? ya atau tidak : ")
    
print ("___________________________________________________")
print ()
print ("           Terima Kasih Telah Mendata!!            ")
