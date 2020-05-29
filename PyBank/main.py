import os
import csv

#route to the correct file
bankData = os.path.join("..", "budget_data_copy.csv")

#Declare file we will write results to
txtFile = "Bank_data.txt"

#Open Csv file
with open(bankData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #Declare lists
    revList = []
    months = []
    numberRows = 0
    averageChange = []
    
    #Loop through csv
    for row in csvreader:
        
        #Populate list with profit/losses
        revList.append(float(row[1]))
        
        #Set revenue total equal to the total of the revList
        revenue = sum(revList)
        
        #Populate months list with the months column values
        months.append(row[0])
        
        #Find the total length of the date column whic is equal to total months
        monthsTotal = len(months)
    
    #Loop through each value after the first in revList
    for x in range(1,len(revList)):
        
        #populate averageChange with the differences between each value
        averageChange.append(revList[x] - revList[x - 1])
        
        #Take the sum of averageChange list and divide it by the lenghth to find average change over the entire data set
        avgChange = sum(averageChange)/len(averageChange)
        
        #Find the max amount of profit
        maxProfit = max(averageChange)
        
        #Find the most money lost
        minLoss = min(averageChange)
        
    #Print results
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {monthsTotal}")
    print(f"Total: ${revenue}")
    print(f"Average Change: ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: ${maxProfit}")
    print(f"Greatest Decrease in Profits: ${minLoss}")

#Open text file
with open(txtFile, "w") as text:
    
    #Write results to text file
    text.write("Financial Analysis")
    text.write("\n---------------------------------")
    text.write(f"\nTotal Months: {monthsTotal}")
    text.write(f"\nTotal: ${revenue}")
    text.write(f"\nAverage Change: ${round(avgChange,2)}")
    text.write(f"\nGreatest Increase in Profits: ${maxProfit}")
    text.write(f"\nGreatest Decrease in Profits: ${minLoss}")

