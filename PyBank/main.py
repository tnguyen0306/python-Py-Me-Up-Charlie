# PyBank

#Dependencies
import os
import csv

#Assign path to the pull the csv file
budget_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "budget_data.csv")

#Assign the neccessary lists
month_list = []
profit_loss = []
monthly_change = []

#Open and read csv file with assigned path
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Skip the header in the csv file
    csv_header = next(csv_file)
   
    #Create list of months and profit/loss
    for row in csv_reader:
        month_list.append(row[0])
        profit_loss.append(int(row[1]))

    #Total month count in the file    
    month_count = len(month_list)
    
    #Total amount of profit/loss in the file    
    net_total = sum(profit_loss)

    #Calculate and create list of profit change each month
    for i in range(len(profit_loss)-1):
        monthly_change.append(profit_loss[i+1]-profit_loss[i])
    
    #calculate the average of monthly profit change
    average_change = sum(monthly_change)/(month_count-1)
    
    #Look up the greatest increase in profit and the month 
    max_increase = max(monthly_change)
    max_month = month_list[monthly_change.index(max_increase)-1]
    
    #Look up the greatest decrease in profit and the month 
    min_increase = min(monthly_change)
    min_month = month_list[monthly_change.index(min_increase)-1]
    
    #Print the Financial Analysis
    print("Financial Analysis \n----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_increase})")

#Assign the path to export the file
output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis", "Financial_Analysis.txt")

#Export file with assigned path
with open(output_file,"w") as file:
    file.write("Financial Analysis\n----------------------------\n")
    file.write(f"Total Months: {month_count}")
    file.write("\n")
    file.write(f"Total: ${net_total}")
    file.write("\n")
    file.write(f"Average Change: ${round(average_change,2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_month} (${min_increase})")