def test_event_list(api_client, event):
    response = api_client.get('/api/events/')

    assert response.status_code == 200



def test_create_event_organizer(api_client, organizer):
    api_client.force_authenticate(user=organizer)

    response = api_client.post('/api/events/', {
        'title': 'New Event',
        'description': 'Desc',
        'status': 'published',
        'event_type': 'online',
        'max_attendees': 5,
        'start_date': '2025-12-01T10:00:00Z',
        'end_date': '2025-12-01T12:00:00Z'
    })

    assert response.status_code == 201