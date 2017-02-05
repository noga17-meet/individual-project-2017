from flask import *
from flask import session as login_session
from nogas_databases import *

app = Flask(__name__)
app.secret_key="this is my project"


engine = create_engine('sqlite:///.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
dbsession = DBSession()

def verify_password(email, password):
	user= session.query(User).filter_by(email=email).first()
	if not user or not user.verify_password(password):
		return False
	else:
		return True

@app.route('/')
def home_page():
	return render_template('home_page.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if (method == 'POST'):
		email = request.form(email)
		password = request.form(password)
	else:
		return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if (method == 'POST'):
		full_name = request.form['full_name']
		email = request.form['email']
		password = request.form['password']
		dob = request.form['day']
		mob = request.form['month']
		yob = request.form['year']
		phone_number = request.form['phone_number']
		Gender = request.form['gender']

		costumer=costumer(name=name, email=email, dob=dob, password=password, username = username , phone_number = phone_number , gender = gender)
		dbsession.add(user)
		dbsession.commit()

	else:
		return render_template('signup.html')