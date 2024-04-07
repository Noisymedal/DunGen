## SETUP: run the following command in the terminal to install dependencies (flask and matplotlib specifically):
## -m pip install -r requirements.txt
## run the web app by typing the following command in the terminal:
## python app.py
## the web app should then run on http://localhost:5000

from flask import Flask, render_template, redirect, url_for, request, session
# from flask_login import login_required, LoginManager
from flask_mysqldb import MySQL
import MySQLdb.cursors, re, bcrypt
import generator
import cv2

app = Flask(__name__)

# Secret key for hashing passwords
app.secret_key = "6xJ]&FRr?am@KX1h.%3=]w.@Wv'+/>f~"

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

@app.route("/about")
# @login_required
def about():
    return render_template("about.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # If user submitted the form correctly, check if account exists in db
        username = request.form['username']
        loginPass = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s', [username])
        account = cursor.fetchone()

        if account:
            # If account exists in db, check if passwords match
            dbPass = account['password']
            dbBytes = dbPass.encode('utf-8')
            loginBytes = loginPass.encode('utf-8')

            passMatch = bcrypt.checkpw(loginBytes, dbBytes) # fix ---TODO---
            print(passMatch)

            if passMatch:
                # If user and password match, log user in

                # Create session data
                session['loggedin'] = True
                session['id'] = account['iduser']
                session['username'] = account['username']
                # Redirect to home page
                return redirect(url_for('profile'))
            else:
                # Error: password does not match
                msg = 'Incorrect password'
        else: 
            # Error: user not in db
            msg = 'Username does not exist'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

# Route for logging out
@app.route('/logout')
# @login_required
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
            # Encrypt the password
            passBytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            passNew = bcrypt.hashpw(passBytes, salt)

            # Insert the new account into the accounts table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)', (username, passNew, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# Route for profile page
@app.route('/profile')
# @login_required
def profile():
    # Check if the user is logged in
    if 'loggedin' in session:
        # Get account info from database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE iduser = %s', (session['id'],))
        account = cursor.fetchone()

        # Get saved dungeons
        cursor.execute('SELECT * FROM dungeon WHERE iduser = %s', (session['id'],))
        dungeons = cursor.fetchall()

        # Show the profile page with account info
        return render_template('profile.html', account = account, dungeons = dungeons)
    # Redirect to login page if not logged in
    return redirect(url_for('login'))

@app.route('/delete')
# @login_required
def delete():
    msg = ''
    if 'loggedin' in session:
        # remove user from the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM user WHERE iduser = %s', (session['id'],))
        mysql.connection.commit()

        # remove saved dungeons associated with user
        cursor.execute('DELETE FROM dungeon WHERE iduser = %s', (session['id'],))
        mysql.connection.commit()

        # logout the user
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('login'))
    else:
        msg = 'literally how'

    return redirect(url_for('/'), msg=msg)

@app.route('/save', methods=['POST'])
# @login_required
def save():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form:
            # get name from request form & image from static folder
            name = request.form['name']
            image = cv2.imread('static/dungeon.png')
            # create new dungeon entry in database
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO dungeon VALUES (NULL, %s, %s, %s, NULL)', (session['id'], image, name))
            mysql.connection.commit()
            msg = 'Dungeon saved successfully!'
        else: 
            msg = 'Please fill out the form'
    else: 
        msg = 'Please log in to save a dungeon'
    return redirect(url_for('profile'))

if __name__ == "__main__":
    app.run(debug=True)
