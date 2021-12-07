# RealCrypto 📉

#### A **Realtime crypto table** based on [django channels](https://channels.readthedocs.io/en/stable/), [redis](https://pypi.org/project/redis/) and [celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html).

![Screenshot from 2021-12-07 22-38-54](https://user-images.githubusercontent.com/56113566/145075943-4d9a1a0e-c511-4b2a-abf3-c5d4a791cf7a.png)

### Setup 🛠

#### Install redis and start `redis-server` 📥:

```bash

sudo apt-get install redis-server

sudo service redis-server start

[Options: {start|stop|restart|force-reload|status}]

```

#### Create & activate `virtualenvironment`💾 :

```bash
python3 -m venv env 
source env/bin/activate
```
#### Install requirements 🚀 :

```bash
pip install -r requirements.txt
```
#### Run below commands on terminal ⤵ :

```bash

python3 manage.py makemigrations

python3 manage.py migrate

python manage.py createsuperuser

python3 manage.py runserver
```

#### Terminal 2 💻 :

```bash
celery -A RealCrypto worker -l INFO
```

#### Terminal 3 💻 :

```bash
celery -A RealCrypto beat -l INFO
```