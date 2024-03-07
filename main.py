
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volume_up')
def volume_up():
    return 'Volume up'

@app.route('/volume_down')
def volume_down():
    return 'Volume down'

if __name__ == '__main__':
    app.run(debug=True)
