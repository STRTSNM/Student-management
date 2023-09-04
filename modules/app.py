from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'your_secret_key'


users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def loading():
    return render_template('loading.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' and 'password' in session:
        return redirect(url_for('dashboard'))

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
    return redirect(url_for('loading'))

if __name__ == '__main__':
    app.run(debug=True)