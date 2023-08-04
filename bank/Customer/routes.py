from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import TradeForm
from flask_login import current_user
from bank.models import select_investments, markets, execute_order



import sys, datetime

#202212
# roles is defined in the init-file
from bank import roles, mysession

iEmployee = 1
iCustomer = 2


Customer = Blueprint('Customer', __name__)


@Customer.route("/trade", methods=['GET', 'POST'])
def trade():
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))

    user_id = current_user.get_id()
    market_data = markets()

    #forms = [TradeForm(market_data[0][i]) for i in range(len(market_data))] 

    form = TradeForm()

    if form.is_submitted():
        execute_order(form,user_id)    
        

    return render_template('trade.html', title='Trade', market_data=market_data, form=form)

@Customer.route("/portfolio", methods=['GET', 'POST'])
def portfolio():

    #202212
    # Her laves et login check
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))

    mysession["state"]="invest"
    print(mysession)
    user_id = current_user.get_id()
    inv = select_investments(user_id)

    
    return render_template('portfolio.html', title='Investments', inv=inv)


