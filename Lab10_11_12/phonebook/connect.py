import csv
import psycopg2
from config import load_config

# SQL-команды для создания таблицы
commands = [
    """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """
]
def insert_from_input():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
                print("Запись успешно добавлена.")
    except Exception as e:
        print("Ошибка при вставке:", e)
def create_table():
    try:
        config = load_config()  # Загружаем параметры из config.py
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            # conn.commit() не нужен — он вызывается автоматически при выходе из with
        print("Таблица успешно создана.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка при создании таблицы:", error)
def update_entry():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                old_name = input("Введите имя, которое нужно обновить: ")
                new_name = input("Новое имя (оставьте пустым, если не менять): ")
                new_phone = input("Новый номер (оставьте пустым, если не менять): ")

                if new_name:
                    cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, old_name))
                if new_phone:
                    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, new_name or old_name))

                print("Данные обновлены.")
    except Exception as e:
        print("Ошибка при обновлении:", e)
def insert_from_csv(file_path):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur, open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # пропускаем заголовок
                for row in reader:
                    if len(row) == 2:
                        name, phone = row
                        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
                print("Данные из CSV успешно загружены.")
    except Exception as e:
        print("Ошибка при загрузке из CSV:", e)
def search_entries():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                name = input("Введите имя для поиска (или оставьте пустым): ").strip()
                phone = input("Введите номер телефона (или оставьте пустым): ").strip()

                if name and phone:
                    cur.execute("SELECT * FROM phonebook WHERE name = %s AND phone = %s", (name, phone))
                elif name:
                    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
                elif phone:
                    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
                else:
                    cur.execute("SELECT * FROM phonebook")

                results = cur.fetchall()
                if results:
                    print("\nРезультаты:")
                    for row in results:
                        print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                else:
                    print("Ничего не найдено.")
    except Exception as e:
        print("Ошибка при поиске:", e)
def delete_entry():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                name = input("Введите имя для удаления (или оставьте пустым): ").strip()
                phone = input("Введите номер телефона для удаления (или оставьте пустым): ").strip()

                if name:
                    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
                elif phone:
                    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                else:
                    print("Нужно ввести хотя бы имя или телефон.")
                    return
                
                print("Запись удалена.")
    except Exception as e:
        print("Ошибка при удалении:", e)
if __name__=='__main__':
    create_table()
