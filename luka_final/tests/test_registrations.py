from events.models import Registration


def test_registration(api_client, attendee, event):
    api_client.force_authenticate(user=attendee)

    response = api_client.post(
        f'/api/events/{event.id}/registrations/',
        {}
    )

    assert response.status_code == 201