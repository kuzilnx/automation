from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return "Hello from Flask"


#if __name__ == "__main__":
#    app.run()
