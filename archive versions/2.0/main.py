import cmds

print("""Support1k 2.0
github.com/DanilPistoletov/Support1k""")

while "anime" == "anime":
    command = input()
    if command == "getip" or command == "мойайпи":
        cmds.getip()
    elif command == "getdhcp" or command == "получитьdhcp":
        cmds.getdhcp()
    elif command == "help" or command == "помощь":
        cmds.gethelp()
    elif command == "getpcname" or command == "имякомпа":
        print(cmds.socket.getfqdn())
    elif command == "getlocalip":
        cmds.getlocalip()
    elif "getdomainip" in command:
        domain = command[12:]
        cmds.getdomainip(domain)
    elif "айписайта" in command:
        domain1 = command[10:]
        cmds.getdomainip(domain1)
    elif "sitestatus" in command:
        siteforcheck = command[11:]
        cmds.sitestatus(siteforcheck)
    elif "статуссайта" in command:
        siteforcheck1 = command[12:]
        cmds.sitestatus(siteforcheck1)
    elif command == "getmac" or command == "получитьмак":
        cmds.getmac()
    elif command == "getmacnum" or command == "получитьмакцифры":
        cmds.getmacnum()
    elif "rangeportsip" in command:
        na4alo = int(input("Введите начальный порт\n"))
        predel = int(input("Введите последний порт\n"))
        for i in range(na4alo, predel):
            cmds.scanports(command[13:])
    elif "диапазонпортовайпи" in command:
        na4alo1 = int(input("Введите начальный порт\n"))
        predel1 = int(input("Введите последний порт\n"))
        for i in range(na4alo1, predel1):
            cmds.scanports(command[19:])
    elif "rangeportsdomain" in command:
        na4alo2 = int(input("Введите начальный порт\n"))
        predel2 = int(input("Введите последний порт\n"))
        for i in range(na4alo2, predel2):
            cmds.scanports(cmds.socket.gethostbyname(command[17:]))
    elif "диапазонпортовдомен" in command:
        na4alo3 = int(input("Введите начальный порт\n"))
        predel3 = int(input("Введите последний порт\n"))
        for i in range(na4alo3, predel3):
            cmds.scanports(cmds.socket.gethostbyname(command[20:]))
    elif "проверитьпортыдомен" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(cmds.socket.gethostbyname(command[20:]), i)
    elif "scanportsondomain" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(cmds.socket.gethostbyname(command[19:]))
    elif "проверитьпортыайпи" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(command[19:])
    elif "scanportsonip" in command:
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(command[14:])
    elif command == "genpass" or command == "сделатьпароль":
        cmds.genpass()
    elif command == "checkpass" or command == "проверитьпароль":
        cmds.checkpass()
    elif command == "getcoords" or command == "моикоординаты":
        import geocoder
        g = geocoder.ipinfo("me")
        print(g.latlng)
    elif "coordsbyip" in command:
        import geocoder
        g1 = geocoder.ipinfo(command[11:])
        print(g1.latlng)
    elif "координатыайпи" in command:
        import geocoder
        g2 = geocoder.ipinfo(command[15:])
        print(g2.latlng)
    elif "citybyip" in command:
        import geocoder
        g3 = geocoder.ipinfo(command[9:])
        print(g3.city)
    elif "городпоайпи" in command:
        import geocoder
        g4 = geocoder.ipinfo(command[12:])
        print(g4.city)
    elif "linklocation" in command:
        cmds.linklocation("https://" + command[13:])
    elif "путьссылки" in command:
        cmds.linklocation("https://" + command[11:])
    elif "pseudocrypt" in command:
        cmds.pseudocrypt(command[12:])
    elif "псевдошифр" in command:
        cmds.pseudocrypt(command[11:])
    elif "cryptoff" in command:
        cmds.pseudocryptoff(command[9:])
    elif "шифрвыкл" in command:
        cmds.pseudocryptoff(command[9:])
    else:
        print("Неверная команда. Вы можете ввести \"помощь\" для просмотра всех команд")