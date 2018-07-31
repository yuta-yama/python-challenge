import os
import csv

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