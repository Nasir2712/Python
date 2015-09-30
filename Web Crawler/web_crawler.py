import urllib.request
from urllib.error import  URLError
import re
import pickle
import shelve

mytuple=()
mylist3=[]
def visit_url(url, domain, mytuple, mylist3):
    global crawler_backlog
    if(len(crawler_backlog)>10):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1    
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_title = re.compile('<title>(?P<title>.*)</title>')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")

            result = regexp_title.search(content_string, re.IGNORECASE)
            
            if result:
                title = result.group("title")
                title=title.lower()
                title_list=title.split()
                for title_word in title_list:
                    mytuple=(url, title_word)
                    mylist3.append(mytuple)

            
            for (urls) in re.findall(regexp_url, content_string):
                    if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                        crawler_backlog[urls] = 0
                        visit_url(urls, domain, mytuple, mylist3)

                        
    except URLError as e:
        print("error")

    x = open("raw_data1.txt","bw")
    pickle.dump(mylist3,x)
    x.close
            
crawler_backlog = {}

seed = "http://www.newhaven.edu/"

crawler_backlog[seed]=0

visit_url(seed, "www.newhaven.edu", mytuple, mylist3)
