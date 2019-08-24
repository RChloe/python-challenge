import os
import csv
import time

# For calculating script runtime
start = time.time()

# Path to collect data from the Resources folder
data_csv = "Homework 3_Instructions_PyBank_Resources_budget_data.csv"
months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
greatest_profit_change = 0
worst_profit_change = 0

# Define the function and have it accept each row from our file
def data_analysis(data):
    month = data[0]
    profit = data[1]
    # Return values of these indexes
    return(month,profit)
    
# Read in the CSV file
with open(data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Take the output from our function
        month,profit = data_analysis(row)
        # Count total months
        months += 1
        # Sum total profit
        total_profit = total_profit + int(profit)
        # If we're at the first row, set initial values
        if row[0] == 'Jan-2010':
            profit_change = 0
            profit_change_list.append(profit_change)
        # If we're at any other row, run rolling calculations
        else:
            profit_change = int(profit) - previous_profit
            profit_change_list.append(profit_change)
        # Get greatest and worst profit change with comparison
        if profit_change > greatest_profit_change:
            greatest_profit_change = profit_change
            greatest_profit_change_month = month
        elif profit_change < worst_profit_change:
            worst_profit_change = profit_change
            worst_profit_change_month = month
        # Reset previous_profit
        previous_profit = int(profit)
    # Calculate the average change over time
    avg_change = sum(change for change in profit_change_list)/(len(profit_change_list)-1)
    # Round the average change
    avg_change = round(avg_change,2)

    # Print and write our data to a file
    print (f'Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${total_profit}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {greatest_profit_change_month} (${greatest_profit_change})\nGreatest Decrease in Profits: {worst_profit_change_month} (${worst_profit_change})')
    output_file = open("HWFile.txt","w")
    output_file.write(f'Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${total_profit}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {greatest_profit_change_month} (${greatest_profit_change})\nGreatest Decrease in Profits: {worst_profit_change_month} (${worst_profit_change})')

end = time.time()
# time to run: 0.0004928112030029297
# This one's super fast
print(end - start)
