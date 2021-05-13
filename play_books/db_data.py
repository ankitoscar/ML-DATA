from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from uuid import uuid4

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
        genre = genre.strip()
        genre = genre_selector(genre)

        description = container[0].findAll("div",{"class":"DWPxHb"})
        description = description[0].text
        
        cover = container[0].findAll("div",{"class":"hkhL9e"})
        cover_url = cover[0].img['src']

        user_id = uuid4()

        try:
            f.write(str(user_id) + ',' + isbn + ',' + title.replace(','," ") + ',' + '' + ',' + author.replace(","," ") + ',' + genre + "," + language.upper() + ',' + cover_url + "\n")
        except UnicodeEncodeError:
            continue


    f.close()

def genre_selector(genre):
    genre = genre.lower()
    if "business & economics" in genre:
        return "BUSINESS"
    elif "fiction" in genre:
        return "FICTION"
    elif "fantasy" in genre and "nonfiction" not in genre and "science" not in genre:
        return "FANTASY"
    elif "sports" in genre:
        return "SPORTS"
    elif "self-help" in genre:
        return "SELF_DEVELOPMENT"
    elif "history" in genre:
        return "HISTORICAL"
    elif "biography" in genre:
        return "BIOGRAPHY"
    elif "health" in genre:
        return "HEALTH"
    elif "family" in genre:
        return "FAMILY"
    elif "children" in genre or "juvenile" in genre:
        return "CHILDRENS"
    elif "drama" in genre:
        return "DRAMA"
    elif "dictionary" in genre:
        return "DICTIONARY"
    elif "humor" in genre or "comedy" in genre or "comic" in genre:
        return "HUMOR"
    elif "action" in genre:
        return "ACTION"
    elif "adventure" in genre:
        return "ADVENTURE"
    elif genre == "sciene":
        return "SCIENCE"
    elif genre == "science fiction" or genre == "sci-fi":
        return "SCIENCE_FICTION"
    elif "cooking" in genre:
        return "COOKING"
    elif "crime" in genre:
        return "CRIME"
    elif "religion" in genre:
        return "RELIGION"
    elif "travel" in genre:
        return "TRAVEL"
    elif "mathematics" in genre:
        return "MATH"
    elif "encyclopedia" in genre:
        return "ENCYKLOPEDIA"
    elif genre == "western":
        return "WESTERN"
    elif "romance" in genre or "romantic" in genre:
        return "ROMANCE"
    elif "jounal" in genre or genre == "journalism":
        return "JOURNALISM"
    elif "fairy" in genre or "fairies" in genre or "fairytale" in genre:
        return "FAIRYTAIL"
    elif genre == "guide":
        return "GUIDE"
    else:
        return "OTHER"