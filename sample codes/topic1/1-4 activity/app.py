rom flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return 'Hello from the Planetary API.'

@app.route('/not_found')
def not_found():
    return 'Not found.'


if __name__ == '__main__':
    app.run()