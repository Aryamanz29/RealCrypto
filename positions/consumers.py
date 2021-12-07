import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
import asyncio
import time
from channels.db import database_sync_to_async
from .models import Position


@sync_to_async
def get_all_positions():
    return list(Position.objects.values())


class PositionsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "position_room_name"
        self.room_group_name = "position_group_name"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        while True:
            students_data = await get_all_positions()
            print(students_data)

            # Send message to WebSocket
            await self.send(
                text_data=json.dumps(
                    {
                        "positions": students_data,
                    }
                )
            )
            time.sleep(3)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data,
            },
        )

    # Receive message from room group
    async def chat_message(self, event):

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": event,
                }
            )
        )
