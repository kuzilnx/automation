# controller for routing http requests:
# /
# /home
# /index
# /about
# /contact

from flask import Flask
from flask import render_template
from model import write_to_file

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/write/<data>',methods=['GET', 'POST'])
def write(data):
    out= write_to_file('db', data)
    return render_template('index.html', title=out)

app.run(port=8080) #1024 --> Well known ports 0 - 65563 --> 1024 pre destinated ports
