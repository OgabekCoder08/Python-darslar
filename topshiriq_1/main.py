# 1-topshiriq
try:
    num1 = int(input("Birinchi sonni kiriting: "))
    num2 = int(input("Ikkinchi sonni kiriting: "))
    amallar = input("amallarni kiriting :+,-,*,/: ")


    if amallar =="+":
        result = num1 + num2
    elif amallar =="-":  
        result = num1 - num2
    elif amallar =="*":
        result = num1 * num2
    elif amallar =="/":
        result = num1 / num2
    else:
        print("Noto'g'ri amal kiritingiz🤷‍♂️")
    print(f"Javob👉: {result}")

except ValueError:
    print("Faqat son kiriting:\n")
except ZeroDivisionError:
    print("0 kiritish mumkin emas❌")
    













