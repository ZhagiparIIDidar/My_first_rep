import os 
import string

# my_path = input("enter a path")
# all_items = []
# my_path = r"C:\Users\didar\OneDrive\Рабочий стол\test"

""" 
# 1)
for root, dirs, files in os.walk(my_path):
    for name in dirs + files:
        all_items.append(name)
for el in range(0, len(all_items)):
    print(f"{el+1}){all_items[el]}")
"""

"""
# 2)
def check_path_access(path):
    checks = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
    return checks

access_checks = check_path_access(my_path)

print(f"Проверка доступа для пути: {my_path}")
print(f"Существует: {access_checks['exists']}")
print(f"Читаемый: {access_checks['readable']}")
print(f"Записываемый: {access_checks['writable']}")
print(f"Исполняемый: {access_checks['executable']}") 
"""

""" 
def check_path_details(path):
    for root, dirs, files in os.walk(my_path):
        for name in dirs + files:
            if not os.path.exists(path):
                print(f"The path '{path}' does not exist.")
                return
            print("----------------")
            print(f"Checking details for: {path}")
            print(f"Exists: {os.path.exists(path)}")
            print(f"Filename: {os.path.basename(path) if os.path.isfile(path) else ''}")
            print(f"Directory: {os.path.dirname(path)}")
            print("---------------")
check_path_details("C:\\Users\\didar\\OneDrive\\Рабочий стол\\test\\file1.txt")
"""

""" 
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"The file has {sum(1 for _ in file)} lines.")

# Проверяем путь
count_lines(new_path)
 """
# new_path = r"C:\Users\didar\OneDrive\Рабочий стол\test\file1.txt"

""" 
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(f"{item}\n")

# Пример списка
my_list = ["apple", "banana", "cherry", "date"]


# Записываем список в файл
write_list_to_file(new_path, my_list)

print(f"List written to {new_path}")
"""    

""" # Перебираем буквы от A до Z
for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"  # Создаём имя файла, например "A.txt"
    # os.remove(file_name)
    with open(file_name, "w") as file:
        file.write(f"This is {file_name}")  # Записываем в файл
    print(f"Created: {file_name}")
 """
""" 
with open("a1.txt", "r", encoding="utf-8") as src, open("a2.txt", "w", encoding="utf-8") as dest:
    for line in src:
        dest.write(line)
 """

""" def delete_file(file_path):

    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return

    if not os.access(file_path, os.W_OK):
        print(f"No write access to '{file_path}', cannot delete.")
        return

    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")


delete_file("a3.txt")
 """