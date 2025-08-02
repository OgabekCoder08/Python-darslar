# cars = ['toyota','bmw','mercedes benz','audi','chevrolet','kia']
# cars.sort()
# print(cars)

# 2-masala
# sonlar = [10,23,5,67,1,89]
# katta = max(sonlar)
# kichik = min(sonlar)
# print(f"Eng kichik son👉",kichik,"\nEng katta son👉",katta)

# 1-masala
# sonlar = [4 -2, 0, 5,-7, 3]
# musbat_sonlar = []
# for son in sonlar:
#     if son >0:
#         musbat_sonlar.append(son)
# print(musbat_sonlar)
# 1-masala
# son1 = 4
# son2 = -2
# son3 =0
# son4=5
# son5 = -7
# son6 = 3
# print(f"Musbat sonlar",son1,son4,son6)

# 2-masala
# sonlar = [10,23,5,67,1,89]
# katta = max(sonlar)
# kichik = min(sonlar)
# print(f"Eng kichik son👉",kichik,"\nEng katta son👉",katta)

# musbat_sonlar = '4, 5, 3'
# manfi_sonlar = '-2, -7'
# print("musbat sonlar👉",musbat_sonlar,"\nmanfi sonlar👉",manfi_sonlar)
# sonlar =[4 ,0, -2, 5,-7, 3]
# sonlar.sort() 
# print(sonlar)
# 2-topshiriq
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")



# sonlar = []
# for n in range(5):
#     sonlar.append(int(input(f"{n+1}-sonni kiriting: ")))

# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# 3-topshiriq
# n = int(input("Nechta son kiritasiz: "))
# yigindi = 0
# for i in range(n):
#     son = float(input(f"{i+1}-sonni kiriting: "))
#     yigindi += son
#     print(f"\nKiritilgan sonni yig'indisi:{yigindi}")

 # 1-topshiriq
# yosh = int(input("Yoshingizni kiriting:👉\t"))
# if yosh<18:
#     qolgan_yil =18 - yosh
#     print(f"Sizga saytga kirishingizga{qolgan_yil} yil qoldi")
# else:
#     print("Xush kelibsiz")

# 2-topshiriq
# login = input("Login kiriting:👉 ")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi kerak")
# else:
#     print("Loginingiz qabul qilindi")

# 3-topshiriq
# son = int(input("Son kiriting>>> "))
# if son>10 or son<5:
#     print("Bu son 10 dan katta yoki 5 dan kichik")
# else:
#     print("Bu son 5 va 10 orasida")

# 1- topshiriq

# yosh = int(input("Yoshingiz nechida:>>>"))
# if yosh >=18:
#     print("Kirishingiz mumkin xush kelibsiz🎉")
# else:
#     print("Uzur kirishingiz mumkin emas❌")

# 2- topshiriq

# kun = input("Bugun qanday kun?>>> ").strip()
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#    print(f"Bugun {kun.title()}, dam olish kuni.") 
# elif kun.lower() == 'dushanba' or kun.lower() == 'seshanba' or kun.lower() == 'chorshanba' or kun.lower() == 'payshanba' or kun.lower() == "juma":
#     print(f"Bugun {kun.title()}, ish kuni!") 
# else:
#    print('Siz xafta kunini xato kiritingiz!❌')

# 3 - topshiriq

# menu = ['osh','somsa','shashlik','qazon kabob']
# buyurtmalar = ['somsa','shashlik','qazon kabob']
# if buyurtmalar:
#    for taom in buyurtmalar:
#     print(f"minuda {taom} bor")
# else:
#     print("savatchangiz bo'sh")



# ism = input("Ismingiz nima:\t")
# yosh = int(input("Nechi yoshdasiz:>>>"))
# if yosh >=18 and ism.lower()!= "Ali":
#    print("Salom Ali sizga saytga kirishga ruhsat bor🎉")
# else:
#     print("Uzur kirishingiz mumkin emas❌")

# menu = ["Lagmon,Osh,Shashlik,Somsa,Choy"]
# buyurtmalar =[]
# narx = 0
# x = int(input("Hurmatli mijoz nechta taom buyurasiz:\t"))
# for i in range(0,x):
#     buyurtma = input(f"{i+1} buyurtmani kiriting: ")
#     buyurtmalar.append(buyurtma)
# if buyurtmalar:
#     for taom in menu:
#         print(f"Sizning{taom.title()} nomli buyurtmangiz qabul qilindi")
#     else:
#         print(f"Sizning{taom.title()} nomli buyurtmangiz menuda yo'q")
# else:
#     print("Savatchangiz bo'sh")
# for a in buyurtmalar:
#     if a == "Lag'mon":
#      narx +=25000
#     if a == "Osh":
#      narx +=20000  
#      if a == "SHashlik":
#       narx +=15000
#       if a == "Somsa":
#        narx +=5000 
#        if a == "CHoy":
#           narx +=300
# print(f"Sizning buyurtmalar soningiz:{len(buyurtmalar)}")
# print(f"Sizning to'lovingiz:{narx}")


# a = "5"
# a += "3"
# t = int(a) + 2
# print(float(t))

# a = "10"
# a += "5"
# t = int(a) + 5
# print(float(t))

# Dostlar = []
# a = int(input("Do'stlaringiz nechta: "))

# for i in range(a):
#     ism1 = input(f"{i+1}-do'stingizni kiriting: ")
#     Dostlar.append(ism1)


#     print(f"Qandaysan {Dostlar[0]} yaxshimisan.")
#     print(f"Qandaysan {Dostlar[1]} yaxshimisan yuribsanmi charchamay")
#     print(f"Qandaysan {Dostlar[2]} yaxshimisan yuribsanmi ")
#     print(f"Qandaysan {Dostlar[3]} yaxshimisan yuribsanmi charchamay")
#     print(f"Qandaysan {Dostlar[4]} yaxshimisan")
    
  
# dostlar = []

# son = int(input("Dostlarning soni: "))

# for i in range(son):
#     ism = input(f'{i+1}-dostingizni kiriting: ')
#     dostlar.append(ism)

# for a in range(len(dostlar)):
#     dost = dostlar[a]
#     if a < 3:
#         print(f"Salom {dost}")

#     elif 3 <= a < 6 :
#         print(f"{dost} qalesan")
    
#     elif 6 <= a < 9:
#         print(f"{dost} nima qilayapsan")

#     else:
#         print(f'{dost} yaxhsi')


#  tajriba
    
# from turtle import*

# bgcolor("black")
# speed(0)
# for i in range(200):
#     color("red")
#     circle(i*0.6)
#     color("cyan")
#     circle(i*0.4)
#     right(4)
#     forward(3)
# done()


# from turtle import*
# from colorsys import*
# speed(0)
# bgcolor("black")
# c = 0
# up()
# goto(40,-110)
# down()
# for i in range(350):
#     c+= 0.00065
#     color(hsv_to_rgb(c,1,1))
#     forward(i-20)
#     right(50)
#     circle(40,139)
#     forward(140-i)
# hideturtle()
# done()

# from turtle import*
# bgcolor("black")
# speed(0)
# up()
# goto(0, -40)
# down()
# for i in range(25):
#     for j in range(15):
#         color(j/15, i/25, 1)
#         right(90)
#         circle(170-i*3,90)
#         left(90)
#         circle(170 -i * 3, 90)
#         right(180)
#         circle(45, 24)
# hideturtle()
# done()


# 1-topshiriq

# Kitoblar = {}

# Kitoblar["Python"] = "Guido van Rossum"
# Kitoblar["Java"] = "James Gosling"
# Kitoblar["C++"] = "Bjarne Stroustrup"
# print(Kitoblar)

# 2-topshiriq

# Ballar = {"Ali":85, "Vali":92,"Hasan":78,"Gani":99}
# eng_yuqori = max(Ballar)
# print("Eng yuqori ball olgan talaba:", eng_yuqori)

# 3-topshiriq

# Talabalar = {
# "Ali": {"yosh": 20, "kurs": 2, "universitet": "TATU"},
# "Vali": {"yosh": 21, "kurs": 3, "universitet": "SAMDU"}
# }
# print("Ali ning universiteti:", Talabalar["Ali"]["universitet"])
# Talabalar["Vali"]["kurs"] = 4
# print("Yangilangan lug'at:", Talabalar)

# kitoblar = ("Alpomish","O'tgan kunlar","Mehropdan Chayon","Ufq","Temir tuziklari")
# kitoblar = list(kitoblar)
# kitoblar[3] = 'Iymon'
# kitoblar.append('Jinlar bazmi')
# kitoblar.remove('Alpomish')
# print(f"1-{kitoblar[0]}")
# print(f"2-{kitoblar[1]}")
# print(f"3-{kitoblar[2]}")
# print(f"4-{kitoblar[3]}")
# print(f"5-{kitoblar[4]}")

# kitoblar = tuple(kitoblar)
# print(kitoblar)



# Baholar = (("Ali",88),("Vali",92),("Karim",75),("Gulbahor",81),("Dilnoza",90))
# Baholar = list(Baholar)

# Baholar[3] = ("Karim",75)
# Baholar.append(("Ozod",85))
# Baholar.remove(("Ali",88))

# print(f"1-{Baholar[0]}")
# print(f"2-{Baholar[0]}")
# print(f"3-{Baholar[0]}")
# print(f"4-{Baholar[0]}")

# Baholar = tuple(Baholar)

# print(Baholar)


# kitoblar = ("Alpomish","O'tgan kunlar","Mehropdan Chayon","Ufq","Temir tuziklari")
# kitoblar = list(kitoblar)
# kitoblar[3] = 'Iymon'
# kitoblar.append('Jinlar bazmi')
# kitoblar.remove('Alpomish')
# print(f"1-{kitoblar[0]}")
# print(f"2-{kitoblar[1]}")
# print(f"3-{kitoblar[2]}")
# print(f"4-{kitoblar[3]}")
# print(f"5-{kitoblar[4]}")

# kitoblar = tuple(kitoblar)
# print(kitoblar)


# 1-topshiriq

# raqamlar = [1 ,2 ,3 ,4 ,800000]
# teskari = []
# for i in range(len(raqamlar)-1 -1 -1):
#     teskari.append(raqamlar[i])
#     print(teskari)



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# son= a[::-1]

# print(son)

# 2-topshiriq

# malumotlar = (1,2,3,4,5,6,7,8,9)
# juft = []
# for i in range(len(malumotlar)):
#     if i %2 == 0:
#         juft.append(malumotlar[i])
   
#     print(juft)


# a,b,c = int(input("3 ta son kiriting 1,2,3 ko'rinishida (1 2 3 u mumkin emas!):"))
# # x = (a+b+c)/3
# print(a,b,c)

# kitoblar={}
# kitoblar["O'tgan Kunlar"]="Abdulla Qodriy","1925"
# kitoblar["Mehrobdan Chayon"]= "Abdulla Qodriy","1930"
# kitoblar["Ufq"]="Said Ahmad","1976"
# kitoblar["Chinor"]="Asqad Muhtor","2018"
# kitoblar["Ko'xna Dunyo"]="Odil Yoqubov","2015"
# print(kitoblar)


#  2-Bolim 1 -topshiriq

# malumot = {
# "ism" : "Og'abek",
# "yosh" : 17,
# "dasturlar":["Python","HTML","JavaSicrip","C++"]
# }
# print(malumot)

# 2-topshiriq

# kitoblar = {
# "nomi1":"O'tkan kunlar",
# "mualifi1":"Abdulla Qodiriy",
# "yili1":1925,

# "nomi2":"Chol va dengiz ",
# "mualifi2":"Ernest Hemingway", 
# "yili2":1952,

# "nomi3":"Hayvonot fermasi ",
# "mualifi3":"George Orwell",
# "yili3":1945,
# "nomi4":"Ufq",
# "mualifi4":"Said Ahmad",
# "yili4":1982,

# "nomi5":"Sariq devni minib",
# "mualifi5":"Xudoyberdi To‘xtaboyev",
# "yili5":1974

# }
# print(kitoblar)



# kitoblar={}
# kitoblar["O'tgan Kunlar"]="Abdulla Qodriy","1925"
# kitoblar["Chol va dengiz"]= "Ernest Hemingway","1952"
# kitoblar["Ufq"]="Said Ahmad","1976"
# kitoblar["Hayvonot fermasi"]="George Orwell","1945"
# kitoblar["Sariq devni minib"]="Xudoyberdi To‘xtaboyev","1974"
# print(kitoblar)



# students = {
#     "Ali": {"math": 90, "english": 85, "science": 88},
#     "Vali": {"math": 92, "english": 80, "science": 86},
#     "Sami": {"math": 88, "english": 90, "science": 91},
#     "Karim": {"math": 92, "english": 90, "science": 87},
#     "Zafar": {"math": 92, "english": 90, "science": 87}, 
# }

# qiymatlar = {

# }

# for ism, baho in students.items():
#     x = sum(students[ism].values()) / len(students[ism])
#     qiymatlar[ism] = x

# print(max(qiymatlar.values()))

# foydalanuvchilar = {
# "Akmal":"1234",
# "Dilshod":"abcd",
# "SHahzoda":"999"
  
# }
# login = input("Login kiriting:\t")
# parol = input("Parol kiriting:\t")
# if login in foydalanuvchilar.keys:
#     if foydalanuvchilar[login] == parol:
#         print("Hush kelibsiz")
#     else:
#         print("Nato'g'ri parol")
# elif login not in foydalanuvchilar:
#     print("Login mavjud emas")
#     new_login = input("Yangi login kiriting:")
#     new_parol = input("Yangi parol kiriting:")
#     foydalanuvchilar[new_login] = new_parol
# print(foydalanuvchilar)

# b= int(input("nechi yoshdasiz: c"))
# if b >= 18:
#     print("kirishingiz mumkun")
# else:
#     print("kirish mumkin emas")


# ism = input("Ismingiz nima: ")
# if ism.lower()!="Og'abek":
#     print(f"Uzr,{ism.title()} biz Og'abekni kutayapmiz")
# else:
#     print("Assalom alaykum")





# sevimli_kitobingiz = []
# print("Sevimli kitobingizni kiriting.(Dastur toxtashi uchun 'stop' deb yozing): ")

# while True:
#     kitob = input("Sevimli kitobingizni kiriting...")
#     if kitob.lower()== 'stop':
#         break
#     else:
#         sevimli_kitobingiz.append(kitob)
# print("\n Sizni sevimli kitobingiz:")
# for k in sevimli_kitobingiz:
#     print(kitob)


# sevimli_kitob = []

# print("Sevimli kitobingizni kriting.")
# kitob = "Kitob nomini kiriting "
# kitob += "(dasturni to'xtatish uchun 'stop' deb yozing): "

# while True: 
#      natija= input(kitob)
#      if natija == 'stop':
#         break 
#      else:
#         print(natija)



# soz = input("mevani nomini kiriting: ")
# natija = {}

# for harf in soz:
#     if harf in natija:
#         natija[harf] += 1
#     else:
#         natija[harf] = 1

# print(natija)

# Input: {'a': 3, 'b': 8, 'c': 1, 'd': 6, 'e': 2}
# Output: {'c': 1, 'e': 2, 'a': 3, 'd': 6, 'b': 8}


# soz = input("So'z kiriting: ")
# natija = {}
# for harf in soz:
#     if harf in natija:
#         natija[harf] += 1
#     else:
    
#         natija[harf] = 1


# print(natija)


# import random
# tugri_son = random.randint(1, 10)
# while True:
#     taxmin = int(input("1 dan 10 gacha bo'lgan sonni toping: "))
#     if taxmin == tugri_son:
        
#         print("Tabriklayman, siz topdingiz!")
#         break
#     else:
#         print("Xato! Qayta urinib ko'ring.")




# oylar = {
#     1: "Yanvar",
#     2: "Fevral",
#     3: "Mart",
#     4: "Aprel",
#     5: "May",
#     6: "Iyun",
#     7: "Iyul",
#     8: "Avgust",
#     9: "Sentabr",
#     10: "Oktabr",
#     11: "Noyabr",
#     12: "Dekabr" 
# }
# son = int(input("Oy raqamini kiriting(1 dan 12 gacha): "))
# if son in oylar:
#     print(oylar[son])
# else:
#     print("Uzr bunday oy yo'q")



# kurslar = {
#    " usd": 12_682.31,
#    "eur": 14_734,
#    "rub": 161.35
# }
# valyuta = input("Valyutani tanlang (usd, eur, rub): ").lower()
# miqdor = float(input("Miqdorni kiriting: "))

# if valyuta in kurslar:
#     som = miqdor * kurslar[valyuta]
#     print(f"{miqdor} {valyuta.upper()} = {som:,.2f} so'm")
# else:
#     print("Noto‘g‘ri valyuta turi kiritildi.")




# harakatlar = {
#     "w": "Yuqoriga harakat",
#     "a": "Chapga harakat",
#     "s": "Pastga harakat",
#     "d": "O'ngga harakat"
# }
# h = input("Harakatni kiriting: ")
# if h in harakatlar:
#     print(harakatlar[h])
# else:
#     print("Bunday ishora yo'q")





# import pygame
# import random
# import sys

# # O‘yin ekran o'lchami
# WIDTH, HEIGHT = 400, 600
# WHITE = (255, 255, 255)
# GRAY = (50, 50, 50)
# RED = (200, 0, 0)
# BLUE = (0, 100, 255)
# BLACK = (0, 0, 0)

# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("🏁 Poyga O‘yini")
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 28)

# # Avtomobil o‘lchami va koordinatalari
# car_width = 50
# car_height = 90
# car_x = WIDTH // 2 - car_width // 2
# car_y = HEIGHT - car_height - 10
# car_speed = 7

# # Dushman mashinasi
# enemy_width = 50
# enemy_height = 90
# enemy_x = random.randint(0, WIDTH - enemy_width)
# enemy_y = -enemy_height
# enemy_speed = 5

# score = 0

# def draw_road():
#     screen.fill(GRAY)
#     pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 4)
#     pygame.draw.rect(screen, WHITE, (0, 0, 10, HEIGHT))  # chap yo'l chizig'i
#     pygame.draw.rect(screen, WHITE, (WIDTH-10, 0, 10, HEIGHT))  # o'ng yo'l chizig'i

# running = True
# while running:
#     clock.tick(60)
#     draw_road()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Avtomobil harakati
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and car_x > 10:
#         car_x -= car_speed
#     if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
#         car_x += car_speed

#     # Dushman avtomobil harakati
#     enemy_y += enemy_speed
#     if enemy_y > HEIGHT:
#         enemy_y = -enemy_height
#         enemy_x = random.randint(10, WIDTH - enemy_width - 10)
#         score += 1
#         enemy_speed += 0.3  # Tezlik oshadi

#     # To‘qnashuv tekshiruvi
#     car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
#     enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
#     if car_rect.colliderect(enemy_rect):
#         print(f"💥 Yutqazdingiz! Ochko: {score}")
#         pygame.quit()
#         sys.exit()

#     # Mashinalarni chizish
#     pygame.draw.rect(screen, BLUE, car_rect)
#     pygame.draw.rect(screen, RED, enemy_rect)

#     # Ochko chiqarish
#     score_text = font.render(f"Ochko: {score}", True, BLACK)
#     screen.blit(score_text, (10, 10))

#     pygame.display.update()





from turtle import*
import math
bgcolor("black")
speed(100)
color("red")
pensize(2)
def heart(n):
    x = 15*math.sin(n)**3
    y =12*math.cos(n)-5*\
       math.cos(2*n)-2*\
       math.cos(3*n)-\
       math.cos(4*n)
    return x,y
for i in range(18):
    pendown()
    for j in range(0,100):
        x, y = heart(j/15)
        goto(x*i, y*i)
    penup()
    hideturtle()
done()







