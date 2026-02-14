import socket

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
    scanportsip [IP] - проверить весь диапазон портов по IP
    scanportsdomain [ДОМЕН] - проверить весь диапазон портов по домену
    rangeportsdomain [ДОМЕН] - проверить открытые порты по домену
    rangeportsip [IP] - проверить открытые порты по айпи
    getcoords - узнать координаты по своему IP-адресу
    coordsbyip [IP] - узнать координаты по указанному IP-адресу
    citybyip [IP] - узнать город по IP-адресу
    genpass - генерация пароля
    checkpass - проверка стойкости пароля
    linklocation [ССЫЛКА] - узнать куда ведёт ссылка
    whois [IP/ДОМЕН] - узнать информацию о домене/IP
    ping [IP/ДОМЕН] - пинг интернет-ресурсов
    tracert [IP/ДОМЕН] - трассировка интернет-ресурса
    md5 [ТЕКСТ] - хеширование в MD5
    sha1 [ТЕКСТ] - хеширование в SHA1
    sha512 [ТЕКСТ] - хеширование в SHA512
    sha256 [ТЕКСТ] - хеширование в SHA256
    blake2b [ТЕКСТ] - хеширование в blake2b
    getdns [IP/ДОМЕН] - перечисление DNS
    getssl [IP/ДОМЕН] - проверка SSL
    """)

def getip():
    import requests
    print(requests.get('https://ident.me').text.strip())

def getdhcp():
    print(socket.gethostbyname(socket.gethostname()))

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

def scanports(ip, na4alo2, predel2):
    import nmap
    nm = nmap.PortScanner()
    nm.scan(f'{ip}', f'{na4alo2}-{predel2}', arguments='-v -T4')
    open_ports = [f"{p}/{proto}" for host in nm.all_hosts() for proto in nm[host].all_protocols() for p in
                  nm[host][proto] if nm[host][proto][p]['state'] == 'open']
    print("Открытые:", open_ports or "Нет открытых")

def genpass():
    import passwordmaster
    passwordmaster.gen()

def checkpass():
    import passwordmaster
    password = input("Введите пароль\n")
    passwordmaster.checker(password)

def linklocation(link):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    r = requests.get(link, headers=headers)
    for i, each in enumerate(r.history, 1):
        print(f'{i} {each.status_code} {each.url}')
    print(f'Финальная ссылка: {r.status_code} {r.url}')

def whois(site):
    import socket
    s = socket.socket()
    s.connect(('whois.iana.org', 43))
    s.send((f'{site}' + '\r\n').encode())
    print(s.recv(4096).decode())
    s.close()

def ping(site):
    import subprocess
    result = subprocess.run(['ping', site], capture_output=True)
    print(result.stdout.decode('cp866', errors='replace'))

def tracert(site):
    import subprocess
    result = subprocess.run(['tracert', site], capture_output=True, encoding='cp866', errors='replace')
    print(result.stdout)

def md5(text):
    import hashlib
    print(hashlib.md5(text.encode("utf-8")).hexdigest())

def sha1(text):
    import hashlib
    print(hashlib.sha1(text.encode("utf-8")).hexdigest())

def sha512(text):
    import hashlib
    print(hashlib.sha512(text.encode("utf-8")).hexdigest())

def sha256(text):
    import hashlib
    print(hashlib.sha256(text.encode("utf-8")).hexdigest())

def blake2b(text):
    import hashlib
    print(hashlib.blake2b(text.encode("utf-8")).hexdigest())

def getdns(site):
    import subprocess, platform
    s = platform.system()
    for t in 'A MX NS TXT'.split():
        print(f"\n=== {t} ===")
        cmd = ['powershell', '-Command', f'Resolve-DnsName {site} -Type {t}'] if s == 'Windows' else ['dig', '+short', site, t]
        print(subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace').stdout)

def getssl(site):
    import ssl, socket
    ctx = ssl.create_default_context()
    with socket.create_connection((site, 443)) as s:
        with ctx.wrap_socket(s, server_hostname=site) as ss:
            c = ss.getpeercert()
            for k, v in c.items():
                print(f"{k}: {v}")
