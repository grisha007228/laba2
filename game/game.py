import random

def get_computer_choice():
    """Возвращает выбор компьютера (камень, ножницы или бумага)."""
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Определяет победителя игры."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def main():
    """Основная функция игры."""
    print("Добро пожаловать в игру 'Камень-ножницы-бумага'!")
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    
    if user_choice not in ['камень', 'ножницы', 'бумага']:
        print("Неверный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Компьютер выбрал: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Вызов основной функции
main()