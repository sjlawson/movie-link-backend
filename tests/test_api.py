
def test_healthcheck(app):
    with app.app_context():
        test_client = app.test_client()
        response = test_client.get('/healthcheck')
        assert response.status_code == 200
        assert response.data == b'OK'


def test_search_empty_query(app, test_database):
    test_client = app.test_client()
    response = test_client.post('/s', json={'title': 'The Thing'})
    assert response.status_code == 200
    assert response.json['search_query'] == {'title': 'The Thing'}
