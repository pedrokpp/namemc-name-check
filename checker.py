import requests
import linecache
import time
nicks = open("nicks.txt", "r")
nicks_count = len(nicks.readlines())

for i in range(1, nicks_count + 1):
    r = requests.get("https://namemc.com/search?q=" + linecache.getline('nicks.txt', i).strip("\n"))
    if "Unavailable" in r.text:
        save = open("invalidos.txt", "a")
        save.write(linecache.getline('nicks.txt', i))
        save.write("\n")
        save.close()
        print(linecache.getline('nicks.txt', i) + " é inválido!")
    elif "Too short" in r.text:
        save = open("invalidos.txt", "a")
        save.write(linecache.getline('nicks.txt', i))
        save.write("\n")
        save.close()
        print(linecache.getline('nicks.txt', i) + " é inválido! (muito curto)")
    elif "Available" in r.text:
        save = open("validos.txt", "a")
        save.write(linecache.getline('nicks.txt', i))
        save.write("\n")
        save.close()
        print(linecache.getline('nicks.txt', i) + " é válido!")
    else:
        pass