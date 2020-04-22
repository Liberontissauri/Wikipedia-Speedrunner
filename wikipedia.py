import requests
from bs4 import BeautifulSoup

def getlinks(URL):
    page = requests.get(URL)

    links = []

    soup = BeautifulSoup(page.content, "html.parser")

    for paragraph in soup.findAll("p"):
        if None in (paragraph):
            continue
        for tag in paragraph.findAll("a"):
            if tag.get("href")[0] == "/" and "/wiki/Wikipedia:" not in tag.get("href") and "/w/index.php" not in tag.get("href"):
                links.append(tag.get("href"))

    return links

print(getlinks("https://en.wikipedia.org/wiki/Pok%C3%A9mon_Sword_and_Shield"))

def mergelinks(linklists):
    finallist = []
    for linklist in linklists:
            for link in linklist:
                if link not in finallist:
                    finallist.append(link)
    return finallist
