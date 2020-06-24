
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    #First line in csv file is a header, so extract it in csv_header list
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # initialize variable month_count to hold the number of months in the dataset
    month_count = 0
    # initialize variable net_profit_loss to hold the net profit/loss in the dataset
    net_profit_loss = 0
    # initialize variable avg_profit_loss to hold the avg change of profit/loss in the dataset
    avg_profit_loss = 0
    avg_change_profit_loss = 0.00
    # initialize variable change_in_profit_loss to hold the change of profit/loss of each month in the dataset
    change_in_profit_loss = 0
    net_change_profit_loss = 0
    # initialize variable greatest_profit to hold the biggest profit change month in the dataset
    greatest_profit = 0
    row_with_greatest_profit = [0,0,0]
    # initialize variable greatest_loss to hold the biggest loss change month in the dataset
    greatest_loss = 0
    row_with_greatest_loss = [0,0,0]

    last_month_value = 0
 

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        month_count += 1
        if last_month_value == 0:
            last_month_value = int(row[1])
        change_in_profit_loss = int(row[1]) - last_month_value
        last_month_value = int(row[1])
        row.append(change_in_profit_loss)
        #print(row)
        net_profit_loss += int(row[1])
        net_change_profit_loss += int(row[2])  

        if int(row[2]) > greatest_profit:
            greatest_profit = row[2]
            row_with_greatest_profit = row
        elif int(row[2]) < greatest_loss:
            greatest_loss  = row[2]
            row_with_greatest_loss = row

    avg_profit_loss = net_profit_loss/month_count
    avg_change_profit_loss = float(net_change_profit_loss/(month_count-1))

    net_profit_loss = '${:,.2f}'.format(net_profit_loss)
    avg_change_profit_loss = '${:,.2f}'.format(avg_change_profit_loss)

    #Print results to console
    print("============================================================")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PyBank ~~~~~~~~~~~~~~~~~~~~~~~~")
    print("============================================================")
    print(f"Total Number of Months in the dataset: {month_count}")
    print(f"Total Net Profit/Loss in the dataset:  {net_profit_loss}")
    print(f"Average Change in Profit/Loss:         {avg_change_profit_loss}")
    print(f"Greatest Profit [Month/Amount]:        {row_with_greatest_profit[0]},(${row_with_greatest_profit[2]})")
    print(f"Greatest Loss [Month/Amount]:          {row_with_greatest_loss[0]}, (${row_with_greatest_loss[2]})")
    print("============================================================")

 # Specify the file to write to
output_path = os.path.join(".", "analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text:
    text.write("============================================================\n")
    text.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PyBank ~~~~~~~~~~~~~~~~~~~~~~~~\n")
    text.write("============================================================\n")
    text.write("Total Number of Months in the dataset: " + "%i" %(month_count) + "\n")
    text.write("Average Change in Profit/Loss:         "+ str(avg_change_profit_loss) + "\n")
    text.write("Average Change in Profit/Loss:         "+ str(avg_change_profit_loss) + "\n")
    text.write("Greatest Profit [Month/Amount]:        "+ str(row_with_greatest_profit[0]) +", ($"+ str(row_with_greatest_profit[2]) + ")\n")
    text.write("Greatest Loss [Month/Amount]:          "+ str(row_with_greatest_loss[0]) +", ($" + str(row_with_greatest_loss[2]) + ")\n")   
    text.write("============================================================\n")
    