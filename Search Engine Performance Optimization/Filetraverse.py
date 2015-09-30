import os
import fnmatch
import pickle

mylist=[]
start_dir = "fortune1"
for dirpath, dirs, files in os.walk(start_dir):
    for single_file in files:
        filepath = os.path.abspath(os.path.join(dirpath, single_file))
        
        if fnmatch.fnmatch(single_file, "*txt"):
            f = open(os.path.join(dirpath, single_file))
            data = f.read()
            tup = (filepath,data)
            mylist.append(tup)

f1=open("raw_data.pickle.txt","bw")
pickle.dump(mylist,f1)
f.close()

                    
		    
