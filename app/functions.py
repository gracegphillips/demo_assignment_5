

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

def calculate_amortization(loan_amount, interest_rate, loan_term_years):
    loan_term_months = loan_term_years * 12  # Convert loan term to months
    monthly_interest_rate = interest_rate / 12 / 100  # Calculate monthly interest rate

    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months))
    else:
        monthly_payment = loan_amount / loan_term_months
    return monthly_payment

def calculate_monthly_interest_rate(interest_rate):
    return interest_rate / 12 / 100