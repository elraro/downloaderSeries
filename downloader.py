from robobrowser import RoboBrowser
import wget
import sys

if len(sys.argv) < 2:
    print("Uso: downloader <serie>")
    print("Ejemplo: downloader http://www.newpct.com/todos-los-capitulos/series/cronicas-vampiricas/")
    exit(-1)

print("Descargando serie " + sys.argv[1].split("/")[5] + "\n")
browser = RoboBrowser(parser="lxml", history=True)
browser.open(sys.argv[1]) # 'http://www.newpct.com/todos-los-capitulos/series/cronicas-vampiricas/'
temp = browser.find("ul", {"class" : "menu"}).find_all("a", href=True)
count = 0
for t in temp:
    if t["href"] != "#":
        try:
            browser.open(t["href"])
            t_link = browser.find("span", {"id" : "content-torrent"}).find("a", href=True)
            wget.download(t_link["href"], out=sys.argv[1].split("/")[5] + str(count) + ".torrent")	
            print("Descargado capítulo " + str(count))
            count += 1
        except Exception as e:
            print("Fallo al descargar el capítulo " + t["href"])
