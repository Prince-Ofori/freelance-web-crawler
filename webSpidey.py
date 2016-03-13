import requests
from bs4 import BeautifulSoup

def spider(maxPages):
    homePage = "https://www.gumtree.com"
    
    for i in range(1, maxPages):
        url = "https://www.gumtree.com/search?q=&search_category=computing-it-jobs&search_location=Lincoln&distance=" + str(i)
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
    
        for link in soup.findAll("a", {"class": "listing-link"}):
            href = (r"https://www.gumtree.com" + link.get("href"))
            if href == homePage:
                continue
            
            getPostData(href)
            print(href + "\n")

def getPostData(postURL):
    sourceCode = requests.get(postURL)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText)
    
    for postName in soup.findAll("h1", {"class": "space-mbs"}):
        print(postName.string)

if __name__ == "__main__":
    maxPages = int(input("Enter max number of pages: "))
    spider(maxPages)
