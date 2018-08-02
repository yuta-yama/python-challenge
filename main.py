import os
import csv
import operator
import collections

# PyBank

filepath = os.path.join("Resources", "budget_data.csv")

d = {}
change = {}
past_month = 0
cur_month = 0
diff = 0
total = 0

print("Financial Analysis")
print("-----------------------")

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
        
print("Total Months: " + str(len(d)))

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total += int(row[1])
        
print("Total: $" + str(total))

avg_total = 0
for key, value in change.items():
    avg_total += value
    
print("Average Change: $" + str(round(avg_total/85, 2)))

maxvalue = max(change.values())
for m in change.keys(): 
    if change[m] == maxvalue:
        print ("Greatest Increase in Profits: " + m + " ($" + str(change[m]) +")")


minvalue = min(change.values())
for k in change.keys(): 
    if change[k] == minvalue:
        print ("Greatest Decrease in Profits: " + k + " ($" + str(change[k]) +")")

print(" ")
        
# PyPoll

filepath = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("------------------------")

names = []

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        names.append(row[2])
        
total = len(names)
print("Total Votes: " + str(total))
print("------------------------")

from collections import Counter

d = Counter(names)

from collections import defaultdict

d2 = dict(d)

khan = d['Khan']
correy = d['Correy']
li = d['Li']
otooley = d["O'Tooley"]

print("Khan: " + str(round((khan/total)*100, 3)) + "% (" + str(khan) +")")
print("Correy: " + str(round((correy/total)*100, 3)) + "% (" + str(correy) +")")
print("Li: " + str(round((li/total)*100, 3)) + "% (" + str(li) +")")
print("O'Tooley: " + str(round((otooley/total)*100, 3)) + "% (" + str(otooley) +")")
print("------------------------")

print("Winner: " + max(d2.items(), key = operator.itemgetter(1))[0])
print("------------------------")


# PRINT TO TEXT FILE

import sys  # Need to have acces to sys.stdout
fd = open('output.txt','w') # open the result file in write mode
old_stdout = sys.stdout   # store the default system handler to be able to restore it
sys.stdout = fd # Now your file is used by print as destination 

# PyBank

filepath = os.path.join("Resources", "budget_data.csv")

d = {}
change = {}
past_month = 0
cur_month = 0
diff = 0
total = 0

print("Financial Analysis")
print("-----------------------")

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
        
print("Total Months: " + str(len(d)))

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total += int(row[1])
        
print("Total: $" + str(total))

avg_total = 0
for key, value in change.items():
    avg_total += value
    
print("Average Change: $" + str(round(avg_total/85, 2)))

maxvalue = max(change.values())
for m in change.keys(): 
    if change[m] == maxvalue:
        print ("Greatest Increase in Profits: " + m + " ($" + str(change[m]) +")")


minvalue = min(change.values())
for k in change.keys(): 
    if change[k] == minvalue:
        print ("Greatest Decrease in Profits: " + k + " ($" + str(change[k]) +")")

print(" ")
        
# PyPoll

filepath = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("------------------------")

names = []

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        names.append(row[2])
        
total = len(names)
print("Total Votes: " + str(total))
print("------------------------")

from collections import Counter

d = Counter(names)

from collections import defaultdict

d2 = dict(d)

khan = d['Khan']
correy = d['Correy']
li = d['Li']
otooley = d["O'Tooley"]

print("Khan: " + str(round((khan/total)*100, 3)) + "% (" + str(khan) +")")
print("Correy: " + str(round((correy/total)*100, 3)) + "% (" + str(correy) +")")
print("Li: " + str(round((li/total)*100, 3)) + "% (" + str(li) +")")
print("O'Tooley: " + str(round((otooley/total)*100, 3)) + "% (" + str(otooley) +")")
print("------------------------")

print("Winner: " + max(d2.items(), key = operator.itemgetter(1))[0])
print("------------------------")

fd.close()