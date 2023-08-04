# write all your SQL queries in this file.
from datetime import datetime
from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql
import random 

@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()

    schema = 'investors'
    id = 'user_id'
    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))
    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return Investors(cur.fetchone())
    else:
        return None


class Investors(tuple, UserMixin):
    def __init__(self, user_data):
        self.user_ID = user_data[0]
        self.password = user_data[1]

    def get_id(self):
       return (self.user_ID)



class Transfers(tuple):
    def __init__(self, user_data):
        self.id = user_data[0]
        self.amount = user_data[1]
        self.transfer_date = user_data[2]


def select_Investors(user_id):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Investors
    WHERE user_ID = %s
    """
    cur.execute(sql, (user_id,))
    user = Investors(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def select_investments(user_id):
    cur = conn.cursor()
    sql = """
    SELECT i.ticker_symbol, quantity, purchase_price, current_price, (current_price - purchase_price)*quantity AS profit
    FROM portfolios i
    JOIN market a ON i.ticker_symbol = a.ticker_symbol 
    WHERE user_ID = %s
    ORDER BY profit DESC
    """
    cur.execute(sql, (user_id,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def markets():
    cur = conn.cursor()
    sql = """
    SELECT *
    FROM market
    """
    cur.execute(sql)
    tuple_resultset = cur.fetchall()
    cur.close()
    print(tuple_resultset)
    return tuple_resultset 

def get_price(ticker_symbol):
    cur = conn.cursor()
    sql = """
    SELECT current_price
    FROM market
    WHERE ticker_symbol= %s
    """
    cur.execute(sql, (ticker_symbol,))
    tuple_resultset = cur.fetchall()
    cur.close()
    print(tuple_resultset)
    return tuple_resultset[0][0] 


def execute_order(order,user_id): 
    ticker_symbol = order.ticker.data
    quantity = order.quantity.data
    if order.buy.data:
        buy = True
    else:
        sell = True
    cur = conn.cursor()
    sql = """
    INSERT INTO Portfolios(record_ID, user_ID, ticker_symbol, purchase_price, quantity)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    cur.execute(sql, (random.randint(5000, 10**8), user_id, ticker_symbol, get_price(ticker_symbol), quantity))
    conn.commit()
    cur.close()