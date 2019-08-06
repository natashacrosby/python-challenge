# find total numbr of months in dataset
import os
import csv


csvpath = "budget_data.csv"

net_total = 0
months = 0
averagechange = 0
increaseprofit = 0
decreaseloss = 0 
i = 0
previousval = 0
current = 0
run = 0



with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    next(csvreader, None)
    previousval = -1

    for row in csvreader:
        if int(row[1]) >= increaseprofit:
            increaseprofit = int(row[1])
            date1 = str(row[0])

        if int(row[1]) <= decreaseloss:
            decreaseloss = int(row[1])
            date2 = str(row[0])

        net_total = int(net_total) + int(row[1])
        months = months + 1

#While loop to find the monthly change
        while i <= months:
            previousval = current
            current = int(row[1])
            run = run + (current - previousval)
            i =i + 1

        averagechange = run / months 

		
print("Financial Analysis")
print("-------------------")
print("Total months: " + str(months))
print("Total Revenue: $" + str(net_total))
print("Average Revenue Change: $" + str(round(averagechange)))
print("Greatest Increase in Revenue: $" + f"{increaseprofit} " + date1)
print("Greatest Decrease in Losses: $" + f"{decreaseloss} " + date2)