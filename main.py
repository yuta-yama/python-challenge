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

print("Financial Analysis", file=open("output.txt", "a"))
print("-----------------------", file=open("output.txt", "a"))

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
        
print("Total Months: " + str(len(d)), file=open("output.txt", "a"))

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total += int(row[1])
        
print("Total: $" + str(total), file=open("output.txt", "a"))

avg_total = 0
for key, value in change.items():
    avg_total += value
    
print("Average Change: $" + str(round(avg_total/85, 2)), file=open("output.txt", "a"))

maxvalue = max(change.values())
for m in change.keys(): 
    if change[m] == maxvalue:
        print ("Greatest Increase in Profits: " + m + " ($" + str(change[m]) +")", file=open("output.txt", "a"))


minvalue = min(change.values())
for k in change.keys(): 
    if change[k] == minvalue:
        print ("Greatest Decrease in Profits: " + k + " ($" + str(change[k]) +")", file=open("output.txt", "a"))

print(" ", file=open("output.txt", "a"))
        
# PyPoll

filepath = os.path.join("Resources", "election_data.csv")

print("Election Results", file=open("output.txt", "a"))
print("------------------------", file=open("output.txt", "a"))

names = []

with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        names.append(row[2])
        
total = len(names)
print("Total Votes: " + str(total), file=open("output.txt", "a"))
print("------------------------", file=open("output.txt", "a"))

from collections import Counter

d = Counter(names)

from collections import defaultdict

d2 = dict(d)

khan = d['Khan']
correy = d['Correy']
li = d['Li']
otooley = d["O'Tooley"]

print("Khan: " + str(round((khan/total)*100, 3)) + "% (" + str(khan) +")", file=open("output.txt", "a"))
print("Correy: " + str(round((correy/total)*100, 3)) + "% (" + str(correy) +")", file=open("output.txt", "a"))
print("Li: " + str(round((li/total)*100, 3)) + "% (" + str(li) +")", file=open("output.txt", "a"))
print("O'Tooley: " + str(round((otooley/total)*100, 3)) + "% (" + str(otooley) +")", file=open("output.txt", "a"))
print("------------------------", file=open("output.txt", "a"))

print("Winner: " + max(d2.items(), key = operator.itemgetter(1))[0], file=open("output.txt", "a"))
print("------------------------", file=open("output.txt", "a"))