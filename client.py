import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("I'm connected!")
    sio.emit("join", {"room": "notification"})


@sio.event
def connect_error(data):
    print("The connection failed!")
    sio.emit("leave", {"room": "notification"})


@sio.event
def disconnect():
    print("I'm disconnected!")
    sio.emit("leave", {"room": "notification"})


@sio.event
def message(data):
    print("message received : ", data)


sio.connect("http://localhost:5000")

sio.wait()
