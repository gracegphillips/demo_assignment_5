from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db
from ..functions import calculate_amortization
from ..functions import calculate_monthly_interest_rate

loan_amortization_detail = Blueprint('loan_amortization_detail', __name__)

@loan_amortization_detail.route('/loan_detail/<int:loan_info_id>')
def loan_detail(loan_info_id):
    db = get_db()
    cursor = db.cursor()

    # Fetch the loan details using the loan_info_id
    cursor.execute('SELECT loan_amount, interest_rate, term_years FROM loan_info WHERE loan_info_id = %s', (loan_info_id,))
    loan_data = cursor.fetchone()

    # Convert the fetched data to the appropriate types
    loan_amount = float(loan_data['loan_amount'])  # Convert loan_amount from Decimal to float
    interest_rate = float(loan_data['interest_rate'])  # Convert interest_rate from Decimal to float
    loan_term_months = int(loan_data['term_years'])  # Convert loan_term_moths to int


    # Call the calculate_amortization function to get the monthly payment
    monthly_payment = calculate_amortization(loan_amount, interest_rate, loan_term_months)
    monthly_interest_rate = calculate_monthly_interest_rate(interest_rate)

    # Create a list to store the loan amortization details
    loan_amortization_list = []

    # Loop to calculate the loan amortization details for each month
    for i in range(1, loan_term_months + 1):
        interest_paid = loan_amount * monthly_interest_rate  # Calculate interest paid for the current month
        principal_paid = monthly_payment - interest_paid  # Calculate principal paid
        remaining_balance = loan_amount - principal_paid  # Calculate remaining balance after payment

        # Append the details for the current month
        loan_amortization_list.append({
            'month': i,
            'starting_balance': loan_amount,
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'monthly_payment': monthly_payment,
            'remaining_balance': remaining_balance
        })

        # Update the loan amount for the next month
        loan_amount = remaining_balance

    # Render the loan detail template and pass the amortization schedule
    return render_template('loan_detail.html', loan_schedule=loan_amortization_list, loan_id=loan_info_id)