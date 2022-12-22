from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("join")
def handle_enter_channel(json):
    join_room(json.get("room"))


@socketio.on("leave")
def handle_exit_channel(json):
    leave_room(json.get("room"))


@socketio.on("notify")
def handle_notify_event(json):
    channel = json.pop("channel", None)
    print(json)
    emit("message", json, to=channel)


if __name__ == "__main__":
    socketio.run(app)
