## Ice&Fire API :fire:
A simple python/django based CRUD application to play around some of the APIs provided by the website.


### How to Install
This project uses `Python 3+` so make sure you are having python3 preinstalled on your local machine.

```
git clone https://github.com/rahulkp220/iceandfire-api.git
cd iceandfire-api
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate --run-syncdb
python manage.py runserver 8080
```

You can also access the `admin` interface of django by using `python manage.py createsuperuser`


### List of APIs
Once the server is up and running, go through


#### Simple API
* `http://localhost:8080/api/external-books/` to fetch all the results
* `http://localhost:8080/api/external-books/?name=nameOfABook` to fetch results for a specific book.


#### DRF based REST API
`http://localhost:8080/api/v1/books/` for all CRUD operations


### Tests & Coverage
Just run `python manage.py test` to trigger tests on your local machine.
To check coverage, run the following:
* `coverage run --source="." manage.py test book` 
* `coverage report`

Current coverage report is shared below.
```
Name                     Stmts   Miss  Cover
--------------------------------------------
book/__init__.py             0      0   100%
book/admin.py               10      0   100%
book/apps.py                 3      3     0%
book/models.py              16      2    88%
book/serializers.py         48      0   100%
book/tests.py               44      0   100%
book/views.py               66      5    92%
iceandfire/__init__.py       0      0   100%
iceandfire/settings.py      18      0   100%
iceandfire/urls.py           9      0   100%
iceandfire/wsgi.py           4      4     0%
manage.py                   12      2    83%
--------------------------------------------
TOTAL                      230     16    93%
```

### Contributions Welcome! 
:tada: :tada: