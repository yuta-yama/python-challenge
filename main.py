# PyBank Pseudo Code

# Import OS and CSV Tools
import os
import csv

# Open File Path
filepath = os.path.join("..", "Resources", "budget_data.csv")

# Import CSV
with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)

#skip the headers
next(csvreader, None)

# print the title
print("Financial Analysis")
print("-----------------------")

## TOTAL MONTHS:
    
    # create a dictionary
    dict = {}
    
    # loop through the csv and create a dictionary for each row
    for row in csvreader:
        dict.update({'row[0]': row[1]})
    
    # for the total, count the number of entries in the dictionary
    print("Total Months: " + len(dict))

## TOTAL