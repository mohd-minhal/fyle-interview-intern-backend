def test_filter_users(client):
    response = client.get('/principal/users/filter?username=student1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['data']) == 1
    assert data['data'][0]['username'] == 'student1'


def test_get_user_by_id(client):
    response = client.get('/principal/users/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['data']['username'] == 'student1'


def test_get_non_existant_user_by_id(client):
    response = client.get('/principal/users/999')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_get_user_by_email(client):
    response = client.get('/principal/users/email/student1@fylebe.com')
    assert response.status_code == 200
    data = response.get_json()
    assert data['data']['email'] == 'student1@fylebe.com'


def test_get_non_existant_user_by_email(client):
    response = client.get('/principal/users/email/nonexistent@example.com')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'User not found'


def test_filter_users_by_email(client):
    response = client.get('/principal/users/filter',
                          query_string={'email': 'student1@fylebe.com'})

    assert response.status_code == 200
    data = response.json
    assert any(user['email'] == 'student1@fylebe.com' for user in data['data'])
