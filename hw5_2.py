user_name_true = "Alex"
password_true = "Galex207"

user_name = input("Введите имя пользователя - ")
if user_name == user_name_true:
    print(f"Имя пользователя введено верно - {user_name}")
    password = input("Введите пароль - ")
    if password == password_true:
        print("Пароль введен верно")
        print("Вам открыт доступ в систему")
    else:
        print("Пароль неверный")
else:
    print("Имя введено неверно")