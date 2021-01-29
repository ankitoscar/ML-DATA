import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Change the url for different genres
my_url="https://www.goodreads.com/choiceawards/best-nonfiction-books-2020"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"inlineblock pollAnswer resultShown"})

#change the fike name to obtain books categorised by their genre
filename="non-fiction_genre.csv"
f=open(filename,'w')
headers="Votes, Title, Cover_Image\n"

f.write(headers)

for container in containers:
 	votes=container.strong.text.split()[0]
 	title=container.div.div.a.img['alt']
 	cover_img=container.div.div.a.img['src']

 	print("Votes "+votes)
 	print("Title "+ title)
 	print("Cover_Image "+cover_img)
 	f.write(votes.replace(',','')+","+title+","+cover_img+"\n")
	

f.close()	
