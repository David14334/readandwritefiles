import csv

employees = open('EmployeePay.csv','r')

employee_file = csv.reader(employees, delimiter=',')


next(employee_file)

total_pay= 0


for record in employee_file:
        bonus= float(record[3]) * float(record[4])
        total_pay = float(record[3]) * bonus

        print("FName:", record[1])
        print("LName:", record[2])
        print("Salary:", "${:,.2f}".format(float(record[3]))
        print("Bonus:", "${:,.2f}".format(bonus)
        print("Total Pay:","${:,.2f}".format(total_pay)
