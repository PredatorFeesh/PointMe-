from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import *
import flask_login as fl
from flask_login import current_user, login_user, logout_user, login_required

from app.models import *
from app.models import db

login_manager = fl.LoginManager()

@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

login_manager.login_view = "login"

login_manager.init_app(app)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return redirect(url_for('homepage'))


@app.route('/homepage')
def homepage():
    if current_user.is_authenticated:
        return redirect(url_for('my_profile'))
    return render_template('homepage.html')

@app.route('/view_attraction')
def view_attraction():
    return render_template('view_attraction.html')

@app.route('/view_event')
def view_event():
    return render_template('view_event.html')

@app.route('/profile')
@login_required
def profile():
    #user = User.query.filter_by(id= {{id of clicked user}} ).first()
    #rec_query = Event.query.filter_by(user_id=current_user.get_id())
    user = "user_beta"
    rec_query = Event.query.paginate(1,5,False)
    return render_template('profile.html',events=rec_query.items, user=user)

@app.route('/my_profile')
@login_required
def my_profile():
    user = User.query.filter_by(id=current_user.get_id()).first()
    rec_query = Event.query.paginate(1,5,False)
    #rec_query = Event.query.filter_by(user_id=current_user.get_id())
    return render_template('my_profile.html', events=rec_query.items, user=user)


@app.route('/events')
def events():
    return redirect("events/1")

@app.route('/events/<int:page>')
def events_page(page):
    if page < 1: return redirect("1")
    rec_query = Event.query.paginate(page, 5, False) 
    return render_template('events.html', events=rec_query.items, page_num=page)

@app.route('/attractions/')
def attractions():
    return redirect(("1"))

@app.route('/attractions/<int:page>')
def attractions_page(page):
    if page < 1: return redirect("1")
    rec_query = Attraction.query.paginate(page, 5, False) 
    return render_template('attractions.html', attractions = rec_query.items, page_num=page)

@app.route('/create_event', methods=["GET","POST"])
@login_required
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        event = Event(title=form.event_title.data, 
            description=form.description.data, 
            location=form.location.data, 
            start_date=form.start_date.data, 
            end_date = form.end_date.data)
        user = User.query.filter_by(id=current_user.get_id()).first()
        user.events.append(event)
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('create_event.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title="Sign In", form=form)