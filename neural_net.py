def greet_user(name):
    """
    Функция для приветствия пользователя по имени.
    :param name: Имя пользователя
    :return: Приветственное сообщение
    """
    return f"Привет, {name}! Рад приветствовать тебя."

if __name__ == "__main__":
    # Получаем имя пользователя
    user_name = input("Введите ваше имя: ")

    # Приветствуем пользователя
    greeting_message = greet_user(user_name)
    print(greeting_message)