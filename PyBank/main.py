import os
import csv

# Path and file to open for analysis
Budget_csv = os.path.join('Resources', 'budget_data.csv')

#Define variables to be used during analysis
total_Months = 0
total = 0
previous_rev = 0
rev_change = 0
g_increase = 0
g_decrease = 0
change = []
avg_change = 0



#open file and define EOL
with open(Budget_csv, newline = '') as csvfile:
    #define file and delminiter
    csvreader = csv.reader(csvfile,delimiter=',')

    #used to skip the hearer row in the anlaysis
    next(csvreader, None)

    for row in csvreader:

        #increases Total Months by 1 and overall total by new total
        total_Months = total_Months + 1
        total = total + int(row[1])

        if total_Months > 1: #needed to exclude first months value in the revenue change analysis
            #Calculate Revenue change for the month
            rev_change = int(row[1]) - previous_rev
            #Track Revenue changes for average value
            change.append(rev_change)
            #print(str(total_Months) + " - " + str(rev_change))

            #determine greatest increase and decrese in revenue
            if rev_change > g_increase:
                g_increase = rev_change
                inc_month = row[0]
            
            if rev_change < g_decrease:
                g_decrease = rev_change
                dec_month = row[0]

        previous_rev = int(row[1])



#output results to the terminal
avg_change = sum(change)/len(change)
print('Financial Analysis')
print('----------------------------')
print ('Total Months: ' + str(total_Months))
print ('Total: $' + (format(total, ",.2f"))) #format total with commas and decimal
print ('Average Change: $' + (format(avg_change, ",.2f")))
print('Greatest Increase in Profits: ' + inc_month + ' ($' + (format(g_increase, ",.2f")) + ')')
print('Greatest Decrease in Profits: ' + dec_month + ' ($' + (format(g_decrease, ",.2f")) + ')')


#same as above, but write results to text file
f = open("results.txt", "a")
f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write('Total Months: ' + str(total_Months) + '\n')
f.write ('Total: $' + (format(total, ",.2f")) + '\n') #format total with commas and decimal
f.write ('Average Change: $' + (format(avg_change, ",.2f")) + '\n')
f.write('Greatest Increase in Profits: ' + inc_month + ' ($' + (format(g_increase, ",.2f")) + ') \n')
f.write('Greatest Decrease in Profits: ' + dec_month + ' ($' + (format(g_decrease, ",.2f")) + ') \n')
f.close()