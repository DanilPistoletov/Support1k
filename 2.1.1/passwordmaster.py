from collections import Counter
import random
illegal = ['qwerty', '12345', 'admin', 'user', 'password']
Small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Symbol = ['`', '~', '!', '@', '"', '#', '№', '$', ';', '%', '^', ':', '&', '?', '*', '(', ')', '-', '_', '+', '=', '<', '>', ',', '.', '/', '|', '\\', '{', '}', '[', ']']
Number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def checker(password):
    lenght = len(password)
    Count = Counter(password)
    small = sum(map(Count.__getitem__, Small))
    big = sum(map(Count.__getitem__, Big))
    symbol = sum(map(Count.__getitem__, Symbol))
    number = sum(map(Count.__getitem__, Number))
    if password in illegal:
        print("Уровень пароля - Недопустимый")
    elif lenght > 49 and small > 4 and big > 4 and symbol > 4 and number > 4:
        print("Уровень пароля - Отличный")
    elif lenght > 29 and small > 2 and big > 2 and symbol > 2 and number > 2:
        print("Уровень пароля - Хороший")
    elif lenght > 10:
        print("Уровень пароля - Приемлемый")
    elif lenght < 11:
        print("Уровень пароля - Ненадёжный")

def gen():
    cmd = str(
        input("Выберите уровень пароля:\n1 - Отличный\n2 - Хороший\n3 - Приемлемый\n4 - Ненадёжный\n5 - Недопустимый\n"))
    if cmd == "1":
        randomn = random.randint(10, 30)
        small = random.choices(Small, k=randomn)
        big = random.choices(Big, k=randomn)
        symbol = random.choices(Symbol, k=randomn)
        number = random.choices(Number, k=randomn)
        password = small + big + symbol + number
        random.shuffle(password)
        print(''.join(password))
    elif cmd == "2":
        randomn = random.randint(9, 15)
        small = random.choices(Small, k=randomn)
        big = random.choices(Big, k=randomn)
        number = random.choices(Number, k=randomn)
        randomn = 3
        symbol = random.choices(Symbol, k=randomn)
        password = small + big + symbol + number
        random.shuffle(password)
        print(''.join(password))
    elif cmd == "3":
        randomn = random.randint(11, 30)
        password = random.choices(Small, k=randomn)
        print(''.join(password))
    elif cmd == "4":
        randomn = random.randint(5, 10)
        password = random.choices(Small, k=randomn)
        print(''.join(password))
    elif cmd == "5":
        password = random.choices(illegal, k=1)
        print(''.join(password))