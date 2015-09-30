import data_load
import indexer 
import searcher
d = indexer.process_data("raw_data.pickle.txt")
searcher.search(d)

