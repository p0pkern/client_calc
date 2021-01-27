# client_calc
Pulls data from a csv file from our timeclock and calculates head count, average wage, average bill rate per employee, and total amount spend on employees for the week.

#Purpose
The time keeping system we use currently only allows the input of an employee name, a 'pin' where the employee clocks in and out, and a single field to put a dollar value. For our internal accuracy we put the employees bill rate in the entry field. We were approached to provide a break down of certain data points that were not easily achieved through our internal database or timeclock on a weekly basis.
They were:
  > Head Count - Total number of employees who worked the previous week for any hours.
  > Average Wage - An average of what each employee earned.
  > Avereage Spend - The average bill rate chareged to the client per employee hour.
  > Total Spend - The total bill rate for the week.
  
Reading a csv file the following calculations are made
  > Head Count - Total length of employees in the csv file, simple total
  > Average Wage - Each wage from the bill rate column is divided by the internal bill rate and then the average is calculated with the employee head count.
  > Average Spend - The average wage from the bill rate
  > Total Spend - Caclulated total of all hours the employees worked summed together(provided in the csv)
  
## Usage
Since the program has very low requirements it is procedural.
> Run in terminal:
> $Python3 client_calc.py

## Future Updates
- Make the files an external data input
