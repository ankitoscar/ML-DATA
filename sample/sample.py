from play_books_scraper import extract

url = 'https://play.google.com/store/books/collection/cluster?clp=sgItCiUKH3Byb21vdGlvbl9ib29rc190b3BzZWxsaW5nX2ZyZWUQRBgBIgQIBQgs:S:ANO1ljKt8L0&gsr=CjCyAi0KJQofcHJvbW90aW9uX2Jvb2tzX3RvcHNlbGxpbmdfZnJlZRBEGAEiBAgFCCw%3D:S:ANO1ljLTEQk'

filename = 'sample.csv'

extract(url,filename)