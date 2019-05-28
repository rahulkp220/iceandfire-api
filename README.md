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


#### Tests
Just run `python manage.py test` to trigger tests on your local machine.


### Contributions Welcome! 
:tada: :tada: