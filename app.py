## SETUP: 
## 1) install & run a virtual environment by running these commands in the vscode bash terminal:
##      py -m venv .venv
##      .venv/scripts/activate
##    bash terminal should show (env) on it now
## 2) run the following command in the vscode terminal to install dependencies:
##      -m pip install -r requirements.txt
## 3) run the web app by typing the following command in the terminal:
##      python app.py
## 4) the web app should then run on http://localhost:5000 (also displayed in vscode terminal)

import MySQLdb.cursors, bcrypt, generator, jsonGenerator, requests
from flask import Flask, render_template, redirect, url_for, request, session, jsonify, send_from_directory, send_file
# from flask_login import login_required, LoginManager
from flask_mysqldb import MySQL
from imgur_python import Imgur
from os import path
from io import BytesIO


app = Flask(__name__)

# Secret key for hashing passwords
app.secret_key = "6xJ]&FRr?am@KX1h.%3=]w.@Wv'+/>f~"

# SQL database connection
app.config['MYSQL_HOST'] = 'dgn.c34mk48scuxa.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'dgnadmin'
app.config['MYSQL_PASSWORD'] = 'vsyjAheSRR9N8TjVtEbKJd'
app.config['MYSQL_DB'] = 'dgn'
mysql = MySQL(app)

# Imgur API connection
imgur_client = Imgur({
    "client_id":"afe66f42ae38075",
    "client_secret":"6e048e2f025ad3e84112451e9809d97171fe174c",
    "access_token": "5b49aa23222bc7d472a3ffdca6bd53c7b7fbbddd",
    "expires_in": 315360000,
    "token_type": "bearer",
    "refresh_token": "44c1b31054dcdb1042ce9bec941c150d4ec742bb",
    "account_id": 116171211,
    "account_username": "GebTheGib"
})

### ROUTES ###

# Landing page / dungeon generation page
@app.route("/")
def generate_dungeon():
    generator.main(False, 40, 10)
    return render_template("generator.html")

# Route for generating a new dungeon
@app.route('/generate', methods=['POST'])
def generate_route():
    timesRan = 0
    data = request.get_json()
    size = int(data.get('size'))  # Convert 'size' to integer
    difficulty = int(data.get('difficulty'))  # Convert 'difficulty' to integer
    theme = data.get('theme')  # Get 'theme' as string
    if timesRan > 0:
        ran = True
    else:
        ran = False

    try:
        generator.main(ran, size, difficulty)  # Generate the image
        return jsonify({'message': 'Image generated successfully'})
        timesRan += 1
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for serving the generated dungeon image
@app.route('/dungeon.png')
def serve_dungeon():
    return send_from_directory('static', 'dungeon.png')

# About page
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

            passMatch = bcrypt.checkpw(loginBytes, dbBytes)
            #print(passMatch)

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
            return render_template('login.html', msg = 'You have successfully registered!')
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

# User settings page
@app.route('/settings')
def settings():
    if 'loggedin' in session:
        return render_template('settings.html')
    else:
        return redirect(url_for('login'))

# Route for updating user information
@app.route('/update', methods=['GET', 'POST'])
def update():
    msg=''
    # get user info from database to verify
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user WHERE username = %s', [session['username']])
    account = cursor.fetchone()

    if account == None:
        # account does not exist, credentials are incorrect
        msg='Invalid username or password'

    else:
        # decrypt and verify mathcing password
        loginPass = request.form['passverify']
        loginBytes = loginPass.encode('utf-8') # encode form password
        dbPass = account['password']
        dbBytes = dbPass.encode('utf-8') # encode db password
        passMatch = bcrypt.checkpw(loginBytes, dbBytes) # check if they match

        # begin updating if all credentials match
        if 'loggedin' in session and request.form['userverify'] == account['username'] and passMatch:

            # change username if username form is filled out
            if request.method == 'POST' and 'newuser' in request.form:
                cursor.execute('UPDATE user SET username = %s WHERE iduser = %s', [request.form['newuser'], session['id']])
                mysql.connection.commit()
            
            # change password if password form is filled out
            if request.method == 'POST' and 'newpass' in request.form:
                newpass = request.form['newpass']
                # Encrypt the new password
                passBytes = newpass.encode('utf-8')
                salt = bcrypt.gensalt()
                newPassEncrypt = bcrypt.hashpw(passBytes, salt)
                # add to db
                cursor.execute('UPDATE user SET password = %s WHERE iduser = %s', [newPassEncrypt, session['id']])
                mysql.connection.commit()
                msg='Changes saved'

    # return if changes were saved or not
    return render_template('settings.html', msg=msg)

# Route for deleting user
@app.route('/delete', methods=['GET', 'POST'])
# @login_required
def delete():
    msg=''
    # get user info from database to verify
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user WHERE username = %s', [session['username']])
    account = cursor.fetchone()

    if account == None:
        # account does not exist, credentials are incorrect
        msg='Invalid username or password'

    else:
        # decrypt and verify mathcing password
        loginPass = request.form['passverify']
        loginBytes = loginPass.encode('utf-8') # encode form password
        dbPass = account['password']
        dbBytes = dbPass.encode('utf-8') # encode db password
        passMatch = bcrypt.checkpw(loginBytes, dbBytes) # check if they match

        # delete account if credentials are correct
        if 'loggedin' in session and request.form['userverify'] == account['username'] and passMatch:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            # remove all associated dungeon images from imgur gallery
            cursor.execute('SELECT imgId FROM dungeon WHERE iduser = %s', (session['id'],))
            imgIdList = cursor.fetchall()
            #print(imgIdList)
            for id in imgIdList:
                response = imgur_client.image_delete(id['imgId'])

            # remove user from the database
            cursor.execute('DELETE FROM user WHERE iduser = %s', (session['id'],))
            mysql.connection.commit()

            # remove saved dungeons associated with user
            cursor.execute('DELETE FROM dungeon WHERE iduser = %s', (session['id'],))
            mysql.connection.commit()

            # logout the user
            session.pop('loggedin', None)
            session.pop('id', None)
            session.pop('username', None)
            msg = 'Account deleted'
            return render_template('login.html', msg=msg)
        else:
            msg='Invalid username or password'

    return redirect(url_for('settings'), msg=msg)

@app.route('/save', methods=['POST'])
# @login_required
def save():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form:
            # get name from request form & image from static folder
            name = request.form['name']

            # store dungeon image via imgur API

            # requests method
            clientID = 'afe66f42ae38075'
            headers = {'Authorization': 'Client-ID ' + clientID}
            url = 'https://api.imgur.com/3/upload'
            with open(path.realpath('static/dungeon.png'), 'rb') as img:
                payload = {'image': img}
                response = requests.post(url, headers=headers, files=payload)
                id = response.json()['data']['id']
                print(response.json())


            # imgur_python method
            #file = path.realpath('static/dungeon.png')
            #title = name
            #description = ''
            #album = None
            #disable_audio = 0
            #response = imgur_client.image_upload(file, title, description, album, disable_audio)
            #id = response['response']['data']['id']

            # create Tabetop Sim save
            save = jsonGenerator.generateJson(id, name)

            # create new dungeon entry in database
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO dungeon VALUES (NULL, %s, %s, %s, NULL, %s)', (session['id'], id, name, save))
            mysql.connection.commit()

            msg = 'Dungeon saved successfully!'
        else: 
            msg = 'Please fill out the form'
    else: 
        msg = 'Please log in to save a dungeon'
    return redirect(url_for('profile'))

@app.route('/downloadsave', methods=['Get', 'POST'])
def downloadSave():

    if request.method == 'POST' and 'imgId' in request.form and 'dgnName' in request.form:
        
        imgId = request.form['imgId']
        saveName = request.form['dgnName'] + ".json"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT dgnSave FROM dungeon WHERE imgId = %s', [imgId])
        save = cursor.fetchone()
        #print(save)
        file1 = open('output/save.json', 'w')
        file1.write(str(save['dgnSave']))
        file1.close()

        return send_file('output/save.json', download_name=saveName,as_attachment=True)
    else:
        #print("false")
        return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
