import requests
import os
'''Test registration of organization.
    parameters:
    - name = name of organization
    - type = type of organization: private, public..
    - postal_code = postcal code
    - address = street address
'''

host_ip = os.environ.get('HOST_IP', 'localhost')
port = os.environ.get('PORT', '5550')

# test no parameters
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={})
assert r.status_code == 400

# test no organization name
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'postal_code': '10150'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no postal code
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'org_name': 'Mahidol'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no first name
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'org_name': 'Mahidol', 'postal_code':'12150'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test wrong postal code
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'postal_code': '101500'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters wrong'