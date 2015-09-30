import os
import time
def search(d):				#search function
    query=input("query: ")
    query = query.strip(" ").split() #get rid of the front and rear spaces, space being the delimiter
    query = list(set(query))
    Found_List=[]

    if ("or" in query) and ("and" not in query): #"OR" search
        query.remove("or")
        print("Performing OR search for: ", query)
        for word in d:
            for quote in query:
                if quote in word[1]:
                    print ("Found at", word[0])
                    print (time.ctime(os.path.getmtime(word[0])))
                    print (os.path.getsize(word[0]))
                    print ('\n')
                    break
    elif("and" in query) or (len(query)==1) or ("and" not in query) and ("or" not in query):
        if "and" in query:
            query.remove("and")
        if "or" in query:
            query.remove("or")
        print ("Performing AND search for: ",query)
        query_len = (len(query))
        i = 0
        for word in d:
            for quote in query:
                if quote in word[1]:
                    i = i + 1
                    if query_len == i:
                        print ("Found at", word[0])
                        print (time.ctime(os.path.getmtime(word[0])))
                        print (os.path.getsize(word[0]))
                        print ('\n')
                        i = 0
