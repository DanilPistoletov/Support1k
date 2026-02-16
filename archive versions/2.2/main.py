import cmds

print("""Support1k 2.2
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
        ip = cmds.socket.gethostbyname(command[13:]).replace('http://', '').replace('https://', '')
        cmds.scanports(ip, na4alo, predel)
        print("Сканирование завершено")
    elif "rangeportsdomain" in command:
        na4alo2 = int(input("Введите начальный порт\n"))
        predel2 = int(input("Введите последний порт\n"))
        ip = cmds.socket.gethostbyname(command[17:]).replace('http://', '').replace('https://', '')
        cmds.scanports(ip, na4alo2, predel2)
        print("Сканирование завершено")
    elif "scanportsdomain" in command:
        ip = command[16:].replace('http://', '').replace('https://', '')
        cmds.scanports(ip, 1, 10)
        print("Сканирование завершено")
    elif "scanportsip" in command:
        ip = cmds.socket.gethostbyname(command[12:]).replace('http://', '').replace('https://', '')
        cmds.scanports(ip, 1, 10)
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
    elif "whois" in command:
        cmds.whois(command[6:].replace('http://', '').replace('https://', ''))
    elif "ping" in command:
        cmds.ping(command[5:].replace('http://', '').replace('https://', ''))
    elif "tracert" in command:
        cmds.tracert(command[8:].replace('http://', '').replace('https://', ''))
    elif "md5" in command:
        cmds.md5(command[4:])
    elif "sha1" in command:
        cmds.sha1(command[5:])
    elif "sha512" in command:
        cmds.sha512(command[7:])
    elif "sha256" in command:
        cmds.sha256(command[7:])
    elif "blake2b" in command:
        cmds.blake2b(command[8:])
    elif "getdns" in command:
        cmds.getdns(command[7:])
    elif "getssl" in command:
        cmds.getssl(command[7:])
    else:
        print("Такой команды нет. Введите \"help\" для просмотра всех команд")
