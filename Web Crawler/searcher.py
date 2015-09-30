import os
import shelve
def search(d, query):    
    Found_List=[]
    dict1_words=shelve.open(d)

    if ("or" in query) and ("and" not in query): #"OR" search
        query.remove("or")
        print("Performing OR search for: ", query)
        for phrase in query:
            if (phrase in dict1_words):
                querylist=[]
                querylist=querylist+dict1_words[phrase]
                querylist=list(set(querylist))
                for phrase in querylist: 
                    print("Found in ... ",phrase,'\n')         
    elif("and" in query) or (len(query)>1 and ("and" not in query)and("or" not in query)):
        if "and" in query:
            query.remove("and")
        if "or" in query:
            query.remove("or")
        print ("Performing AND search for: ",query)
        list_dict=dict1_words[query[0]]
        for word1 in query[1:]:
            list_dict1=dict1_words[a]
            list_dict=list(set(list_dict).intersection(list_dict1))
        for word2 in list_dict1:
            print("Found in ...", word2, '\n')
          
            
    elif((len(query)==1) and ("and" not in query)and("or" not in query)):
        print ("Searching for: ",query)
        dict1_words[query[0]]=list(set(dict1_words[query[0]]))
        for word3 in dict1_words[query[0]]:
            print("Found in...", word3,'\n')

