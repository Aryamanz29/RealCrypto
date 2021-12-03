# RealCrypto
Realtime crypto based django web app

### Setup

```python
sudo service redis-server start

python3 manage.py makemigrations

pyhton3 manage.py migrate

python3 manage.py runserver

celery -A RealCrypto worker -l INFO

celery -A RealCrypto beat -l INFO

```