from celery import shared_task
from .models import Position
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from .utils import get_random_code
import requests


@shared_task
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    data = requests.get(url).json()
    # Fetching data from API and save it to the database
    for crypto in data:
        p, _ = Position.objects.get_or_create(name=crypto["name"])
        p.image = crypto["image"]
        p.price = crypto["current_price"]
        p.rank = crypto["market_cap_rank"]
        p.market_cap = crypto["market_cap"]
        p.save()


# Running this celery task in every 1 minutes
@periodic_task(run_every=(crontab(minute="*/1")))
def get_crypto_current():
    get_crypto_data()
