class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'

    def get_admin_access_level(self):
        return self.__admin_access_level

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: можно добавлять только экземпляры класса User.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удалён.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


# Список пользователей
users = []

# Создание администратора
admin1 = Admin(1, "Иван Админ")

# Добавление пользователей
user1 = User(2, "Алексей")
user2 = User(3, "Мария")

admin1.add_user(users, user1)
admin1.add_user(users, user2)

# Вывод списка пользователей
print("\nТекущие пользователи:")
for user in users:
    print(f"ID: {user.get_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")

# Удаление пользователя
admin1.remove_user(users, 2)

# Вывод обновлённого списка
print("\nОбновлённый список пользователей:")
for user in users:
    print(f"ID: {user.get_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")






