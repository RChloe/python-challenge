import csv

def average(numbers):
    avg = sum(numbers/len(numbers))
    return avg

file = 'Homework 3_Instructions_PyBank_Resources_budget_data.csv'
#file = os.path.join("..","Desktop","cereal.csv")

with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    csvreader = list(csv.reader(csvfile, delimiter=','))

    # Count rows to get total months (not including header)
    total_profit = sum(int(row[1]) for row in csvreader)
    months = sum(1 for row in csvreader)
    avg_change = total_profit/len(csvreader)
    print(avg_change)
    #total_profit = sum(row[1] for row in csvreader)
