import re

# Чтение файла example.txt.txt
with open('lab5/example.txt.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 1. Найти строку, содержащую 'a', за которой следует ноль или более 'b'
def match_a_followed_by_zero_or_more_bs(text):
    pattern = r'a*b*'
    return re.findall(pattern, text)

# 2. Найти строку, содержащую 'a', за которой следует от двух до трех 'b'
def match_a_followed_by_two_to_three_bs(text):
    pattern = r'ab{2,3}'
    return re.findall(pattern, text)

# 3. Найти последовательности строчных букв, соединенных подчеркиванием
def find_lowercase_joined_with_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# 4. Найти последовательности одной прописной буквы, за которой следуют строчные буквы
def find_uppercase_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# 5. Найти строку, содержащую 'a', за которой следует что угодно, заканчивающееся на 'b'
def match_a_followed_by_anything_ending_in_b(text):
    pattern = r'a.*b'
    return re.findall(pattern, text)

# 6. Заменить все пробелы, запятые или точки на двоеточие
def replace_space_comma_dot_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

# 7. Преобразовать строку в snake_case в camelCase
def snake_to_camel(text):
    pattern = r'(_\w)'
    return re.sub(pattern, lambda x: x.group(1)[1].upper(), text)

# 8. Разделить строку по прописным буквам
def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, text)

# 9. Вставить пробелы перед словами, начинающимися с прописной буквы
def insert_spaces_before_capitals(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', text)

# 10. Преобразовать строку в camelCase в snake_case
def camel_to_snake(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', text).lower()

# Выполнение функций и вывод результатов
print("1. Строки, содержащие 'a', за которой следует ноль или более 'b':")
print(match_a_followed_by_zero_or_more_bs(text))

# print("\n2. Строки, содержащие 'a', за которой следует от двух до трех 'b':")
# print(match_a_followed_by_two_to_three_bs(text))

# print("\n3. Последовательности строчных букв, соединенных подчеркиванием:")
# print(find_lowercase_joined_with_underscore(text))

# print("\n4. Последовательности одной прописной буквы, за которой следуют строчные буквы:")
# print(find_uppercase_followed_by_lowercase(text))

# print("\n5. Строки, содержащие 'a', за которой следует что угодно, заканчивающееся на 'b':")
# print(match_a_followed_by_anything_ending_in_b(text))

# print("\n6. Замена всех пробелов, запятых или точек на двоеточие:")
# print(replace_space_comma_dot_with_colon(text))

# print("\n7. Преобразование строки в snake_case в camelCase:")
# print(snake_to_camel(text))

# print("\n8. Разделение строки по прописным буквам:")
# print(split_at_uppercase(text))

# print("\n9. Вставка пробелов перед словами, начинающимися с прописной буквы:")
# print(insert_spaces_before_capitals(text))

# print("\n10. Преобразование строки в camelCase в snake_case:")
# print(camel_to_snake(text))