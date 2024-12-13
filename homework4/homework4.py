import random

def find_multiples():
    # Генерируем случайный список из 50 чисел в диапазоне от 0 до 200
    numbers = [random.randint(1, 200) for _ in range(50)]
    print(f"Сгенерированные числа: {numbers}")
    
    # Запрашиваем у пользователя число X
    x = int(input("Введите число X: "))
    
    # Используем лямбда-функцию для фильтрации кратных чисел
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    # Выводим найденные числа
    print(f"Числа, кратные {x}: {multiples}")

# Вызов функции
find_multiples()