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
            publisher = details['Publisher']
        except KeyError:
            publisher = ''
        try:
            isbn = details['ISBN']
        except KeyError:
            isbn = ''
        try:
            language = details['Language']
        except KeyError:
            language = ''
        genre = details['Genres'].partition("/")[0]
        genre.replace(","," ")
        user_id = shortuuid.uuid()
        no_of_exchanges = random.randrange(0,10)

        ratings = container[0].findAll("div",{"class":"BHMmbe"})
        if len(ratings) == 0:
            ratings = 0
        else:
            ratings = ratings[0].text

        try:
            f.write(user_id + ',' + title.replace(",","|") + ',' + author.replace(",","|") + ',' + publisher.replace(",","|") + ',' + isbn + "," + language + ',' + str(no_of_exchanges) + ',' + str(ratings) + ',' + genre + "\n")
        except UnicodeEncodeError:
            continue


    f.close()