# PyBank

import os
import csv

budget_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)
    
    month_count = int(len(list(csv_reader)))
    print(month_count)
#    for row in csv_reader:
#        #month_count = len(row[0])
 #       print(row)