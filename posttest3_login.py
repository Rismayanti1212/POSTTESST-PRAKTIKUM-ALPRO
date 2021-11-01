import sys
fixed_account = [{"Username":"chimaa", "Password":"subhanallah"}]
print("---------------------------------------------------")
print("            WELCOME TO APP CHIM's CAFE ")
print("___________________________________________________")
print("""                    1. Buat akun
                    2. Login
                    3. Keluar
___________________________________________________""")
menu = int(input("Silahkan Masukkan Menu  : "))
pilihan = 'y'
while pilihan == 'y' :
    if menu == 1 :
        new_user = {}
        new_user["Username"] = input("Silahkan isi Username   : ")
        new_user["Password"] = input("Silahkan Isi Password   : ")
        fixed_account.append(new_user)
        print()
        print("   Akun Anda Telah Terdaftar Sebagai Member Kami   ")
        print("___________________________________________________")
    elif menu == 2:
        a = 1
        while a <= 3 :
            username = input("Username                : ")
            password = input("Password                : ")
            current_user = next((new_user for new_user in fixed_account if username == new_user
                    ["Username"] and password == new_user["Password"]),False)
            if current_user:
                print()
                print("                SELAMAT DATANG", username,  "^.^" )
                print("                     TERIMA KASIH            ")
                break
            else:
                print()
                print("               Username atau Password Salah                 ")
                print("Batas coba login adalah 3, Anda Sudah Mencoba", a, "Kali")
            a += 1
            print("                      ANDA GAGAL LOGIN            ")
        print("___________________________________________________")
    elif menu == 3 :
        print()
        print("                     TERIMA KASIH            ")
        print("___________________________________________________")
        sys.exit()
    else:
        print("Kode tidak terbaca")
    menu = int(input("Silahkan Masukkan Menu : "))
print()
print("                     TERIMA KASIH            ")
