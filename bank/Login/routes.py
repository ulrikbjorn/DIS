from flask import render_template, url_for, flash, redirect, request, Blueprint
from bank import app, conn, bcrypt
from bank.forms import CustomerLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from bank.models import Investors, select_Investors


from bank import roles, mysession
import sys

Login = Blueprint('Login', __name__)

posts = [{}]


@Login.route("/")
@Login.route("/home")
def home():
    #202212
    mysession["state"]="home or /"
    print(mysession)
    #202212
    role =  mysession["role"]
    print('role: '+ role)

    return render_template('home.html', posts=posts, role=role)


@Login.route("/about")
def about():
    #202212
    mysession["state"]="about"
    print(mysession)
    return render_template('about.html', title='About')


@Login.route("/login", methods=['GET', 'POST'])
def login():

    #202212
    mysession["state"]="login"
    print(mysession)
    role=None

    # jeg tror det her betyder at man er er logget på, men har redirected til login
    # så kald formen igen
    # men jeg forstår det ikke
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))

    
    form = CustomerLoginForm()

    # Først bekræft, at inputtet fra formen er gyldigt... (f.eks. ikke tomt)
    if form.validate_on_submit():

        

        #"202212"
        # her checkes noget som skulle være sessionsvariable, men som er en GET-parameter
        # implementeret af AL. Ideen er at teste på om det er et employee login
        # eller om det er et customer login.
        # betinget tildeling. Enten en employee - eller en customer instantieret
        # Skal muligvis laves om. Hvad hvis nu user ikke blir instantieret
        user = select_Investors(form.id.data)
    
        # Derefter tjek om hashet af adgangskoden passer med det fra databasen...
        # Her checkes om der er logget på
        if user != None and bcrypt.check_password_hash(user[1], form.password.data):

            mysession["role"] = roles[2] 
            mysession["id"] = form.id.data
            print(mysession)
            print(roles)

            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    #202212


    #202212
    role =  mysession["role"]
    print('role: '+ role)

    #return render_template('login.html', title='Login', is_employee=is_employee, form=form)
    return render_template('login.html', title='Login', is_employee=False, form=form, role=role   )
#teachers={{"id": str(1234), "name":"anders"},}
#data={"user_id": str(user_id), "total_trials":total_trials}

    #hvor gemmes login-bruger-id?

@Login.route("/logout")
def logout():
    #202212
    mysession["state"]="logout"
    print(mysession)

    logout_user()
    return redirect(url_for('Login.home'))


