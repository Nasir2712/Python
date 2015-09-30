import urllib.request
import json
from pprint import pprint
import pickle
import shelve

query=input("query: ")
query = query.strip(" ").split() #get rid of the front and rear spaces, space being the delimiter
query = list(set(query)) 
str1="http://api.openweathermap.org/data/2.5/weather?q="
a=len(query)
if (len(query)<=1):
    str2=query[0]
elif(len(query)>1):
    str2 = query[0]+query[1]
str3=str1+str2    
page = urllib.request.urlopen(str3)
code=page.getcode()
content=page.read()
if (code == 200):
    content_string = content.decode("utf-8")
    json_data = json.loads(content_string)
    pprint(json_data)

def process_data(pickle_file, shelve_file):
    global dict1_words
    dict1_words = {}
    word_list=[]
    i=0
    h=open(pickle_file,"br")
    mylist2=pickle.load(h)
    shelve_file = shelve.open(shelve_file)
    for quote1 in mylist2:                               # quote1 is the quote inside a tuple 
        quote2=list(quote1[1:])                          # quote2 is quote in a list
        for quote3 in quote2:                            # quote3 is the whole string
            words = quote3.split()
            for word in words:
                dict1_words.setdefault(word,[]).append(quote1[0:1])
   

                    
    for key,value in dict1_words.items():
        shelve_file[key]=(value)
    h.close
    shelve_file.close()
    
process_data("raw_data.txt","shelve_file")
