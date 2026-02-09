import socket
def getip():
    import urllib.request
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)

def getdhcp():
    print(socket.gethostbyname(socket.gethostname()))

def gethelp():
    print("""
    help - список команд и пояснение к ним
    getip - получение внешнего адреса компьютера
    getdhcp - получение вашего DHCP
    getpcname - получение имени вашего компьютера
    getdomainip [ДОМЕН] - получение IP сайта
    sitestatus [ДОМЕН] - проверка статуса сайта
    getmac - получить MAC-адрес
    getmacnum - получить MAC-адрес в виде числа
    scanportsip [IP] - проверить популярные открытые порты по IP
    scanportsdomain [ДОМЕН] - проверить популярные открытые порты по домену
    rangeportsdomain [ДОМЕН] - проверить открытые порты по домену
    rangeportsip [IP] - проверить открытые порты по айпи
    getcoords - узнать координаты по своему IP-адресу
    coordsbyip [IP] - узнать координаты по указанному IP-адресу
    citybyip [IP] - узнать город по IP-адресу
    genpass - генерация пароля
    checkpass - проверка стойкости пароля
    linklocation [ССЫЛКА] - узнать куда ведёт ссылка
    """)

def getpcname():
    print(socket.getfqdn())

def getlocalip():
    host = socket.getaddrinfo(socket.gethostname(), None)
    ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
    print(*ipv4_addresses)

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
    print(f'Финальная ссылка: {r.status_code} {r.url}')
