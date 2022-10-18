#MicroOSINT by SiberianHacker (ShwepsikGG) 
from googlesearch import search
quote = input("Кого ищем > ")
print("[Ищем на doxbin]")
for i1 in search("site:doxbin.org " + quote, stop=1000, pause=1):
    print(i1)
print("[Ищем на pastebin]")
for i1 in search("site:pastebin.com " + quote, stop=1000, pause=5):
    print(i1)
print("[Гуглим]")
for i in search(quote, stop=1000, pause=1):
    print(i)