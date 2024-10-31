from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/grades.html')
def grades():
    return render_template('grades.html')

@app.route('/loans.html')
def loans():
    return render_template('loans.html')

@app.route('/loan_detail.html')
def loan_detail():
    return render_template('loan_detail.html')

