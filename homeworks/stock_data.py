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


stock_data(".\\files")