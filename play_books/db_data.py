from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import shortuuid
import random

def extract(main_url,filename):
    uClient = uReq(main_url)
    main_html = uClient.read()
    uClient.close()
    main_soup = soup(main_html, "html.parser")
    cards = main_soup.findAll("div",{"class":"vU6FJ p63iDd"})
    f = open(filename, "a")

    for card in cards:
        url = 'https://play.google.com' + card.a['href']
        print(url)
        client = uReq(url)
        book = client.read()
        client.close()
        book_soup = soup(book, "html.parser")
        container = book_soup.findAll("main",{"class":"LXrl4c"})
    
        title = container[0].findAll("h1",{"class":"AHFaub"})
        title = title[0].span.text

        author = container[0].findAll("span",{"class":"ExjzWd"})
        try:
            author = author[0].a.text
        except (AttributeError,IndexError):
            author = ''
        info = container[0].findAll("div",{"class":"hAyfc"})

        details = {}

        for i in range(len(info)):
            x = info[i].findAll("div",{"class":"BgcNfc"})
            y = info[i].findAll("span",{"class":"htlgb"})
            details[x[0].text] = y[0].text
        
        try:
            isbn = details['ISBN']
        except KeyError:
            isbn = ''
        try:
            language = details['Language']
        except KeyError:
            language = ''
        genre = details['Genres'].partition("/")[0]
        genre.replace(",","|")
        genre.strip()
        
        cover = container[0].findAll("div",{"class":"hkhL9e"})
        cover_url = cover[0].img['src']

        try:
            f.write(isbn + ',' + title.replace(",","|") + ',' + author.replace(",","|") + ',' + genre + "," + language + ',' + cover_url + "\n")
        except UnicodeEncodeError:
            continue


    f.close()