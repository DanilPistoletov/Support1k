import cmds

print("""Support1k 2.1.1
github.com/DanilPistoletov/Support1k""")

while "anime" == "anime":
    command = input().lower()
    if command == "getip":
        cmds.getip()
    elif command == "getdhcp":
        cmds.getdhcp()
    elif command == "help":
        cmds.gethelp()
    elif command == "getpcname":
        print(cmds.socket.getfqdn())
    elif command == "getlocalip":
        cmds.getlocalip()
    elif "getdomainip" in command:
        domain = command[12:].replace('http://', '').replace('https://', '')
        cmds.getdomainip(domain)
    elif "sitestatus" in command:
        siteforcheck = command[11:].replace('http://', '').replace('https://', '')
        cmds.sitestatus(siteforcheck)
    elif command == "getmac":
        cmds.getmac()
    elif command == "getmacnum":
        cmds.getmacnum()
    elif "rangeportsip" in command:
        na4alo = int(input("Введите начальный порт\n"))
        predel = int(input("Введите последний порт\n"))
        for i in range(na4alo, predel):
            cmds.scanports(command[13:], i)
        print("Сканирование завершено")
    elif "rangeportsdomain" in command:
        na4alo2 = int(input("Введите начальный порт\n"))
        predel2 = int(input("Введите последний порт\n"))
        for i in range(na4alo2, predel2):
            cmds.scanports(cmds.socket.gethostbyname(command[17:]), i)
        print("Сканирование завершено")
    elif "scanportsdomain" in command:
        domain = command[16:].replace('http://', '').replace('https://', '')
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(cmds.socket.gethostbyname(domain), i)
        print("Сканирование завершено")
    elif "scanportsip" in command:
        ip = command[12:].replace('http://', '').replace('https://', '')
        print(ip)
        ports = [7, 20, 21, 22, 23, 25, 53, 69, 80, 81, 110, 115, 143, 389, 443, 587, 993, 995, 2083, 2087, 2222, 3128, 3306, 5432, 8080, 8083]
        for i in ports:
            cmds.scanportsv2(ip, i)
        print("Сканирование завершено")
    elif command == "genpass":
        cmds.genpass()
    elif command == "checkpass":
        cmds.checkpass()
    elif command == "getcoords":
        import geocoder
        g = geocoder.ipinfo("me")
        print(g.latlng)
    elif "coordsbyip" in command:
        import geocoder
        g1 = geocoder.ipinfo(command[11:])
        print(g1.latlng)
    elif "citybyip" in command:
        import geocoder
        g3 = geocoder.ipinfo(command[9:])
        print(g3.city)
    elif "linklocation" in command:
        link = command[13:].replace('http://', '').replace('https://', '')
        cmds.linklocation("https://" + link)
    else:
        print("Такой команды нет. Введите \"help\" для просмотра всех команд")