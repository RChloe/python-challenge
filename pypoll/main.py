import os
import csv
import time

# For calculating script runtime
start = time.time()

data_csv = "Homework 3_Instructions_PyPoll_Resources_election_data.csv"
total_votes = 0
candidates = []
candidate_votes = {}
table = {}
formatted_data = []
winner_votes = 0

# Read in the CSV file
with open(data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Add to votes each time
        total_votes += 1
        # If there is a new candidate, add them
        if row[2] not in candidates:
            candidates.append(row[2])
            votes = 1
            candidate_votes.update({row[2]:votes})
        # If we've seen the candidate before, add to their tally
        else:
            votes = candidate_votes[row[2]] + 1
            candidate_votes.update({row[2]:votes})
    # For each candidate, calculate their percentage of the votes
    for key in candidate_votes:
        percent = round(candidate_votes[key]/total_votes*100,2)
        # Make a table of the candidates and percents
        table.update({key:percent})
        # Find whoever has the greatest percentage of votes
        if candidate_votes[key]>winner_votes:
            winner_votes = candidate_votes[key]
            winner = key

    # Create a list of our formatted results
    formatted_data.append("\nElection Results")
    formatted_data.append("-------------------------")
    formatted_data.append("Total Votes: " + str(total_votes))
    formatted_data.append("-------------------------")

    # For each candidate, build a string with their results
    for candidate in candidates:
        print_string = str(candidate) + ": " + str(table[candidate]) + "% ("+ str(candidate_votes[candidate])+")"
        formatted_data.append(print_string)

    # Add candidate results to the results list
    formatted_data.append("-------------------------")
    formatted_data.append("Winner: "+winner)
    formatted_data.append("-------------------------\n")

    # Print and export our formatted data
    output_file = open("HWFile.txt","w")
    for x in range(len(formatted_data)):
        print(formatted_data[x])
        output_file.write(formatted_data[x]+"\n")

end = time.time()
# time to run: 3.885343074798584
# This one takes forever!
print(end - start)