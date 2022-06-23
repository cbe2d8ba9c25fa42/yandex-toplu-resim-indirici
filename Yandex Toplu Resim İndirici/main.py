from colorama import *
import urllib.request
import requests,os,re

def banner():
    os.system("cls")
    print(f"""{Fore.RED}
 ___ ___                 __                   _______.--.--.                   __ 
|   |   |.---.-.-----.--|  |.-----.--.--.    |     __|-----|.----.-----.-----.|  |
 \     / |  _  |     |  _  ||  -__|_   _|    |    |  |  _  ||   _|__ --|  -__||  |
  |___|  |___._|__|__|_____||_____|__.__|    |_______|_____||__| |_____|_____||__|

           {Fore.GREEN} Kodlayan: Umut Şahin ~ Yandex Görsel Arayıcı Ve İndirici
                                                                                  
    """)

def main():
    banner()
    print(f"{Fore.MAGENTA} Aranacak Kelime: {Fore.RED}",end="")
    keyword = input()
    print()
    url = f"https://yandex.com.tr/gorsel/search?text={keyword}&from=morda_new"
    req = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"})
    find = re.findall('{"url":"(.*?)"', req.text)
    if (len(find) != 0):
        num = 1
        os.mkdir("Resimler/"+keyword)
        find = list(set(find))
        for i in find:
            if ("http" in i and i.split(".")[-1] != "css"):
                try:
                    if (i.split(".")[-1] == "png"):
                        urllib.request.urlretrieve(i, "Resimler/"+keyword+"/image"+str(num)+".png")
                    elif (i.split(".")[-1] == "gif"):
                        urllib.request.urlretrieve(i, "Resimler/"+keyword+"/image"+str(num)+".gif")
                    else:
                        urllib.request.urlretrieve(i, "Resimler/"+keyword+"/image"+str(num)+".jpg")
                    print(f"{Fore.GREEN}[TAMAMLANDI {str(num)}] {Fore.RED}{i}")
                    num +=1
                except:
                    continue

if (__name__=="__main__"):
    try:
        init()
        main()
    except KeyboardInterrupt:
        exit()