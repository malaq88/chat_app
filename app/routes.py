# app/routes.py
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from app.forms import RegistrationForm, LoginForm, RoomForm
from app.models import User, Room, Message
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_room', methods=['GET', 'POST'])
@login_required
def create_room():
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(
            name=form.name.data,
            theme=form.theme.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            owner=current_user
        )
        db.session.add(room)
        db.session.commit()
        flash('Room has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_room.html', form=form)

@app.route('/room/<int:room_id>', methods=['GET', 'POST'])
@login_required
def room(room_id):
    room = Room.query.get_or_404(room_id)
    if datetime.utcnow() > room.end_time:
        flash('The room has expired.', 'warning')
        return redirect(url_for('home'))

    if request.method == 'POST':
        message_content = request.form.get('message')
        if message_content:
            message = Message(content=message_content, room=room, author=current_user)
            db.session.add(message)
            db.session.commit()

    messages = Message.query.filter_by(room=room).all()
    return render_template('chatroom.html', room=room, messages=messages)
