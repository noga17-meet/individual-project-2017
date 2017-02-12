from flask import *
from flask import session as login_session
from nogas_databases import *

app = Flask(__name__)
app.secret_key="this is my project"


engine = create_engine('sqlite:///FizzBuzz.db')
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
def homepage():
	return render_template('home_page.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form(email)
		password = request.form(password)
	else:
		return render_template('login.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'POST':
		full_name = request.form['full_name']
		email = request.form['email']
		password = request.form['password']
		dob = request.form['day']
		mob = request.form['month']
		yob = request.form['year']
		phone_number = request.form['phone_number']
		Gender = request.form['gender']

		costumer=costumer(name=name, email=email, dob=dob, password=password, username = username , phone_number = phone_number , gender = gender)
		session.add(costumer)
		session.commit()
		return redirect(url_for('cats_page'))

	else:
		return render_template('sign_up_page.html')


if __name__=='__main__':
	app.run(debug=True)