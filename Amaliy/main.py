# print("Login kiriting:👉")
# login = input()
# print("Parol kiriting:👉")
# parol = input()

# if login == "Og'abek" and parol == "0808":
#     print("Qaysi foydalanuvchi haqida ma'lumot kerak?")
#     print("Bizda mavjud bo'lgan ismlar: sarvar, ali, laylo, og'abek,zuhriddin,nursulton,gavhar.")
#     ism = ""
#     while ism != "stop":
#         print("Ism kiriting (yoki 'stop'):")
#         ism = input().lower()
#         if ism == "sarvar":
#            print("Sarvar - Dasturchi, Python bo'yicha tajribaga ega.")
#         elif ism == "ali":
#            print("Ali - Web dizayner, Figma va Adobe bilan ishlaydi.")
#         elif ism == "laylo":
#            print("Laylo - Backend dasturchi, Django va FastAPI bilan ishlaydi.")
#         elif ism == "og'abek":
#           print("Og'abek - IT dasturchi, Python boyicha tajribasi bor. ")
#         elif ism == "zuxriddin":
#           print("Zuxriddin - Dasturchi,HTML boyicha tajribasi bor. ")
#         elif ism == "nursulton":
#            print("Nursulton - Dasturchi,C++ boyicha tajribasi bor. ")
#         elif ism == "gavhar":
#            print("Gavhar - Dasturchi,JAVA boyicha tajribasi bor.")
#         elif ism == "stop":
#           print("Dastur toxtadi ❌.")
#         else:
#           print("Ma'lumot topilmadi 🤷‍♂️.")
# else:
#   print("Login yoki parol notogri 🔐.")       


# class Kitob:
  
#     def init(self, nomi, muallifi, sahifa_soni):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.sahifa_soni = sahifa_soni

#     def info(self):
#         print(f"Kitob nomi: {self.nomi}")
#         print(f"Muallif: {self.muallifi}")
#         print(f"Sahifa soni: {self.sahifa_soni}")



# kitob1 = Kitob("Shair va Xato", "Abdulla Oripov", 150)
# kitob2 = Kitob("Yurtimning Manzarasi", "Erkin Vohidov", 200)
# kitob3 = Kitob("Badiiy Poetikalar", "Muhammad Yusuf", 250)


# kitob1.info()
# kitob2.info()
# kitob3.info()



# class Kitob:
  
#     def init(self, nomi, muallifi, sahifa_soni):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.sahifa_soni = sahifa_soni

#     def info(self):
#         print(f"Kitob nomi: {self.nomi}")
#         print(f"Muallif: {self.muallifi}")
#         print(f"Sahifa soni: {self.sahifa_soni}")



# kitob1 = Kitob("Shair va Xato", "Abdulla Oripov", 150)
# kitob2 = Kitob("Yurtimning Manzarasi", "Erkin Vohidov", 200)
# kitob3 = Kitob("Badiiy Poetikalar", "Muhammad Yusuf", 250)


# kitob1.info()
# kitob2.info()
# kitob3.info()


# from uuid import uuid4

# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
        

#     def __str__(self):
#         return f"{self.make} {self.model} {self.yil}-yil, ${self.narh} {self.__km} km {self.__id}"
# avto1 = Avto("GM","Malibu","Qora",2025,27000,10)


# print(avto1) 

# class  Shape:
#     def __init__(self,input_shape):
#         self.input_shape = input_shape

#     def main(self):
#         self.input_shape = input("triangle yoki square kiritishini: ")
#     def check_shape(self):
#         if self.input_shape == "triangle":
#             print("triangle shakli")
#         elif self.input_shape == "square":
#             print("square shakli")
#         else:
#             print("nomalum shakil")




# a = int(input("1-chi katta kesmani uzunligini kiriting:"))
# b = int(input("2-chi katta kesmani uzunligini kiriting:"))
# print(f"kesmani qoplash uchun {a//b} ta kesma kerak")
















                  