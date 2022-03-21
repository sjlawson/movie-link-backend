from decimal import Decimal

from flask import url_for


def test_healthcheck(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        response = test_client.get(url_for('main.healthcheck'))
        assert response.status_code == 200
        assert response.json == {'status': 'OK'}


def test_search_with_no_params(test_app):
    """
    If no params are given, just return all the movies
    :param test_app:
    :return:
    """
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        response = test_client.get(url_for('main.search'))
        assert response.status_code == 200
        assert response.json['search_query'] == {}
        assert len(response.json['result']) == 9742


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
                                            'links': [{'imdb': '76363', 'tmdb': '13716.0'}],
                                            'movie_id': 31193,
                                            'rating': 3.5,
                                            'tags': [],
                                            'title': 'Many Adventures of Winnie the Pooh, The (1977)'}]


def test_search_genre(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        query_params = {
            'title': '',
            'tags': '',
            'genres': 'adventure, comedy'
        }
        response = test_client.get(url_for('main.search'), query_string=query_params)
        assert response.status_code == 200
        assert response.json['search_query'] == {
            'genres': 'adventure, comedy',
            'tags': '',
            'title': ''
        }
        assert len(response.json['result']) == 4620


def test_single_rating_search(test_app):
    with test_app.app_context(), test_app.test_request_context():
        test_client = test_app.test_client()
        query_params = {
            'rating': 3.5
        }
        response = test_client.get(url_for('main.search'), query_string=query_params)
        assert response.status_code == 200
        assert response.json['result'] == [{'genres': 'Animation|Children|Musical',
                                            'links': [{'imdb': '76363', 'tmdb': '13716.0'}],
                                            'movie_id': 31193,
                                            'rating': 3.5,
                                            'tags': [],
                                            'title': 'Many Adventures of Winnie the Pooh, The (1977)'}]
