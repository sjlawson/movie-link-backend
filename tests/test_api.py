from flask import url_for


def test_healthcheck(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        response = test_client.get(url_for('main.healthcheck'))
        assert response.status_code == 200
        assert response.data == b'OK'


def test_search_exact_title_query(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        query_params = {
            'title': 'Many Adventures of Winnie the Pooh, The (1977)',
            'tags': '',
            'genres': ''
        }
        response = test_client.get(url_for('main.search'), query_string=query_params)
        assert response.status_code == 200
        assert response.json['search_query'] == {
            'genres': '',
            'tags': '',
            'title': 'Many Adventures of Winnie the Pooh, The (1977)'
        }
        assert response.json['result'] == [{'genres': 'Animation|Children|Musical',
                                            'movie_id': 31193,
                                            'title': 'Many Adventures of Winnie the Pooh, The (1977)'}]


def test_search_genre(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        query_params = {
            'title': '',
            'tags': '',
            'genres': 'adventure'
        }
        response = test_client.get(url_for('main.search'), query_string=query_params)
        assert response.status_code == 200
        assert response.json['search_query'] == {
            'genres': 'adventure',
            'tags': '',
            'title': ''
        }
        assert len(response.json['result']) == 5


