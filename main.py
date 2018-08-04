import os
import csv
import operator
import collections
import sys

##### PYBANK #####

filepath = os.path.join("Resources", "budget_data.csv")

d = {}
change = {}
past_month = 0
cur_month = 0
diff = 0
total = 0

file = open('output.txt', 'w+')

def output(file, output_item):
    sys.stdout.write(output_item)
    file.write(output_item)

output(file, "Financial Analysis \n")
output(file, "------------------------ \n")

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        d.update({row[0]:int(row[1])})
        cur_month = int(row[1])
        if past_month == 0:
            change.update({row[0]:int(0)})
        else:
            diff = cur_month - past_month
            change.update({row[0]:diff})
        past_month = int(row[1])
        
output(file, "Total Months: " + str(len(d)) + " \n")

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total += int(row[1])
        
output(file, "Total: $" + str(total) + " \n")

avg_total = 0
for key, value in change.items():
    avg_total += value
    
output(file, "Average Change: $" + str(round(avg_total/85, 2)) + " \n")

maxvalue = max(change.values())
for m in change.keys(): 
    if change[m] == maxvalue:
        output(file, "Greatest Increase in Profits: " + m + " ($" + str(change[m]) +") \n")

minvalue = min(change.values())
for k in change.keys(): 
    if change[k] == minvalue:
        output(file, "Greatest Decrease in Profits: " + k + " ($" + str(change[k]) +") \n")

output(file, " \n")
        
    
##### PYPOLL #####

filepath = os.path.join("Resources", "election_data.csv")

output(file, "Election Results \n")
output(file, "------------------------ \n")

names = []

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        names.append(row[2])
        
total = len(names)
output(file, "Total Votes: " + str(total) + "\n")
output(file, "------------------------ \n")

from collections import Counter

d = Counter(names)

from collections import defaultdict

d2 = dict(d)

khan = d['Khan']
correy = d['Correy']
li = d['Li']
otooley = d["O'Tooley"]

output(file, "Khan: " + str(round((khan/total)*100, 3)) + "% (" + str(khan) + ") \n")
output(file, "Correy: " + str(round((correy/total)*100, 3)) + "% (" + str(correy) + ") \n")
output(file, "Li: " + str(round((li/total)*100, 3)) + "% (" + str(li) +") \n")
output(file, "O'Tooley: " + str(round((otooley/total)*100, 3)) + "% (" + str(otooley) + ") \n")
output(file, "------------------------ \n")

output(file, "Winner: " + max(d2.items(), key = operator.itemgetter(1))[0] + "\n")
output(file, "------------------------ \n")