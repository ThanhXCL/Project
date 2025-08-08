#Kéo, Búa, Bao
import random

def get_user_choice():
    print("Lựa chọn của bạn:")
    print("1. Kéo")
    print("2. Búa")
    print("3. Bao")
    choice = input("Nhập số (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Lựa chọn không hợp lệ. Vui lòng nhập lại (1-3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(p1, p2):
    mapping = {"keo": 0, "bua": 1, "bao": 2}

    i1 = mapping.get(p1)
    i2 = mapping.get(p2)

    if i1 is None or i2 is None:
        return "lỗi"

    if i1 == i2:
        return "hòa"
    elif (i1 == 0 and i2 == 2) or (i1 == 1 and i2 == 0) or (i1 == 2 and i2 == 1):
        return "thắng"
    else:
        return "thua"
