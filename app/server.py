from flask import Flask, jsonify, request, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dataroutersecret'
# TODO: create a view for client's registration

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


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


@app.route('/users/orgs/', methods=['POST'])
def register():
    data = request.get_json()
    if data:
        if 'name' not in data:
            return jsonify({'message': 'Required parameters missing'}), 400
        return jsonify({'message': 'success'})
    return jsonify({'message': 'No parameters are specified.'}), 400


@app.route('/orgs/info')
def get_org_list():
    return jsonify({'orgs': session['client_org']})


@app.route('/orgs/info/<int:id>')
def get_org_info(id):
    for org in session['client_org']:
        if id == org['id']:
            return jsonify(org)
    return 'Not found'



@app.route('/clear_cookies')
def clear_cookies():
    if 'client_org' in session:
        del session['client_org']
    return 'Done'


if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")
