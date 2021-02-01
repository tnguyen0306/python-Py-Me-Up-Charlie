# PyBank

import os
import csv
import numpy as np

budget_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "budget_data.csv")

month_list = []
profit_loss = []
monthly_change = []

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    csv_header = next(csv_file)
   
    for row in csv_reader:
        month_list.append(row[0])
        profit_loss.append(int(row[1]))
        
    month_count = len(month_list)
    
    net_total = np.sum(profit_loss)

    for i in range(len(profit_loss)-1):
        monthly_change.append(profit_loss[i+1]-profit_loss[i])
    
    average_change = sum(monthly_change)/(month_count-1)
    
    max_increase = max(monthly_change)
    max_month = month_list[monthly_change.index(max_increase)-1]
    
    min_increase = min(monthly_change)
    min_month = month_list[monthly_change.index(min_increase)-1]
    
    print("Financial Analysis \n----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: {round(average_change,2)}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_increase})")
