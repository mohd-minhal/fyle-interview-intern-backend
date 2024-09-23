def test_ready_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    data = response.json

    # Check if the status is 'ready'
    assert data['status'] == 'ready'

    assert 'time' in data
