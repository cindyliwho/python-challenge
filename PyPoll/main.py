import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    #creates a vote dictionary, stores candidate name and corresponding number of votes. 
    #loops through the file, if name is not contained in the dictionary, add the name as a key and value + 1
    #if name already appears in the dictionary keys, simply add 1 to its value
    totalVotes = 0
    voteDict = {}
    for row in csvreader: 
        totalVotes = totalVotes + 1
        if row[2] not in voteDict.keys(): 
            voteDict[row[2]] = 1

        else: 
            voteDict[row[2]] = voteDict.get(row[2]) + 1


    #creates a percentage dictionary that stores the corresponding percentage of vote each candidate receives 
    #finds the candidate with the max vote, determines the winner
    percentageDict= {}
    maxVote = 0
    winner = ""
    for candidate in voteDict:
        percentage = (voteDict[candidate]/totalVotes)*100
        percentageDict[candidate] = percentage
        if voteDict[candidate] > maxVote:
            maxVote = voteDict[candidate]
            winner = candidate

    
    outputStr1 = list(voteDict)[0] + ": " + "%.3f" % percentageDict.get(list(voteDict)[0]) + "% (" + str(voteDict.get(list(voteDict)[0])) + ")"
    outputStr2 = list(voteDict)[1] + ": " + "%.3f" % percentageDict.get(list(voteDict)[1]) + "% (" + str(voteDict.get(list(voteDict)[1])) + ")"
    outputStr3 = list(voteDict)[2] + ": " + "%.3f" % percentageDict.get(list(voteDict)[2]) + "% (" + str(voteDict.get(list(voteDict)[2])) + ")"


with open('analysis/summary.txt', 'w') as f:
     f.write(f"Election Results \n ------------------------- \n Total Votes: {totalVotes} \n ------------------------- \n {outputStr1} \n {outputStr2} \n {outputStr3} \n ------------------------- \n Winner: {winner} \n -------------------------")

print(f"Election Results \n ------------------------- \n Total Votes: {totalVotes} \n ------------------------- \n {outputStr1} \n {outputStr2} \n {outputStr3} \n ------------------------- \n Winner: {winner} \n -------------------------")

