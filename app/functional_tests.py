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
assert r.json()['message'] == 'No parameters are specified.'

# test no organization name
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'postal_code': '10150', 'org_type': 'Academic'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no organization type
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'postal_code': '10150', 'org_name': 'Mahidol'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no postal code
r = requests.post('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'org_name': 'Mahidol', 'org_type': 'Academic'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no parameters for person
r = requests.post('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={})
assert r.status_code == 400
assert r.json()['message'] == 'No parameters are specified.'

# test no first name
r = requests.post('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={'last_name':'Doe', 'email': 'john_doe@test.com'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no last name
r = requests.post('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={'first_name':'John', 'email': 'john_doe@test.com'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no email
r = requests.post('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={'first_name':'John', 'last_name':'Doe'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'

# test no password
r = requests.post('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={'first_name':'John', 'last_name':'Doe'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'


# test update informaton
r = requests.put('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={'licence_id':'123456789'})
assert r.status_code == 200
assert r.json()['message'] == 'Information updated'

r = requests.put('http://{0}:{1}/users/orgs/'.format(host_ip, port),
        json={'street':'Phayathai'})
assert r.status_code == 200
assert r.json()['message'] == 'Information updated'

# test delete user
r = requests.delete('http://{0}:{1}/users/persons/'.format(host_ip, port),
        json={})
assert r.status_code == 200
assert r.json()['message'] == 'Deletion succesful'

# test user veiwing
r = requests.get('http://{0}:{1}/users/'.format(host_ip, port),
        json={})
assert r.status_code == 200
assert r.json()['message'] == 'OK'
