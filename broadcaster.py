import socketio
import time
from faker import Faker
import random

sio = socketio.Client()

faker = Faker()


@sio.event
def connect():
    print("I'm connected!")
    sio.emit("join", {"room": "notification"})


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")
    sio.emit("leave", {"room": "notification"})


@sio.event
def message(data):
    print("message received : ", data)


time.sleep(10)
sio.connect("http://0.0.0.0:5000", wait_timeout=20)
counter = 0
while True:
    counter += 1
    sio.emit(
        "notify",
        {
            "message": {
                "name": faker.name(),
                "project": faker.bs(),
                "timestamp": faker.iso8601(),
            },
            "channel": "notification",
        },
    )

    time.sleep(random.randint(3, 10))
