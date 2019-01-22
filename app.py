from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@socketio.on('connect', namespace='/test')
def test_connect():
    # 连接事件处理程序可以选择返回False以拒绝连接。这样就可以在此时对客户端进行身份验证。
    emit('my_response', {'data': 'Connected', 'count': 233})
    return True


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@socketio.on('my_event', namespace='/test')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    socketio.run(app, debug=True)
