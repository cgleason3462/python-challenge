import os
import csv

#route to correct csv
pollData = os.path.join("..", "election_data.csv")
txtFile = "Poll_data.txt"

#Open csv data
with open(pollData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #Create lists to store data from csv
    totalVotes = []
    candidateList = []
    uniqueCandidates = []
    percentageVotes = []
    
    for row in csvreader:
       
        #Store votes column in totalVotes list
        totalVotes.append(row[0])
        
        #find the length of the column to determine how many votes were cast
        Total = len(totalVotes)
        
        #Populate list with the candidate column
        candidateList.append(row[2])
        
    for i in set(candidateList):
        
        #Store rows from candidateList into uniqueCandidates list
        uniqueCandidates.append(i)
        
        #Count the the amount of votes per candidate
        y = candidateList.count(i)
        
        #Find and round the percentage of votes per candidate
        x = round((y / Total) * 100)
        
        #Populate the percentage list with the accurate percentages per candidate
        percentageVotes.append(x)
    
    def most_Voted(candidateList):
    
        #returns the candidate with the most votes
        return max(set(candidateList), key = candidateList.count)
        
        #the list the function will draw from
        candidateList = []
        
        #print most voted for candidate
        print(most_Voted(candidateList))
    
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {Total}')
    print("-------------------------")
    #loop through list and print the percentage and total for each candidate that recevied votes
    for x in range(len(uniqueCandidates)):
       print(uniqueCandidates[x] + ": " + str(percentageVotes[x]) +"% (" + str(totalVotes[x])+ ")")
    print("-------------------------")
    print(f'Winner: {most_Voted(candidateList)}')
    print("-------------------------")
    
with open(txtFile, "w") as text:
    
    text.write("Election Results")
    text.write("\n-------------------------")
    text.write(f'\nTotal Votes: {Total}')
    text.write("\n-------------------------")
    for x in range(len(uniqueCandidates)):
       text.write(uniqueCandidates[x] + ": " + str(percentageVotes[x]) +"% (" + str(totalVotes[x])+ ")")
    text.write("\n-------------------------")
    text.write(f'\nWinner: {most_Voted(candidateList)}')
    text.write("\n-------------------------")
