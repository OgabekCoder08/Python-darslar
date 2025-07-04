talabalar = []
baholar = []
print("Assalom alaykum hurmatli foydalanuvchi.")
n = int(input("Nechta talaba kiritasiz👉: "))
for i in range(n):
  ism = input(f"{i+1} - talabaning isimni kiriting: ")
  baho = float(input(f"{ism} bahosini kiriting: "))
talabalar.append(ism)
baholar.append(baho)

ortacha = sum(baholar)/ len(baholar)
print(f"Talabalarning o'rtacha bahosi👉{ortacha}")





