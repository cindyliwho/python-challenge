import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)
    print(f"csv header: {csv_header}")


    months = 0
    netTotal = 0
    prevAmount = 0
    currChange = 0
    changeDict = {}
    for row in csvreader:
        netTotal = netTotal + int(row[1])
        if months == 0:
            prevAmount = int(row[1])

        else: 
            currChange = int(row[1]) - prevAmount
            changeDict.update({row[0] : currChange})
            prevAmount = int(row[1])
           
        months = months + 1
    sum = 0
    max = 0
    maxDate = ""
    min = 0
    minDate = ""
    for date in changeDict: 
        sum = sum + changeDict[date]
        if changeDict[date] > max: 
            max = changeDict[date]
            maxDate = date

        if changeDict[date] < min:
                min = changeDict[date]
                minDate = date

    changes = sum/len(changeDict)

with open('analysis/summary.txt', 'w') as f:
     f.write(f"Financial Analysis \n ------------------------- \n Total Months: {months} \n Total: ${netTotal} \n Average Change: ${'%.2f' % changes} \n Greatest Increase in Profits: {maxDate} (${max})\n Greatest Decrease in Profits: {minDate} (${min}))")

print(f"Financial Analysis \n ------------------------- \n Total Months: {months} \n Total: ${netTotal} \n Average Change: ${'%.2f' % changes} \n Greatest Increase in Profits: {maxDate} (${max})\n Greatest Decrease in Profits: {minDate} (${min})")
