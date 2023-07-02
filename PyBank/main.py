#import os module
import os
from pathlib import Path

#Import module for reading CSV files
import csv

#Set path for csv data file
csvpath = Path("Resources/budget_data.csv")

#Open and read csv data file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    csv_header = next(csvfile)
    print(f"csv_header: {csv_header}")

    #Find number of months and net profit/loss
    Months = []
    NetProfit = []
    for rows in csvreader:
        Months.append(rows[0])
        NetProfit.append(int(rows[1]))
        Total_Months = len(Months)

    #Calculate monthly profit change
    ProfitChange = []
    for i in range(1,len(NetProfit)):
        ProfitChange.append((int(NetProfit[i]))-int(NetProfit[i-1]))

    #Calculate average change in Profit/Losses
    average_change = sum(ProfitChange)/len(ProfitChange)
   
    #Calculate greatest increase and decrease of monthly profit change
    GreatestIncrease = max(ProfitChange)
    GreatestDecrease = min(ProfitChange).

    #return data found
    print("Financial Analysis")
    print("----------------------------")
    print ("Total Months: ", str(Total_Months))
    print ("Total Profit: ", f"${sum(NetProfit):,}")
    print ("Average Change: ", f"${average_change:,.2f}")
    print ("Greatest Increase in Profits: ",str(Months[ProfitChange.index(max(ProfitChange))+1])," ",f"${GreatestIncrease:,}")
    print ("Greatest Decrease in Profits: ",str(Months[ProfitChange.index(min(ProfitChange))+1])," ",f"${GreatestDecrease:,}")

    #Export data found to a text file
    file = open("analysis/output.txt","w")
    file.write("Financial Analysis"+"\n")
    file.write("----------------------------"+"\n")
    file.write ("Total Months: "+ str(Total_Months)+ "\n")
    file.write ("Total Profit: "+ f"${sum(NetProfit):,}"+"\n")
    file.write ("Average Change: "+ f"${average_change:,.2f}"+"\n")
    file.write ("Greatest Increase in Profits: "+str(Months[ProfitChange.index(max(ProfitChange))+1])+" "+f"(${GreatestIncrease:,})"+"\n")
    file.write ("Greatest Decrease in Profits: "+str(Months[ProfitChange.index(min(ProfitChange))+1])+" "+f"(${GreatestDecrease:,})"+"\n")
    file.close()

      