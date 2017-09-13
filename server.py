from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'


@app.route('/data')
def get_data():
    return '<table><tr><td>Name</td><td>Email</td></tr><tr><td>Likit</td><td>likit.pre@mahidol.edu</td></tr></table>'


@app.route('/json/data')
def get_json_data():
    data = {
        'name': 'Likit',
        'email': 'likit.pre@mahidol.edu'
    }
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)