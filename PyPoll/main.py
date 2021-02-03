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

print(candidate_name)


#Get the total vote for each candidate
