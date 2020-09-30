#create variable for all financial info
savings = 500
monthy_income = 2000
annual_income = monthy_income * 12
monthy_expenses = 1000
annual_expenses = monthy_expenses * 12

print("Year 1")
print("---------------")
print(f'Savings: {savings}')
print (f'Month expenses: {monthy_expenses}')
print (f'Annual epenses: {annual_expenses}')
print (f'Monthy Income: {monthly_income}')
print(f'Annual Income: {annual_income}')

savings -= 400
monthy_expenses -= 500
monthly_income += 1000
annual_expenses = monthy_expenses * 12
annual_income = monthy_expenses * 12

print("")
print("Year 2")
print("---------------")
print(f'Savings: {savings}')
print (f'Month expenses: {monthy_expenses}')
print (f'Annual expenses: {annual_expenses}')
print (f'Monthy Income: {monthly_income}')
print(f'Annual Income: {annual_income}')