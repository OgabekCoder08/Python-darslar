# def hisob_kitob():
#     son1 = int(input("1-sonni kiriting:"))
#     son2 = int(input("2-sonni kiriting:"))
#     a= son1*son2
#     b = son1/son2
#     c = son1+son2
#     d = son1-son2
#     return  f+"{son1} * {son2} = {a}    "    f"{son1} / {son2} = {b}  "   f"{son1} + {son2} = {c}  "   f"{son1} - {son2} = {d}"
# print(hisob_kitob())

print("Login kiriting:")
login = input()
print("Parol kiriting:")
parol = input()

if login == "sarvar" and parol == "1234":
  print("Qaysi foydalanuvchi haqida ma'lumot kerak?")
  print("Mavjud ismlar: sarvar, ali, laylo, abdulaziz.")
  ism = ""
  while ism != "stop":
    print("Ism kiriting (yoki 'stop'):")
    ism = input()
    if ism == "sarvar":
      print("Sarvar - Dasturchi, Python bo'yicha tajribaga ega.")
    elif ism == "ali":
      print("Ali - Web dizayner, Figma va Adobe bilan ishlaydi.")
    elif ism == "laylo":
      print("Laylo - Backend dasturchi, Django va FastAPI bilan ishlaydi.")
    elif ism == "abdulaziz":
      print("Abdulaziz - IT dasturchi, Python boyicha tajribasi bor. ")
    elif ism == "stop":
      print("Dastur toxtadi.")
    else:
      print("Ma'lumot topilmadi.")
else:
  print("Login yoki parol notogri.")





















