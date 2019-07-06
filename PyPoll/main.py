import os
import csv

# Create csv file path
filename = 'election_data.csv'
filepath = os.path.join('Resources',filename)

# Open and read csv file
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    voterId = []
    county = []
    candidates = []
    
    # Read the csv file row by row
    for row in csvreader:
        voterId.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
    # Remove headers from entries
    voterId.pop(0)
    county.pop(0)
    candidates.pop(0)
    
    # Total number of votes cast
    numVotes = len(voterId)
    
    # Unique list of candidates receiving votes
    def unique(list):
        unilist = []
        for entry in list:
            if entry not in unilist:
                unilist.append(entry)
        return unilist
    
    uniCand = unique(candidates)
    
    line1 = 'Election Results'
    line2 = '-----------------------------'
    line3 = f'Total Votes: {numVotes}'
    line4 = '-----------------------------'
    
    # Find total number of votes and percent of vote won by each candidate
    numVoteList = []
    perList = []
    for entry in uniCand:
        votesCand = candidates.count(entry)
        percCand = (votesCand/numVotes)*100
        perList.append(percCand)
        numVoteList.append(votesCand)
    
    lines5 = []
    
    for x in range(len(uniCand)):
        lines5.append(f'{uniCand[x]}: %{round(perList[x],3)} ({numVoteList[x]})')
    
    # Decide winner of election
    maxloc = numVoteList.index(max(numVoteList))
    
    # Print results
    line6 = '-----------------------------'
    line7 = f'Winner: {uniCand[maxloc]}'
    line8 = '-----------------------------'
    
    # Print in terminal
    summary = []
    summary2 = []
    summary.extend([line1,line2,line3,line4])    
    print('')
    for line in summary:
        print(line)
    for line in lines5:
        print(line)
    summary2.extend([line6, line7,line8])
    for line in summary2:
        print(line)
    print('')    
    
    # Save results to a text file
    outputpath = filename.split('.')[0] + '_output.txt'
    with open(outputpath,'w') as fileOut:
        for line in summary:
            fileOut.write(line + '\n')  
        for line in lines5:
            fileOut.write(line + '\n')
        for line in summary2:
            fileOut.write(line + '\n')
