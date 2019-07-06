import os
import csv

# Create csv file path
filename = 'budget_data.csv'
filepath = os.path.join('Resources',filename)

# Open and read csv file
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    date = []
    profloss = []
    
    # Read the csv row by row
    for row in csvreader:
        date.append(row[0])
        profloss.append(row[1])
    
    # Remove the headers from the entries    
    date.pop(0)
    profloss.pop(0)
    
    # Total number of months included in dataset
    totmonth = len(date)
    
    # Net total amount of Profits/Losses over all period
    proflossint = []
    for num in range(len(profloss)):
        proflossint.append(int(profloss[num]))
    totprofloss = sum(proflossint)    
    
    # Average, min, and max of Profits/Losses
    def avg(list):
        listsum = sum(list)
        listlen = len(list)
        return listsum/listlen

    avgprofloss = avg(proflossint)
    minprofloss = min(proflossint)
    maxprofloss = max(proflossint)
    
    # Find date corresponding to min/max
    mindate = date[proflossint.index(minprofloss)]
    maxdate = date[proflossint.index(maxprofloss)]
    
    # Time to print
    line1 = 'Financial Analysis'
    line2 = '------------------------------------'
    line3 = f'Total Months: {totmonth}'
    line4 = f'Total: ${totprofloss}'
    line5 = f'Average Change: ${round(avgprofloss,2)}'
    line6 = f'Greatest Increase in Profits: {maxdate} (${maxprofloss})'
    line7 = f'Greatest Decrease in Profits: {mindate} (${minprofloss})'
    
    # Print in terminal
    summary = []
    summary.extend([line1,line2,line3,line4,line5,line6,line7])    
    print('')
    for line in summary:
        print(line)
    print('')
    
    # Export to text file
    outputpath = filename.split('.')[0] + '_output.txt'
    with open(outputpath,'w') as fileOut:
        for line in summary:
            fileOut.write(line + '\n')