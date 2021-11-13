from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/main')
def main():
    return render_template('main.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)
