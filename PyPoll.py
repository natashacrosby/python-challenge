import os
import csv



csvpath = "election_data.csv"

votes = 0
candidates = []
vote_count = {}
vote_percent = {}

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    #COUNT VOTES + LIST CANDIDATES
    for row in csvreader:
        
        votes = votes + 1        

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

    #CALCULATE PERCENTAGE OF VOTES
    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"
    
    #FIND WINNER
    maxi = max(vote_count.keys(), key=(lambda k: vote_count[k]))    
    
    #MAKE VARIABLES FOR PRINTING RESULTS
    space = "-------------------------------"
    results1 = (
        "Election Results" + '\n' + space + '\n' + "Total Votes: "+ str(votes)+ '\n' + space + '\n')
    results2 = (
        space + '\n'
        "Winner: "+ str(maxi)+ '\n' + space + '\n')
   
   #PRINT RESULTS
    print(results1)
    for key, val in vote_percent.items():
        print(key, ": ", val)
    print(results2)
    
    #CREATE TEXT FILE
    f = open("Election_results.txt", "w")

    f.write(results1)
    for key, val in vote_percent.items():
         f.write((key + ": " + val)+ '\n')
    f.write(results2)
    
    f.close()