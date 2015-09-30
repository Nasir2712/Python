from data_load import data_list

query=input("query: ")
query = query.strip(" ").split() 
query = list(set(query))         

if ("or" in query) and ("and" not in query):    
    query.remove("or")                          
    print("Performing OR search for: ", query)
    for i, quote in enumerate(data_list):
        for word in query:                      
            if (word in quote):
                index1 = quote.index(word)
                print("Found:", i, "...", quote[index1:index1+50],"...")


elif ("and" in query) and ("or" not in query):    
    query.remove("and")                          
    print("Performing AND search for: ", query)
    for i,quote in enumerate(data_list):
        if (query[0] in quote) and (query[1] in quote):
            print("Found:", i, "...", quote[:500],"...")
            
elif(len(query)==1):
    for i,quote in enumerate(data_list):
        found_at = quote.find(query[0])
        if( found_at > 0):
            print("Found:", i, "..."+quote[found_at:found_at+50], "...")

elif ('and' not in query) and ("or" not in query):
    for i,quote in enumerate(data_list):
        if (query[0] in quote) and (query[1] in quote):
            print("Found:", i, "...", quote[:500],"...")
            

else :
    query.remove("and")
    query.remove("or")
    for i,quote in enumerate(data_list):
        if (query[0] in quote) and (query[1] in quote):
            print("Found:", i, "...", quote[:500],"...")
