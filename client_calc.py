"""
Author: Chris Peterman
Name: Client_Calc
Description: One of our clients needed specific data from our employee timeclock. The only issue is that the timeclock
only holds a certain amount of data. To remedy this I utilized the data points from the timeclock did calculations to
create the missing data points and then wrote them to an excel sheet. The data is pulled from a csv file.
"""

import csv
import xlwt

results = []

with open('report.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    head_count = 0
    line_count = 0

    avg_pay = 0
    avg_spend = 0
    total_spend = 0

    calc_bill = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            total = row[13].replace(',', '')
            pay_rate = (float(row[12]) / 1.32)
            total_bill = float(total)
            bill_rate = float(row[12])

            avg_pay += pay_rate
            avg_spend += bill_rate
            total_spend += total_bill

            head_count += 1

    results.append(head_count)
    results.append(round(avg_pay / head_count, 2))
    results.append(round(avg_spend / head_count, 2))
    results.append(round(total_spend, 2))

# Write to an Excel workbook
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Head_Count')

sheet.write(0, 0, 'Head Count')
sheet.write(0, 1, 'Average Wage')
sheet.write(0, 2, 'Average Spend')
sheet.write(0, 3, 'Total Spend')
sheet.write(1, 0, str(results[0]))
sheet.write(1, 1, str(results[1]))
sheet.write(1, 2, str(results[2]))
sheet.write(1, 3, str(results[3]))

workbook.save('report.xls')

