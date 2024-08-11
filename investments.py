def calculate_future_value(investment_money, loan_amount, loan_interest_rate, minimum_payment, current_age, retirement_age, annual_rate_of_return):
    # Calculate the monthly interest rate
    monthly_loan_interest_rate = loan_interest_rate / 12

    # Initialize variables for both scenarios
    total_balance_invest = 0
    total_balance_pay_off_loans = 0

    # Iterate from current_age to retirement_age
    for age in range(current_age, retirement_age):
        # Scenario 1: Minimum loan payments and invest the rest
        if investment_money > minimum_payment:
            interest_earned = (total_balance_invest + investment_money - minimum_payment) * (annual_rate_of_return / 12)
            total_balance_invest = total_balance_invest + investment_money - minimum_payment + interest_earned

        # Scenario 2: Apply all money towards loans before making investments
        loan_interest = loan_amount * monthly_loan_interest_rate
        loan_amount = loan_amount + loan_interest - minimum_payment
        total_balance_pay_off_loans += investment_money - minimum_payment

        # Check if the loan is paid off before retirement
        if loan_amount <= 0:
            break

    # Determine which scenario is more beneficial
    if total_balance_invest > total_balance_pay_off_loans:
        return "You should only make the minimum payments on your loan and apply the rest towards retirement."
    elif total_balance_invest < total_balance_pay_off_loans:
        return "You should apply all ${:.2f} towards your loan before making any investments.".format(investment_money)
    else:
        return "Both scenarios result in the same amount of money."

# Input validation and data gathering
while True:
    try:
        investment_money = float(input("Enter how much money you will be putting towards loans/retirement each month: "))
        loan_amount = float(input("Enter how much you owe in loans: "))
        loan_interest_rate = float(input("Enter the annual interest rate of the loans: "))
        minimum_payment = float(input("Enter your minimum monthly loan payment: "))
        current_age = int(input("Enter your current age: "))
        retirement_age = int(input("Enter the age you plan to retire at: "))
        annual_rate_of_return = float(input("Enter the annual rate of return you predict for your investments: "))
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        continue

    if investment_money < minimum_payment:
        print("The investment money should be greater than or equal to the minimum payment.")
    else:
        break

# Calculate and print the recommendation
recommendation = calculate_future_value(investment_money, loan_amount, loan_interest_rate, minimum_payment, current_age, retirement_age, annual_rate_of_return)
print(recommendation)