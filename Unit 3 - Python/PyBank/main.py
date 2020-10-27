import os
import csv

bank_csv=os.path.join("Resources", "Python_PyBank_Resources_budget_data.csv")

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

num_rows = 0
net_total = 0
mom_change=[]

with open(bank_csv, 'r') as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=',')
    header = next(csv_reader)
    first_row = next(csv_reader)
    prev_net = int(first_row[1])
    num_rows += 1
    net_total += prev_net  
    
    for row in csv_reader:
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        mom_change.append(net_change)
        num_rows += 1
        net_total += int(row[1])

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

average_change = round((sum(mom_change)/len(mom_change)),2)
    
print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change} ")
print(f"Greatest Increase in Profits: {greatest_increase[0]}  : (${str(greatest_increase[1])})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${str(greatest_decrease[1])})")


output_csv= os.path.join("PyBank","Analysis", "Bank_Output.csv")

with open(output_csv, 'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------'])
    csvwriter.writerow([f'Total Months: {num_rows}'])
    csvwriter.writerow([f'Total: {net_total}'])
    csvwriter.writerow([f'Average Change: {average_change}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase[0]}  : (${str(greatest_increase[1])})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease[0]} (${str(greatest_decrease[1])})'])
