import requests
import linecache
import time
words = open("words.txt", "r")
words_count = len(words.readlines())

for i in range(1, words_count + 1, 1):
    time.sleep(1)
    r = requests.get("https://api.mojang.com/users/profiles/minecraft/" + linecache.getline('words.txt', i).strip("\n"))
    if "name" in r.text:
        save = open("invalid.txt", "a")
        save.write(linecache.getline('words.txt', i))
        save.write("\n")
        save.close()
        print(linecache.getline('words.txt', i) + " is invalid!")
    else:
        save = open("valid.txt", "a")
        save.write(linecache.getline('words.txt', i))
        save.write("\n")
        save.close()
        print(linecache.getline('words.txt', i) + " is valid!")