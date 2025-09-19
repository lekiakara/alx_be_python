# Define user input variables

monthly_income = 5000
total_monthly_expenses = 4000

# User input for financial details

monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculate monthly savings

monthly_savings = monthly_income - total_monthly_expenses
print("Your monthly savings are $:", monthly_savings)

# Projected annual savings

simple_interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


print("Projected savings after one year, with interest, is:", projected_savings)


