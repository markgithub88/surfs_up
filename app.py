from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/test')
def test():
    return 'This is a test'











