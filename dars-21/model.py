from datetime import datetime
hozir= datetime.now()
def talaba(ism,famila,tyil,kurs,yonalish):
    students = {
        "ism" :ism,
        "famila" :famila,
        "tyil" :tyil,
        "kurs" :kurs,
        "yo'nalish" :yonalish
    }
    print(f"\nIsm:{ism.title()}\nFamila:{famila.title()}\nTug'ilgan yil:{tyil}\nKurs:{kurs()}\nYo'nalish nomi:{yonalish}\nYosh:{hozir-tyil}")

ism = input("Ismingizni kiriting: ")
famila = input("Familangizni kiriting: ")
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
kurs = int(input("Nechanchi kurs: "))
yonalish = input("Yo'nalish nomi: ")
talaba(ism,famila,tyil,kurs,yonalish)