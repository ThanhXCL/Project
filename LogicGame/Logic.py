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

def determine_winner(user, computer):
    choices = ["Kéo", "Búa", "Bao"]
    print(f"\nBạn chọn: {choices[user-1]}")
    print(f"Máy chọn: {choices[computer-1]}")

    if user == computer:
        return "Hòa!"
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        return "Bạn thắng!"
    else:
        return "Bạn thua!"

def main():
    print("=== Trò chơi Kéo - Búa - Bao ===")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print("Kết quả:", result)

        again = input("\nChơi tiếp? (y/n): ").lower()
        if again != 'y':
            print("Cảm ơn bạn đã chơi!")
            break

if __name__ == "__main__":
    main()
