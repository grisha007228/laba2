def get_number():
    """Генератор нечетных чисел из диапазона от 0 до 29."""
    for number in range(30):
        if number % 2 != 0:  # Проверяем, является ли число нечетным
            yield number

def main():
    """Основная функция для вывода значений."""
    odd_numbers = get_number()
    
    # Инициализируем переменные для хранения значений
    first = None
    fifth = None
    last = None
    
    # Используем цикл for для перебора значений
    for index, number in enumerate(odd_numbers):
        if first is None:
            first = number  # Сохраняем первое нечетное число
        if index == 4:  # Пятое нечетное число (индекс 4)
            fifth = number
        last = number  # Обновляем последнее нечетное число
    
    # Выводим результаты
    print(f"Первое нечетное число: {first}")
    print(f"Пятое нечетное число: {fifth}")
    print(f"Последнее нечетное число: {last}")

# Вызов основной функции
main()