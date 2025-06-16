import tkinter as tk

# Создаём главное окно
root = tk.Tk()
# Меняем цвет заднего фона
root.configure(background="chartreuse3")

root.title("Приветствие")
root.geometry("300x150")  # размеры окна

# Функция, которая срабатывает при нажатии кнопки
def say_hello():
    name = name_entry.get()
    greeting_label.config(text=f"Привет, {name}!")

# Поле ввода
name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=10)

# Кнопка
hello_button = tk.Button(root, text="Сказать привет", command=say_hello, bg="chartreuse2")
hello_button.pack(pady=5)

# Метка для вывода результата
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

# Запуск приложения
root.mainloop()