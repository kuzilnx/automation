
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('flask-example.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)