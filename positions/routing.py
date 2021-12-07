from django.urls import path
from positions.consumers import PositionsConsumer

websocket_urlpatterns = [
    path("ws/positions/", PositionsConsumer.as_asgi(), name="positions"),
]
