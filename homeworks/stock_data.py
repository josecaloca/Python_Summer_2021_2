'''
Instructions:
1. Please download a CSV file containing the stock history of some companies, for example from:
http://finance.yahoo.com/q/hp?s=GOOG
http://finance.yahoo.com/q/hp?s=IBM
http://finance.yahoo.com/q/hp?s=MSFT

(Download Data)
Save files giving them different names to a local folder on your drive

2. Write a program that searches for CSV files with stock rates in a given folder and for every one of them:

3. Calculates the percentage change betweeen Close and Open price and adds these values as another column to this CSV file.
You can replace the old file or create a new one.

Change = (Close-Open)/Open

4. The output files can be stored in another folder
5. You can use Python to download files. An example is given here: https://github.com/prubach/Python_Summer_2021_2/blob/master/download_file.py
6. Please do not use pandas, or only use it as an alternative way of implementing it along a more "manual" way using just python without any libraries.
'''

import os
import csv

def stock_data(folder):
    for a in os.listdir(folder):
        path = os.path.join(folder, a)
        try:
            if path.endswith('.csv'):
                with open(path, 'r') as input, open(path + str('.csv'), 'w') as output:
                    reader = csv.reader(input)
                    writer = csv.writer(output, lineterminator='\n')

                    list = []
                    row = next(reader)
                    row.append('Change')
                    list.append(row)

                    if row[1].lower() == 'open' and row[4].lower() == 'close':
                        for row in reader:
                            row.append((float(row[4]) - float(row[1])) / float(row[1]))
                            list.append(row)

                        writer.writerows(list)
        except (OSError) as nve:
            print(type(nve))
            print(str(type(nve)) + ' handling: ' + str(nve))


stock_data(".\\files") # there should be created a folder called "files" that contains the data to read and manipulate