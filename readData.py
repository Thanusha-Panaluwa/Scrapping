import csv

with open('data.csv', 'rU')as csvfiles:
    spamreader = csv.reader(csvfiles)
    for rows in spamreader:
        #print rows
        row= ', '.join(rows)
        print (row)
        
        #print row
    
    
