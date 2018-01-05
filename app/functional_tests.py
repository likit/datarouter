import requests
'''Test registration of organization.
    parameters:
    - name = name of organization
    - type = type of organization: private, public..
    - postal_code = postcal code
    - address = street address
'''

# test no parameters
r = requests.post('http://localhost:5550/users/orgs/',
        json={})
assert r.status_code == 400

# test no name
r = requests.post('http://localhost:5550/users/orgs/',
        json={'postal_code': '10150'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'