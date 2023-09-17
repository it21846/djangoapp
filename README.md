# Django app for Studenttransfer applications

To configure the project enter the following commands

``` bash
git clone https://github.com/it21846/djangoapp.git
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
cd djangoapp
cp djangoapp/.env.example djangoapp/.env
```

To run the project with gunicorn webserver, execute
```bash
gunicorn --bind 0.0.0.0:8000 djangoapp.wsgi
```
