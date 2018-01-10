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

# test no parameters for organisation
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

# test no parameters for person
r = requests.post('http://{0}:{1}/users/pers/'.format(host_ip, port),
        json={})
assert r.status_code == 400

# test no first name
r = requests.post('http://{0}:{1}/users/pers/'.format(host_ip, port),
        json={'last_name':'Doe'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no last name
r = requests.post('http://{0}:{1}/users/pers/'.format(host_ip, port),
        json={'first_name':'John'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no email
r = requests.post('http://{0}:{1}/users/pers/'.format(host_ip, port),
        json={'first_name':'John', 'last_name':'Doe'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

