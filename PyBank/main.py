import os
import csv

bankData = os.path.join("..", "budget_data_copy.csv")

with open(bankData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    revList = []
    months = []
    numberRows = 0
    averageChange = []
    
    for row in csvreader:
        revList.append(float(row[1]))
        revenue = sum(revList)
        
        months.append(row[0])
        monthsTotal = len(months)
        
    for x in range(1,len(revList)):
        averageChange.append(revList[x] - revList[x - 1])
        avgChange = sum(averageChange)/len(averageChange)
        maxProfit = max(averageChange)
        minLoss = min(averageChange)
        
    
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {monthsTotal}")
    print(f"Total: ${revenue}")
    print(f"Average Change: ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: ${maxProfit}")
    print(f"Greatest Decrease in Profits: ${minLoss}")
    



