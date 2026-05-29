from django.urls import reverse

def test_register(api_client):
    response = api_client.post('/api/auth/register/', {
        'username': 'test',
        'password': 'pass1234',
        'role': 'attendee'
    })

    assert response.status_code == 201



def test_login(api_client, attendee):
    response = api_client.post('/api/auth/login/', {
        'username': 'attendee1',
        'password': 'pass1234'
    })

    assert response.status_code == 200
    assert 'access' in response.data