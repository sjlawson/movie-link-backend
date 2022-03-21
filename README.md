# MovieLens search
## Python API

This project is designed to be run inside a docker container, however it will function in naitive environment for testing purposes.

## Steps for setup:

The docker-compose file should be used to run everything and see it work with the react front end.
A simple `docker-compose up` in the main project directory should do the trick.
You should then see a message like:
```
site_1     | Compiled successfully!
site_1     |
site_1     | You can now view frontend-react in the browser.
site_1     |
site_1     |   Local:            http://localhost:80
site_1     |   On Your Network:  http://172.20.0.4:80
```
To load the front end web app in your browser, you will need the "On Your Network" address.


### To test the backend on a local machine

1- Build a virtual env for Python3.9+ i.e.: `python3.9 -m venv venv`
2- Activate the venv: `source venv/bin/activate`
3- Install dependencies: `pip install -r requirements.txt`
4- Run tests: `pytest` or `pytest -vv` if you like to see eveything

Uses in-memory sqlite for testing. It is also possible to run the API on your local.
1- Build a sqlite database by running, `flask db upgrade`
2- Import the small-set sample data: `flask movielens seed-data`
3- run: `flask run`
