# app/__init__.py
import datetime

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_required
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask(__name__)
app.config.from_object('app.config.Config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
socketio = SocketIO(app)

from app.models import User, Room, Message


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/chatroom/<int:room_id>', methods=['GET', 'POST'])
@login_required
def chatroom(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        msg = request.form.get('message')
        if msg:
            message = Message(content=msg, room=room, author=current_user)
            db.session.add(message)
            db.session.commit()
    messages = Message.query.filter_by(room=room).all()
    return render_template('chatroom.html', room=room, messages=messages)


@socketio.on('message')
def handle_message(data):
    msg = data['msg']
    room = data['room']
    author = current_user.username  # Assumindo que você está usando Flask-Login
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Envia a mensagem para todos os clientes na sala
    socketio.emit('message', {
        'author': author,
        'msg': msg,
        'time': timestamp
    }, room=room)


@socketio.on('join')
def on_join(data):
    username = data['username']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    room = data['room']
    join_room(room)
    emit('message', {'author': "System", 'msg': f'{username} has entered the room.', 'time': timestamp}, room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    room = data['room']
    leave_room(room)
    emit('message', {'author': "System", 'msg': f'{username} has left the room.', 'time': timestamp}, room=room)


from app import routes, models
