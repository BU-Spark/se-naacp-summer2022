import csv
from operator import ne

from pandas import crosstab

def crossReference(text, neighborhoods, articleId):
    for n in neighborhoods:
        if n in text:
            (neighborhoods[n]).append(articleId)

    return neighborhoods

def check():
    with open("testfile.csv","r")as file:
        file_reader = csv.reader(file)
        places = {
            'Allston': [],
            'Dorchester': [],
            'South End': [],
            'Downtown': [],
            'Roxbury': [],
        }

        for article in file_reader:
            id = article[0]
            hl1 = article[4]
            hl2 = article[5]
            lede = article[7]
            body = article[8]

            for n in places:
                if n in hl1:
                    (places[n]).append(id)
            
            for n in places:
                if n in hl2:
                    (places[n]).append(id)

            for n in places:
                if n in lede:
                    (places[n]).append(id)

            for n in places:
                if n in body:
                    (places[n]).append(id)

    return places



print(check())
        
