from collections import Counter
import random
illegal = ['qwerty', '12345', 'admin', 'user', 'password']
from string import ascii_lowercase as Small, ascii_uppercase as Big, digits as Number
Symbol="`~!@\"#№$;%^:&?*()-_+=<>.,/|\{}[]"

def checker(password):
    Count = Counter(password)
    small = sum(map(Count.__getitem__, Small))
    big = sum(map(Count.__getitem__, Big))
    symbol = sum(map(Count.__getitem__, Symbol))
    number = sum(map(Count.__getitem__, Number))
    if password in illegal:
        print("Уровень пароля - Недопустимый")
    elif len(password) > 49 and small > 4 and big > 4 and symbol > 4 and number > 4:
        print("Уровень пароля - Отличный")
    elif len(password) > 29 and small > 2 and big > 2 and symbol > 2 and number > 2:
        print("Уровень пароля - Хороший")
    elif len(password) > 10:
        print("Уровень пароля - Приемлемый")
    elif len(password) < 11:
        print("Уровень пароля - Ненадёжный")

def gen():
    cmd = str(
        input("Выберите уровень пароля:\n1 - Отличный\n2 - Хороший\n3 - Приемлемый\n4 - Ненадёжный\n5 - Недопустимый\n"))
    if cmd == "1":
        p = sum([random.choices(g, k=random.randint(10, 30)) for g in [Small, Big, Symbol, Number]], [])
        random.shuffle(p)
        print(''.join(p))
    elif cmd == "2":
        small = random.choices(Small, k=random.randint(9, 15))
        big = random.choices(Big, k=random.randint(9, 15))
        number = random.choices(Number, k=random.randint(9, 15))
        symbol = random.choices(Symbol, k=3)
        password = small + big + symbol + number
        random.shuffle(password)
        print(''.join(password))
    elif cmd == "3":
        print(''.join(random.choices(Small, k=random.randint(11, 30))))
    elif cmd == "4":
        print(''.join(random.choices(Small, k=random.randint(5, 10))))
    elif cmd == "5":
        print(''.join(random.choices(illegal, k=1)))
