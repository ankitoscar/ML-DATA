import uuid
import random

filename = 'user_selection.csv'

f = open(filename,"w")

genres = ['action','romance','thriller','crime','horror','comedy','dark humour','sci-fi','self help','finance','adventure']

authors = ['Sidney Sheldon','Agatha Christie','Edgar Allan Poe','Mark Twain','Dan Brown','Jules Verne','Chetan Bhagat','Amish Tripathi','Khalid Hosseini','Ian Fleming','Charles Dickens']

headers = "userid, genre_1, genre_2, genre_3, genre_4, genre_5, author_1, author_2, author_3, author_4, author_5\n"

f.write(headers)

for i in range(30):
    userid = uuid.uuid4().hex
    f.write(userid + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ','
            + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors) + '\n')

    print(userid + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ',' + random.choice(genres) + ','
            + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors) + ',' + random.choice(authors))
