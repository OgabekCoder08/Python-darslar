try:
    Fayl = input("Izlayotgan faylingizni kiriting:👉 ")
    f = open(Fayl)
    print(f.read())
except FileNotFoundError:
    print("Kechirasiz faylingiz topilmadi.🤷")
finally:
    print("Ko'rishguncha hayir sog' bo'ling.")









