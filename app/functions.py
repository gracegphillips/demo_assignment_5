

###### grades

def calculate_grade(number_grade):
    if number_grade >= 90:
        letter_grade = 'A'
    elif number_grade >= 80:
        letter_grade =  'B'
    elif number_grade >= 70:
        letter_grade =  'C'
    elif number_grade >= 60:
        letter_grade =  'D'
    else:
        letter_grade =  'F'
    return letter_grade


###### loan amortization

def loan_amortization(monthly_interest_rate, loan_term_months, loan_amount, interest_rate, loan_term_years):
    loan_term_months = loan_term_years * 12  # Convert loan term to months
    monthly_interest_rate = interest_rate / 12 / 100  # Calculate monthly interest rate

    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months
    return monthly_payment


####Test cases

#Test calculate_grade function
print("Testing calculate_grade function:")
print(f"Grade for 95: {calculate_grade(95)}")  # Expected output: A
print(f"Grade for 85: {calculate_grade(85)}")  # Expected output: B
print(f"Grade for 75: {calculate_grade(75)}")  # Expected output: C
print(f"Grade for 65: {calculate_grade(65)}")  # Expected output: D
print(f"Grade for 55: {calculate_grade(55)}")  # Expected output: F


# Test loan_amortization function
print("\nTesting loan_amortization function:")
monthly_interest_rate = 0.05 / 12  # 5% annual interest rate
loan_term_months = 30 * 12  # 30 years
loan_amount = 300000  # $300,000 loan

monthly_payment = loan_amortization(monthly_interest_rate, loan_term_months, loan_amount, 5, 30)
print(f"Monthly payment for a $300,000 loan at 5% interest over 30 years: {monthly_payment:.2f}")