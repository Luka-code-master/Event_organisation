from events.models import Registration


def test_review_confirmed_attendee(
    api_client,
    attendee,
    event
):
    Registration.objects.create(
        user=attendee,
        event=event,
        status='confirmed'
    )

    api_client.force_authenticate(user=attendee)

    response = api_client.post(
        f'/api/events/{event.id}/reviews/',
        {
            'rating': 5,
            'comment': 'Great'
        }
    )

    assert response.status_code == 201