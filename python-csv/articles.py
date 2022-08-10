from doctest import testfile
from re import subn
from webbrowser import get
from xml.etree.ElementPath import prepare_parent
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import csv
import ast


#gets access to the database
cred = credentials.Certificate('access.json')
firebase_admin.initialize_app(cred, {

    'databaseURL': 'https://test-5fd70-default-rtdb.firebaseio.com/'

})

#gets a reference of the database and creates the articles collection
database = db.reference('/')
database.child('articles')
artbase = db.reference('/articles')

#csv file containing the article information
articles = "testfile.csv"




"""
Returns an array of languages of the article.
input -> string str
output -> arr lst
"""
def formatLangToList(str):
    if str == "":
        return []
    lst = [str.strip("[]")]
    return lst

"""
Returns an array of terms of the article.
input -> string str
output -> arr lst
"""
def formatStrToList(str):
    if str == "":
        return []
    lst = str.split(',')
    return lst



"""
"""
def getNumMentions(str):
    
    return

"""
Iterates line by line through the suburbs csv file and populates the articles collection in database.
"""
def addArticles():
    #track number of database inputs
    lineCounter = -1
    with open(articles,"r") as file:
        file_reader = csv.reader(file)
        #hash table keeps track of neighborhoods inputed in database
        seen = {}

        #format each neighborhood follows
        format = {
            "body":"", 
            "language": '', 
            "word count": 0,
            "content id": '',
            "publisher": '',
            "date": '',
            'author': '',
            'neighborhoods': [],
            "licensor terms": [],
            'indexing terms': {},
            'meta': {
                'copyright': '', 
                'volume': '', 
                'issue number': '',
            },
            "file name": articles,
            "folder name": '',
        }

        for line in file_reader:
            lineCounter += 1
            #neighborhood name
            artId = line[12]
            #if the name is not avaiable, move to next entry
            if artId == '' or lineCounter <= 0:
                continue
            newArt = format.copy()
            if artId not in seen:
                seen[artId] = 1
                #add data to article
                newArt['body'] = line[8]
                newArt['language'] = formatLangToList(line[9])
                newArt['word count'] = int(line[10])
                newArt['content id'] = artId
                newArt['publisher'] = line[16]
                newArt['date'] = line[17]
                newArt['author'] = line[6]
                newArt['neighborhoods'] = ['none']
                newArt['licensor terms'] = formatStrToList(line[18])

                #prevent error caused by blank column
                if line[19] != "" and line[19] != " " and line[19] != None:
                    newArt['indexing terms'] = ast.literal_eval(line[19])
                else:
                    newArt['indexing terms'] = {}
                 
                newArt['meta']['copyright'] = line[11]
                newArt['meta']['volume'] = line[13]
                newArt['meta']['issue number'] = line[14]
                #add article to collection
                artbase.child(artId).set(newArt)

        print(len(seen))
        #print(seen)

addArticles()