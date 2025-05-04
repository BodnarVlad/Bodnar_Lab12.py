#Завдання 1
inventory = [
    {"назва товару": "Ноутбук", "кількість": 10, "ціна за одиницю": 25000, "категорія": "електроніка"},
    {"назва товару": "Футболка", "кількість": 20, "ціна за одиницю": 400, "категорія": "одяг"},
    {"назва товару": "Хліб", "кількість": 50, "ціна за одиницю": 20, "категорія": "продукти"},
    {"назва товару": "Телевізор", "кількість": 5, "ціна за одиницю": 15000, "категорія": "електроніка"},
    {"назва товару": "Джинси", "кількість": 8, "ціна за одиницю": 900, "категорія": "одяг"},
    {"назва товару": "Молоко", "кількість": 15, "ціна за одиницю": 30, "категорія": "продукти"},
    {"назва товару": "Навушники", "кількість": 12, "ціна за одиницю": 1200, "категорія": "електроніка"},
]

print("=== Завдання 1: Таблиця інвентаризації ===")
print(f"{'Назва':<15}{'Кількість':<10}{'Ціна':<10}{'Категорія':<15}")
for item in inventory:
    print(f"{item['назва товару']:<15}{item['кількість']:<10}{item['ціна за одиницю']:<10}{item['категорія']:<15}")

#Завдання 2
print("\n=== Завдання 2: Пошук та редагування ===")
try:
    search_type = input("Шукати за назвою чи категорією? (введіть 'назва' або 'категорія'): ").strip().lower()
    if search_type not in ['назва', 'категорія']:
        raise ValueError("Невірний тип пошуку.")

    search_value = input(f"Введіть {search_type} для пошуку: ").strip().lower()
    found_items = []

    for item in inventory:
        if item[search_type].lower() == search_value:
            found_items.append(item)

    if not found_items:
        raise LookupError("Товар(и) не знайдено.")

    for item in found_items:
        print(f"\nЗнайдено: {item}")
        update = input("Бажаєте оновити цей товар? (так/ні): ").strip().lower()
        if update == 'так':
            field = input("Що оновити? ('кількість' або 'ціна'): ").strip().lower()
            if field == "кількість":
                new_qty = int(input("Нова кількість: "))
                if new_qty < 0:
                    raise ValueError("Кількість не може бути від’ємною.")
                item["кількість"] = new_qty
            elif field == "ціна":
                new_price = float(input("Нова ціна: "))
                if new_price < 0:
                    raise ValueError("Ціна не може бути від’ємною.")
                item["ціна за одиницю"] = new_price
            else:
                print("Невірне поле.")
            print("Оновлено:", item)

except ValueError as ve:
    print("Помилка вводу:", ve)
except LookupError as le:
    print("Пошук:", le)
except Exception as e:
    print("Інша помилка:", e)

#Завдання 3
print("\n=== Завдання 3: Аналітика складу ===")

# Підрахунок вартості по кожній категорії
category_totals = {}
for item in inventory:
    category = item["категорія"]
    total = item["кількість"] * item["ціна за одиницю"]
    category_totals[category] = category_totals.get(category, 0) + total

print("\nЗагальна вартість товарів по категоріях:")
for cat, total in category_totals.items():
    print(f"{cat.title()}: {total} грн")

# Категорія з найбільшою сумарною вартістю
max_cat = max(category_totals, key=category_totals.get)
print(f"\nКатегорія з найбільшою сумарною вартістю: {max_cat.title()} ({category_totals[max_cat]} грн)")

# Товари з кількістю менше порогового значення
threshold = 5
low_stock_items = [item for item in inventory if item["кількість"] < threshold]
if low_stock_items:
    print(f"\nТовари з кількістю менше {threshold}:")
    for item in low_stock_items:
        print(f"{item['назва товару']} ({item['кількість']} шт)")
else:
    print(f"\nНемає товарів з кількістю менше {threshold}.")
