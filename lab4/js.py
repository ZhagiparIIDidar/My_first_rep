import json

# Открываем и читаем JSON файл
with open('sample-data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Выводим заголовок
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

# Обрабатываем и выводим данные
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    DN = attributes['dn']
    Description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(f"{DN:<50} {Description:<20} {speed:<10} {mtu:<10}")