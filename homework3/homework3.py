from datetime import datetime

def get_birth_date():
    """Запрашивает дату рождения у пользователя и возвращает её в формате datetime."""
    birth_date_str = input("Введите вашу дату рождения (дд/мм/гггг): ")
    return datetime.strptime(birth_date_str, "%d/%m/%Y")

def calculate_age(birth_date):
    """Вычисляет возраст на основе даты рождения."""
    today = datetime.utcnow()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    """Основная функция, которая управляет процессом."""
    birth_date = get_birth_date()
    age = calculate_age(birth_date)
    print(f"Ваш возраст: {age} лет.")

# Вызов основной функции
main()