def test_ready_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    data = response.json

    # Check if the status is 'ready'
    assert data['status'] == 'ready'

    assert 'time' in data

def test_valid_principal(client, h_principal):
    response = client.get('/principal/assignments', headers=h_principal)
    assert response.status_code == 200

def test_invalid_principal(client):
    response = client.get('/principal/assignments')
    assert response.status_code == 200

def test_invalid_api_endpoint(client):
    response = client.get('/invalid/api/path')
    assert response.status_code == 404