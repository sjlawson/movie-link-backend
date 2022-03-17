from flask import url_for


def test_healthcheck(test_app):
    with test_app.app_context():
        test_client = test_app.test_client()
        response = test_client.get('/healthcheck')
        assert response.status_code == 200
        assert response.data == b'OK'


def test_search_empty_query(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        query_params = {
            'title': 'Adventure',
            'tags': 'funny',
            'genres': 'comedy'
        }
        response = test_client.get(url_for('main.search'), query_string=query_params)
        assert response.status_code == 200
        assert response.json['search_query'] == {'title': 'The Ting'}
