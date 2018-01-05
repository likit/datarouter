import requests

r = requests.post('http://localhost:5550/users/orgs/',
        json={})
assert r.status_code == 400

r = requests.post('http://localhost:5550/users/orgs/',
        json={'postal_code': '10150'})
assert r.status_code == 400
assert r.json()['message'] == 'Required parameters missing'