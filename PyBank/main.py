import os
import csv
months = 0
profitloss = 0
max_profit = 0
max_loss = 0
monthly = []
month_names = []
diff = 0
csvpath = os.path.join("budget_data.csv")
with open (csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        months = months+1
        profitloss = profitloss + int(row[1])
        monthly.append(int(row[1]))
        month_names.append(row[0])
        

for i in range(1, len(monthly)):
    diff = diff + (monthly[i]-monthly[i-1])
    if max_profit < monthly[i]-monthly[i-1]:
        max_profit = monthly[i]-monthly[i-1]
        max_month = month_names[i]
    elif max_loss > monthly[i]-monthly[i-1]:
        max_loss = monthly[i]-monthly[i-1]
        min_month = month_names[i]

avg_profitloss = diff / (len(monthly)-1)

print("Financial Analysis")
print("________________________\n")
print(f"Total months: {months}")
print(f"Total: ${profitloss}")
print(f"Average Change: ${round(avg_profitloss,2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_month} (${max_loss})")


output_path = os.path.join("budget_results.txt")
with open(output_path, "w", newline='') as csvfile:
    csvfile.write("Financial Analysis\n")
    csvfile.write("__________________________\n\n")
    csvfile.write(f"Total months: {months}\n")
    csvfile.write(f"Total: ${profitloss} \n")
    csvfile.write(f"Average Change: ${round(avg_profitloss,2)}\n")
    csvfile.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
    csvfile.write(f"Greatest Decrease in Profits: {min_month} (${max_loss})\n")


