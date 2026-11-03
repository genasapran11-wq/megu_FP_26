# Практична робота за заняттями 1–6. «Каса крамниці» — ВАРІАНТ ІЗ ЗАГОТОВКАМИ
# Прізвище, ім'я: ____________________   Група: ________
#
# Заголовки функцій уже написані. Замініть None на правильний вираз
# і впишіть числа зі своєї картки там, де стоїть 0.
# Перевірка:  python check_practical.py practical_scaffold
#
# Правила ті самі: return, а не print; вхідні списки не змінювати;
# ШІ-помічники заборонено. Роботу треба захистити онлайн.

CARD = 0  # номер вашої картки

cart = [120, 1000, 45, 300]

print(len(cart))  # 4


# ============ ЧАСТИНА 1. Функції каси ============

# Ф1. Вартість позиції. item_cost(25, 4) -> 100
def item_cost(price, quantity):
    return None  # ціна помножити на кількість


# Ф2. Вартість позиції плюс пакування. item_cost_with_packing(10, 3, 5) -> 35
def item_cost_with_packing(price, quantity, packing):
    return None  # використайте item_cost(...) і додайте packing


# Ф3. Знижка з картки. Для картки 1: discount_price(1000) -> 850.0
def discount_price(price):
    if price >= 0:      # замініть 0 на поріг знижки з картки
        return None     # ціна мінус відсоток: price - price * ... / 100
    else:
        return price


# Ф4. Доставка з картки. Для картки 1: delivery_cost(899) -> 60
def delivery_cost(total):
    if total >= 0:      # замініть 0 на межу безкоштовної доставки
        return 0
    else:
        return None     # вартість доставки з картки


# Ф5. Новий список із доданою ціною. add_item([10, 20], 30) -> [10, 20, 30]
def add_item(cart, price):
    return None  # підказка: cart + [...]   (НЕ append!)


# Ф6. Ціни після знижки. Для картки 1: discounted_all([100, 1000]) -> [100, 850.0]
def discounted_all(cart):
    return None  # підказка: [discount_price(p) for p in ...]


# Ф7. Сума кошика. cart_total([10, 20, 30]) -> 60
def cart_total(cart):
    return None  # вбудована функція sum


# Ф8. До сплати: сума після знижки + доставка від цієї суми.
#     Для картки 1: receipt_total(cart) -> 1315.0
def receipt_total(cart):
    total = None    # cart_total(discounted_all(...))
    return None     # total + delivery_cost(...)


# ============ ЧАСТИНА 2. Виправте нечисті функції ============
# Перепишіть кожну на чисту. Над функцією напишіть, що в ній було не так.

fee = 40


# Ч2.1. Має стати price_with_fee(price, fee):  price_with_fee(100, 40) -> 140
def price_with_fee(price):
    return price + fee


# Ч2.2. Має повертати НОВИЙ список:  add_gift([10, 20]) -> [10, 20, 0]
def add_gift(cart):
    cart.append(0)
    return cart
