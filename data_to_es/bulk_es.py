from elasticsearch import Elasticsearch
from read_file import csv_to_dictreader

filename = '/home/minty/Documents/chicago_parking_ticket_data/data/processed/head_parking_tickets.csv'
host = 'localhost:9200'

es = Elasticsearch([host])

def basic_insert(filename):
    
    list_to_insert = csv_to_dictreader(filename)

    #print(type(list_to_insert), list_to_insert)
    print(str(len(list_to_insert)) + ' records found to insert')
    for record in list_to_insert:
        #print(record)
        es.index(index='ticket_test', doc_type='do_i_need_this', body=record)

    print('Insert complete')


if __name__ == "__main__":

    basic_insert(filename)


