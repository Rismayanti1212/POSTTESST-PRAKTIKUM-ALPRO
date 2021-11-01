import datetime
#MENU
x = datetime.datetime.now()
print("___________________________________________________")
print("                    CHIM's CAFE                    ")
print("                   Jln. My Story                   ")
print("           ", (x),                            )
print("___________________________________________________")
print("""FOOD MENU
1. Chicken Wings                 RP. 25.000
2. Pasta Carbonaro               RP. 35.000
3. Oregano French Fries          RP. 20.000
4. Spicy Tortilla Chicken Roll   RP. 35.000
5. Spicy Fried Beancurd          RP. 30.000
6. Beef Steak                    RP. 45.000
7. Omlet                         RP. 15.000
8. Fettucini                     RP. 27.000
9. Chicken Sup                   RP. 20.000
10. Beef Burger                  RP. 25.000    
                    DRINKS MENU
                    1. Latte           RP. 25.000
                    2. Macchiato       RP. 35.000
                    3. Ice Blend       RP. 20.000
                    4. Ice Drinks      RP. 35.000
                    5. Milk Shake      RP. 30.000
                    6. Americano       RP. 30.000
                    7. Flavoured Tea   RP. 25.000
                    8. Hot Chocolate   RP. 30.000
                    9. Mocktail        RP. 40.000
                    10. Mojito         RP. 20.000

*perhatikan kode menu jika ingin memesan F/D""")
print("___________________________________________________")

#List of Dictionary Menu

menu_makanan = [
  {"no_f" : "1", "food" : "Chicken Wings", "food_price" : 25000},
  {"no_f" : "2", "food" : "Pasta Carbonara", "food_price" :35000},
  {"no_f" : "3", "food" : "Oregano French Fries", "food_price" : 20000},
  {"no_f" : "4", "food" : "Spicy Tortilla Chicken Roll", "food_price" : 35000},
  {"no_f" : "5", "food" : "Spicy Fried Beancurd", "food_price" : 30000},
  {"no_f" : "6", "food" : "Beef Steak", "food_price" : 45000},
  {"no_f" : "7", "food" : "Omlet ", "food_price" : 15000},
  {"no_f" : "8", "food" : "Fettucini", "food_price" : 27000},
  {"no_f" : "9", "food" : "Chicken Sup", "food_price" : 20000},
  {"no_f" : "10", "food" : "Beef Burger", "food_price" : 25000},
]
menu_minuman = [
  {"no_d" : "1", "drink" : "Latte", "drink_price" : 30000},
  {"no_d" : "2", "drink" : "macchiato", "drink_price" :30000},
  {"no_d" : "3", "drink" : "Ice Blend", "drink_price" : 20000},
  {"no_d" : "4", "drink" : "Ice Drinks", "drink_price" : 20000},
  {"no_d" : "5", "drink" : "Milk Shake", "drink_price" : 25000},
  {"no_d" : "6", "drink" : "Americano", "drink_price" : 30000},
  {"no_d" : "7", "drink" : "Falvoured Tea", "drink_price" : 25000},
  {"no_d" : "8", "drink" : "Hot Chocolate", "drink_price" : 30000},
  {"no_d" : "9", "drink" : "Mocktail", "drink_price" : 40000},
  {"no_d" : "10", "drink" : "Mojito", "drink_price" : 20000},
]
print("______________________WELCOME______________________")

#Proses 

list_ordered_makanan = []
list_ordered_minuman = []
greet1 = str(input("Hello, Apakah Anda Ingin Memesan Sesuatu? "))

#Jika Belum Ingin Memesan

if greet1 == 'n' or greet1 == 'N' :
    greet2 = input("Apakah Ingin Menunggu Seseorang? ")
    if greet2 :
        print("""
              a. 15 menit
              b. 25. menit
              c. 45 menit""")
        minute = [{ "kode" : "a", "min" : "15 Menit"},
                    {"kode" : "b", "min" : "25 Menit"},
                    {"kode" : "c", "min" : "30 menit"},]
        greet3 = str(input("Baik, Berapa Lama? "))
        if greet3 == 'a' or greet3 == 'b' or greet3 == 'c' :
            print("Baik, Ditunggu")
            waiting = next((sub for sub in minute if sub['kode'] == greet3), None)
            print(f"________Menunggu {waiting['min']} Sebelum Pemesanan________")
        greet1 = str(input("Apakah Anda Sudah Siap Memesan? "))
        
#Jika Ingin Memesan

while greet1 == 'y' or greet1 == 'Y' :
    print("_____________________Pemesanan______________________")
    order = str(input("Apa Yang Ingin Anda Pesan? F/f=Food & D/d=Drink : "))
    if order == 'f' or order == 'F' :
        order_food = input("Silahkan Pilih Menu Makanan Anda : ")
        ordered = next((sub for sub in menu_makanan if sub['no_f'] == order_food), None)
        total_food = int(input(f"Berapa porsi {ordered['food']}, yang ingin anda pesan? "))
        ordered['total_food'] = int(total_food)
        ordered['payment'] = ordered['total_food'] * ordered['food_price']
        list_ordered_makanan.append(ordered)
        greet1 = str(input("Apa Ada Tambahan Lagi? "))
    elif order == 'd' or order == 'D' :
        order_drink = input("Silahkan Pilih Menu Minuman Anda : ")
        ordered = next((sub for sub in menu_minuman if sub['no_d'] == order_drink), None)
        total_drink = int(input(f"Berapa porsi {ordered['drink']}, yang ingin anda pesan? "))
        ordered['total_drink'] = int(total_drink)
        ordered['payment'] = ordered['total_drink'] * ordered['drink_price']
        list_ordered_minuman.append(ordered)
        greet1 = str(input("Apa Ada Tambahan Lagi? "))      
    else :
        print("Mohon Maaf, Menu Tersebut Tidak Ada Dalam Daftar")    
print("___________________________________________________")

#Proses Penjumlahan Pesanan

total_food = 0
total_drinks = 0
for list_order in list_ordered_makanan :
    total_food += list_order['total_food']
for list_order in list_ordered_minuman :
    total_drinks += list_order['total_drink']
    
#Potongan Harga Yang Di Dapatkan

if total_food >= 2 :
    food_discount = 5
else :
    food_discount = 0
if total_drinks >= 3 :
    drink_discount = 10
else :
    drink_discount = 0
menu_discount = food_discount + drink_discount
if datetime.datetime.today().weekday() < 5 :
    day_discount = 10
else : 
    day_discount = 5
payment = str(input("Apakah Ingin Melakukan Pembayaran Melalu E-Money? "))
if payment == 'y' or payment == 'Y' :
    emoney_discount = 5
else :
    emoney_discount = 0
    
#Proses Perhitungan Keseluruhan

print("___________________________________________________")
print()
print("                     PEMBAYARAN                 ")
print("                     ----------                 ")
for list_order in list_ordered_makanan :
    print(list_order['food'])
    print(list_order['food_price'], "x", list_order['total_food'], "= RP.", list_order['payment'])
for list_order in list_ordered_minuman :
    print(f"{list_order['drink']}")
    print(f"{list_order['drink_price']} x {list_order['total_drink']} = RP. {(list_order['payment'])}")
print("---------------------------------------------------+")
total_discount = menu_discount + day_discount + emoney_discount
list_all_ordered = list_ordered_makanan + list_ordered_minuman
total_price = sum(list_order['payment'] for list_order in list_all_ordered)
cut_discount = total_price * total_discount / 100
total_payment = total_price - cut_discount
print("                                         RP.", total_price)
print("----------------------------------------------------")
print("Diskon Makanan :  ",  food_discount, "%")
print("Diskon Minuman :  ", drink_discount, "%")
print("Diskon Hari    :  ",   day_discount, "%")
print("Diskon E_Money :  ",emoney_discount, "%")
print("---------------------------------------------------+")
print("            RP.", total_price, "Diskon Sebesar", total_discount, "%")
print("---------------------------------------------------=")
print("                                Total : RP.",  total_payment)
print("____________________________________________________")
