import requests
from bs4 import BeautifulSoup


def spider(maxPages):
    dist = 1
    homePage = "https://www.gumtree.com"
    while dist < maxPages:
        url = "https://www.gumtree.com/search?q=&search_category=computing-it-jobs&search_location=Lincoln&distance=" + str(dist)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll("a", {"class": "listing-link"}):
            href = r"https://www.gumtree.com" + link.get("href")
            if href == homePage:
                continue
            getPostData(href)
            print(href)

        dist += 1

def getPostData(postURL):
    sourceCode = requests.get(postURL)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText)
    for postName in soup.findAll("h1", {"class": "space-mbs"}):
        print(postName.string)

spider(15)
