## SETUP: run the following command in the terminal to install dependencies (flask and matplotlib specifically):
## -m pip install -r requirements.txt
## run the web app by typing the following command in the terminal:
## python app.py
## the web app should then run on http://localhost:5000

from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors, re, hashlib
import generator
from flask import jsonify
from flask import send_from_directory

app = Flask(__name__)

app.secret_key = "holy moly"

# SQL database connection
app.config['MYSQL_HOST'] = 'dgn.c34mk48scuxa.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'dgnadmin'
app.config['MYSQL_PASSWORD'] = 'vsyjAheSRR9N8TjVtEbKJd'
app.config['MYSQL_DB'] = 'dgn'
mysql = MySQL(app)

### ROUTES ###

@app.route("/")
def generate_dungeon():
    generator.main()
    return render_template("generator.html")

@app.route('/generate', methods=['POST'])
def generate_route():
    data = request.get_json()
    size = int(data.get('size'))  # Convert 'size' to integer
    difficulty = int(data.get('difficulty'))  # Convert 'difficulty' to integer
    theme = data.get('theme')  # Get 'theme' as string

    try:
        generator.main(size, difficulty)  # Generate the image
        return jsonify({'message': 'Image generated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dungeon.png')
def serve_dungeon():
    return send_from_directory('static', 'dungeon.png')

@app.route("/about")
def about():
    return render_template("about.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))

        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['iduser']
            session['username'] = account['username']
            # Redirect to home page
            # flash('Login successful')
            return redirect(url_for('profile'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

# Route for logging out
@app.route('/logout')
def logout():
    # Remove session data
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))

# Route for creating new account
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''

    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        account = cursor.fetchone()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'

        # regex for validation (add later?)
        #elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            #msg = 'Invalid email address!'
        #elif not re.match(r'[A-Za-z0-9]+', username):
            #msg = 'Username must contain only characters and numbers!'
        
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Hash the password (Add in future)
            # hash = password + app.secret_key
            # hash = hashlib.sha1(hash.encode())
            # password = hash.hexdigest()

            # Account doesn't exist, and the form data is valid, so insert the new account into the accounts table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# Route for profile page
@app.route('/profile')
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        # Get account info from database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE iduser = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # Redirect to login page if not logged in
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
