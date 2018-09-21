import json
import csv 

filename = '/home/minty/Documents/chicago_parking_ticket_data/data/processed/head_parking_tickets.csv'

def csv_to_dictreader(filename):
    
    result = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            result.append(row)

    return result


if __name__ == "__main__":

    list = csv_to_dictreader(filename)

    for i in list:
        print(i)
