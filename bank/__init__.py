from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

#202212
#from flask import session
#from flask_session import Session


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
#db = "dbname='bluechip' user='postgres' host='127.0.0.1' password = '6090'"
db = "dbname='bluechip' user='postgres' host='127.0.0.1' password = '6090'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#202212
# Check Configuration section for more details
#SESSION_TYPE = 'filesystem'


#202212
roles = ["ingen","employee","customer"]
print(roles)
mysession = {"state" : "initializing","role" : "Not assigned", "id": 0 ,"age" : 202212}
print(mysession)

from bank.Login.routes import Login
from bank.Customer.routes import Customer

app.register_blueprint(Login)
app.register_blueprint(Customer)


#from bank import routes
