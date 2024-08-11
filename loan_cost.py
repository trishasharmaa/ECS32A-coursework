#Program to calculate loan cost
def loan_cost():  #Creating a function
    amount_borrowed = float(input("Please enter the amount of money you borrowed: $"))  #Asking the user for principal amount(amount borrowed)
    annual_interest = float(input("Please enter the annual interest rate: "))         #Asking the user for the annual interest rate
    annual_interest_rounded = round(annual_interest, 2)                               #Rounding the annual interest rate
    monthly_interest = annual_interest_rounded/12                                     #Finding monthly interest rate by dividing annual rate by 12
    no_of_payments_months = int(input("Please enter the number of payments to be made: "))   #Asking the user for the no. of months the payments are to be made
    monthly_cost = amount_borrowed*monthly_interest/(1-((1+monthly_interest)**(-no_of_payments_months)))  #Finding the monthly cost
    total_cost = no_of_payments_months*monthly_cost    #Finding the total cost
    print(f"A loan of ${amount_borrowed:.2f} with an annual interest of {annual_interest:.2f} paid off over {no_of_payments_months} months will have monthly payments of ${monthly_cost:.2f}.")
    print(f"In total, you will pay ${total_cost:.2f}, making the cost of your loan ${total_cost - amount_borrowed:.2f}.")  #Printing the result

loan_cost()