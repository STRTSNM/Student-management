from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/loading')
def loading():
    return render_template('loading.html')

# Simulated user database (replace with your own authentication system)
users = {'user1': 'password1', 'user2': 'password2'}



# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if 1==1:
        return render_template('loading.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password are correct
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Dashboard route (protected route)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f'Welcome to the dashboard, {username}! <a href="/logout">Logout</a>'
    return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)