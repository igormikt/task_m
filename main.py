class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # Статус задачи: по умолчанию не выполнена

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Выполнено" if self.completed else "❌ Не выполнено"
        return f"{self.description} (до {self.deadline}) — {status}"


tasks = []  # список задач

def add_task(description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

def show_uncompleted_tasks():
    print("📋 Невыполненные задачи:")
    for i, task in enumerate(tasks):
        if not task.completed:
            print(f"{i + 1}. {task}")

def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1].mark_completed()
        print("✅ Задача отмечена как выполненная.")
    else:
        print("⚠️ Неверный номер задачи.")


add_task("Купить молоко", "2025-06-10")
add_task("Сделать домашнее задание", "2025-06-09")

show_uncompleted_tasks()
complete_task(1)
show_uncompleted_tasks()
