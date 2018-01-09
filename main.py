from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True
    

@app.route('/signup', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def validate_form():

    username = request.form['username'] 
    username_error = '' 
    password = request.form['password'] 
    password_error = ''
    verify = request.form['verify']
    verify_error = ''
    email = request.form['email']
    email_error = ''  

    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"
     
    if ' ' in username:
        username_error = "Not a valid username"        

    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"
        password = ''

    if ' ' in password:
        password_error = "Not a valid password"
        password = ''

    if verify != password or len(verify) == 0:
        verify_error = "Passwords do not match"
        verify = ''

    
    if len(email) < 3 or len(email) > 20:
        email_error = "Email must be between 3 and 20 characters"
    if '.' not in email:
        email_error = "Not a valid email"
    if '@' not in email:
        email_error = "Not a valid email"
    if ' ' in email:
        email_error = "Not a valid email"
                        

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template('index.html', username = username, username_error = username_error, password_error = password_error, verify_error = verify_error, email = email, email_error = email_error)

app.run()




