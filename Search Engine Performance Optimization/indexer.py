import pickle
import fnmatch
import os

def process_data(d):
    f1 = open(d,"br")
    mylist1 = pickle.load(f1)
    f1.close()
    return mylist1
