from flask import Flask, render_template,request
import sqlite3
conn = sqlite3.connect('database.db')

#conn.execute('CREATE TABLE users (email TEXT, password TEXT)')

conn.close()

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/home')
def index():
    return render_template('home.html')
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/regis')
def register():

    return render_template('register.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)
