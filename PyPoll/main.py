# PyPoll

#Dependencies
import os
import csv

#Assign path to the pull the csv file
election_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "election_data.csv")

#Assign the neccessary lists
id_list = []
county_list = []
candidate_list = []
candidate_name = []

candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0

#Open and read csv file with assigned path
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Skip the header in the csv file
    csv_header = next(csv_file)
    
    #Create list of months and profit/loss
    for row in csv_reader:
        id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

#Get the total vote based on the length of Voter ID list
total_vote = len(id_list)

#Look up to see who is the candidate
for x in candidate_list:
    if x not in candidate_name:
        candidate_name.append(x)

#Get the total vote for each candidate
for i in candidate_list:
    if str(candidate_list[i]) == str(candidate_name[0]):
        candidate1 = candidate1 +1
    elif str(candidate_list[i]) == str(candidate_name[1]):
        candidate2 = candidate2 +1
    elif str(candidate_list[i]) == str(candidate_name[2]):
        candidate3 = candidate3 +1
    elif str(candidate_list[i]) == str(candidate_name[3]):
        candidate4 = candidate4 +1

print(candidate1)
print(candidate2)
print(candidate3)
print(candidate4)
