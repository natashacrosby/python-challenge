# find total numbr of months in dataset
import os
import csv


csvpath = "budget_data.csv"

net_total = 0
months = []
averagechange = 0
increaseprofit = 0
decreaseloss = 0 
i = 0
before = 0
current = 0
play = 0



with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    next(csvreader, None)
    previousval = -1

    for row in csvreader:
        print(row)

        currentval = int(row[1])
        change = currentval - previousval
        previousval = currentval
    
        increaseprofit = [int(row[1]) >= increaseprofit for row in csvreader]  
        decreaseloss = [int(row[1]) <= decreaseloss for row in csvreader]

        months.append(row)
        net_total = str(net_total) + str(row[1])
        date1 = str(row[0])
        date2 = str(row[0])



print("Financial Analysis")
print("-------------------")
print("Total months: " + str(len(months)))
print("Total Revenue: $" + str(net_total))
print("Average Revenue Change: $" + str(round(averagechange)))
print("Greatest Increase in Revenue: $" + f"{increaseprofit} " + date1)
print("Greatest Decrease in Losses: $" + f"{decreaseloss} " + date2)