# PyPoll

#Dependencies
import os
import csv

#Assign path to the pull the csv file
election_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resources", "election_data.csv")

#Open and read csv file with assigned path
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Skip the header in teh csv file
    csv_header = next(csv_file)