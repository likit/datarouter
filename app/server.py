from flask import Flask, jsonify, request, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dataroutersecret'
# TODO: create a view for client's registration

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


@app.route('/register')
def register():
    org_params = {}
    accepted_params = set(['orgname', 'orgtype', 'department', 'unit'])
    for key in request.args:
        if key in accepted_params:
            org_params[key] = request.args[key]
    if 'client_org' in session:
        _newid = len(session['client_org']) + 1
        org_params['id'] = _newid
        client_org = session['client_org']
        client_org.append(org_params)
        session['client_org'] = client_org
    else:
        org_params['id'] = 1
        session['client_org'] = [org_params]
    return "Registration done"


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
    app.run(debug=True)
