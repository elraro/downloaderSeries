from robobrowser import RoboBrowser
import wget
import sys
import re

if len(sys.argv) < 2:
    print("Uso: downloader <serie>")
    print("Ejemplo: downloader http://www.newpct.com/todos-los-capitulos/series/cronicas-vampiricas/")
    exit(-1)

print("Descargando serie " + sys.argv[1])
browser = RoboBrowser(parser="lxml", history=True)
browser.open(sys.argv[1]) # 'http://www.newpct.com/todos-los-capitulos/series/cronicas-vampiricas/'
soup = browser.parsed
temp = soup.find("ul", {"class" : "menu"}).find_all("a", href=True)
count = 0
for t in temp:
    if t["href"] != "#":
        try:
            browser.open(t["href"])
            torrent = browser.parsed
            t_link = torrent.find("span", {"id" : "content-torrent"}).find("a", href=True)
            wget.download(t_link["href"], out="torrent" + str(count) + ".torrent")
            print("Descargado capítulo " + str(count))
            count += 1
        except Exception as e:
            print("Fallo al descargar el capítulo " + t["href"])
