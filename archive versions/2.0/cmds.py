import socket
def getip():
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)

def getdhcp():
    print(socket.gethostbyname(socket.gethostname()))

def gethelp():
    print("""
    Соблюдайте регистр команд и всё будет хорошо
    help / помощь - список команд и пояснение к ним
    getip / мойайпи - получение внешнего адреса компьютера
    getdhcp / получитьdhcp - получение вашего DHCP
    getpcname / имякомпа - получение имени вашего компьютера
    getdomainip / айписайта [ДОМЕН] - получение IP сайта (без http/https)
    sitestatus / статуссайта [ДОМЕН] - проверка статуса сайта (без http/https)
    speedtest / узнатьскорость - измерение скорости скачивания и загрузки
    getmac / получитьмак - получить MAC-адрес
    getmacnum / получитьмакцифры- получить MAC-адрес в виде числа
    scanportsonip / проверитьпортыайпи - проверить популярные открытые порты по IP
    scanportsondomain / проверитьпортыдомен - проверить популярные открытые порты по домену (без http/https)
    rangeportsdomain / диапазонпортовдомен - проверить открытые порты по домену (без http/https)
    rangeportsip / диапазонпортовайпи - проверить открытые порты по айпи
    getcoords / моикоординаты - узнать координаты по своему IP-адресу
    coordsbyip / координатыайпи - узнать координаты по указанному IP-адресу
    citybyip / городпоайпи - узнать город по IP-адресу
    genpass / сделатьпароль - генерирует пароль (английский алфавит + цифры)
    genpassv2 / сложныйпароль - генерирует пароль (английский и русский алфавиты + цифры + символ)
    linklocation / путьссылки - узнать куда ведёт ссылка (без http/https)
    pseudocrypt / псевдошифр - шифрование русских маленьких букв
    cryptoff / шифрвыкл - дешифрование псевдошифра
    """)

def getpcname():
    print(socket.getfqdn())

def getlocalip():
    host = socket.getaddrinfo(socket.gethostname(), None)
    ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
    print(ipv4_addresses)

def getdomainip(x):
    print(socket.gethostbyname(x))

def sitestatus(x):
    import requests
    import urllib.request
    from urllib.error import URLError
    try:
        urllib.request.urlopen("https://" + x)
        print("Сайт доступен")
        status = requests.get('https://' + x)
        print("Код сайта: ", status.status_code)
    except URLError:
        print("Сайт недоступен")

def getmac():
    from uuid import getnode
    import re
    print(':'.join(re.findall('..', '%012x' % getnode())))

def getmacnum():
    from uuid import getnode
    print(getnode())

def scanports(ip, i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.09)
    try:
        connect = sock.connect((ip, i))
        print("Порт ", i, " открыт")
        sock.close()
    except:
        pass

def genpass():
    import passwordmaster
    passwordmaster.gen()

def checkpass():
    import passwordmaster
    password = input("Введите пароль\n")
    passwordmaster.checker(password)

def scanportsv2(ip, i):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.09)
    try:
        connect = sock.connect((ip, i))
        print("Порт ", i, " открыт")
        sock.close()
    except:
        pass

def linklocation(link):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    r = requests.get(link, headers=headers)
    for i, each in enumerate(r.history, 1):
        print(f'{i} {each.status_code} {each.url}')

def pseudocrypt(str):
    text = str
    text = text.replace("а", "0")
    text = text.replace("б", "9")
    text = text.replace("в", "8")
    text = text.replace("г", "7")
    text = text.replace("д", "6")
    text = text.replace("е", "5")
    text = text.replace("ё", "4")
    text = text.replace("ж", "3")
    text = text.replace("з", "2")
    text = text.replace("и", "1")
    text = text.replace("й", "!")
    text = text.replace("к", "@")
    text = text.replace("л", "#")
    text = text.replace("м", "$")
    text = text.replace("н", "%")
    text = text.replace("о", "^")
    text = text.replace("п", "&")
    text = text.replace("р", "*")
    text = text.replace("с", "(")
    text = text.replace("т", ")")
    text = text.replace("у", "-")
    text = text.replace("ф", "_")
    text = text.replace("х", "+")
    text = text.replace("ц", "=")
    text = text.replace("ч", "№")
    text = text.replace("ш", ";")
    text = text.replace("щ", ":")
    text = text.replace("ь", "?")
    text = text.replace("ы", "~")
    text = text.replace("ъ", "`")
    text = text.replace("э", "<")
    text = text.replace("ю", ">")
    text = text.replace("я", ",")
    print(text)

def pseudocryptoff(str):
    text = str
    text = text.replace("0", "а")
    text = text.replace("9", "б")
    text = text.replace("8", "в")
    text = text.replace("7", "г")
    text = text.replace("6", "д")
    text = text.replace("5", "е")
    text = text.replace("4", "ё")
    text = text.replace("3", "ж")
    text = text.replace("2", "з")
    text = text.replace("1", "и")
    text = text.replace("!", "й")
    text = text.replace("@", "к")
    text = text.replace("#", "л")
    text = text.replace("$", "м")
    text = text.replace("%", "н")
    text = text.replace("^", "о")
    text = text.replace("&", "п")
    text = text.replace("*", "р")
    text = text.replace("(", "с")
    text = text.replace(")", "т")
    text = text.replace("-", "у")
    text = text.replace("_", "ф")
    text = text.replace("+", "х")
    text = text.replace("=", "ц")
    text = text.replace("№", "ч")
    text = text.replace(";", "ш")
    text = text.replace(":", "щ")
    text = text.replace("?", "ь")
    text = text.replace("~", "ы")
    text = text.replace("`", "ъ")
    text = text.replace("<", "э")
    text = text.replace(">", "ю")
    text = text.replace(",", "я")
    print(text)