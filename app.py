from flask import Flask, render_template,request, flash
import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE if not exists user (userid integer primary key AUTOINCREMENT, fname varchar(50), email varchar(50), password varchar)')
print ("Table created successfully")
conn.close()
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'DevOps Project'
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/',methods=['GET','POST'])
def login():
    flash('',"success")
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        email=request.form['email']
        psw=request.form['password']
        with sqlite3.connect("database.db") as con:
            selquery= "SELECT * FROM user WHERE email=? AND password=?" 
            curr= con.execute(selquery,(email,psw))
            if curr.fetchone():
                print('User Found ')
                return render_template('home.html')
            else:
                flash('User Not Found, Try Again',"danger")
                print('User not Found')
    flash('',"sucess")
    return render_template('login.html')
        
@app.route('/regis',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        fname = request.form['fname']
        email = request.form['email']
        psw = request.form['psw']
        with sqlite3.connect("database.db") as con:
            insquery="INSERT INTO user (fname,email,password) VALUES (?,?,?)"
            cur = con.cursor()
            cur.execute(insquery,(fname,email,psw) )
            con.commit()
        flash('User Successfully Added')
        print("Record Successfully added")
        return render_template('login.html')
    return render_template('register.html')
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)
