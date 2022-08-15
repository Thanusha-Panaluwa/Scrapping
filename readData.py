import csv

# open CSV file and has read the data and store at the "row" variable.
# for loop helps to read each data one by one.
# now you can use "row" for further.

with open('data.csv', 'rU')as csvfiles:
    spamreader = csv.reader(csvfiles)
    for rows in spamreader:
        #print rows
        row= ', '.join(rows)
        print (row)
        
        #print row
    
    
