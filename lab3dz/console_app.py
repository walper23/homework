import json
import os

FILE_NAME = "data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def show_tasks(data):
    if not data:
        print("Нет задач")
        return
    for task in data:
        print(f"{task['id']} | {task['title']} | {task['status']}")


def add_task(data):
    title = input("Введите задачу: ").strip()
    if not title:
        print("Пустая строка!")
        return

    new_id = max([t["id"] for t in data], default=0) + 1

    data.append({
        "id": new_id,
        "title": title,
        "status": "не выполнено"
    })

    print("Добавлено!")


def delete_task(data):
    try:
        task_id = int(input("ID для удаления: "))
    except:
        print("Ошибка ввода")
        return

    for task in data:
        if task["id"] == task_id:
            data.remove(task)
            print("Удалено!")
            return

    print("Не найдено")


def update_task(data):
    try:
        task_id = int(input("ID для изменения: "))
    except:
        print("Ошибка ввода")
        return

    for task in data:
        if task["id"] == task_id:
            task["status"] = "выполнено" if task["status"] == "не выполнено" else "не выполнено"
            print("Обновлено!")
            return

    print("Не найдено")


def search_task(data):
    word = input("Поиск: ").lower()
    for task in data:
        if word in task["title"].lower():
            print(f"{task['id']} | {task['title']} | {task['status']}")


def main():
    data = load_data()

    while True:
        print("\n1. Показать\n2. Добавить\n3. Удалить\n4. Изменить статус\n5. Поиск\n0. Выход")
        choice = input("Выбор: ")

        if choice == "1":
            show_tasks(data)
        elif choice == "2":
            add_task(data)
        elif choice == "3":
            delete_task(data)
        elif choice == "4":
            update_task(data)
        elif choice == "5":
            search_task(data)
        elif choice == "0":
            save_data(data)
            print("Сохранено!")
            break
        else:
            print("Ошибка выбора")


if __name__ == "__main__":
    main()