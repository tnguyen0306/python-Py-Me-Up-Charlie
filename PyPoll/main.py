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

#Get the total vote for each candidate
candidate1 = candidate_list.count(candidate_name[0])
candidate2 = candidate_list.count(candidate_name[1])
candidate3 = candidate_list.count(candidate_name[2])
candidate4 = candidate_list.count(candidate_name[3])

#Calulate the precentage of vote for each candidates
percent1 = 100 * candidate1/total_vote
percent2 = 100 * candidate2/total_vote
percent3 = 100 * candidate3/total_vote
percent4 = 100 * candidate4/total_vote
percent_list = [percent1,percent2,percent3,percent4]

#Find the winner
winner_candidate = candidate_name[percent_list.index(max(percent_list))]

#Print the Election results
print(f"Election Results \n-------------------------")
print(f"Total Votes: {total_vote}\n----------------------------")
print(f"{candidate_name[0]}: {percent1:.3f}% ({candidate1})")
print(f"{candidate_name[1]}: {percent2:.3f}% ({candidate2})")
print(f"{candidate_name[2]}: {percent3:.3f}% ({candidate3})")
print(f"{candidate_name[3]}: {percent4:.3f}% ({candidate4})")
print(f"----------------------------")
print(f"Winner: {winner_candidate}")
print(f"----------------------------")