from flask import Flask, jsonify, request, session, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)
app.secret_key = 'Flaming_Boys.gamer'  # Replace with a strong secret key

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Sample data
data = {
    'message': 'Hello, World!'
}

# Home page
@app.route('/')
def home():
    if 'username' in session:
        return f"<h1>Welcome, {session['username']}!</h1><p>Experience the authentic flavors of India at our restaurant.</p>"
    return "<h1>Welcome to My Indian Restaurant</h1><p>Experience the authentic flavors of India at our restaurant.</p>"

# Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        if c.fetchone():
            return "User already exists!"
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Sign Up">
        </form>
    ''')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        if c.fetchone():
            session['username'] = username
            return redirect(url_for('home'))
        return "Invalid credentials!"
    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# API endpoints
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def save_data():
    new_data = request.json
    data.update(new_data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
