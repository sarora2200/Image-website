from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = "Geeks"
    password = "12345"
    
    if request.method == 'POST':
        form_username = request.form['username']
        form_password = request.form['password']
        
        if form_username == username and form_password == password:
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)