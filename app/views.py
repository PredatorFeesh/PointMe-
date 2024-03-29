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

@app.route('/profile/<int:id>')
@login_required
def profile(id):
    viewing_user = User.query.filter_by(id=id).first()
    user = User.query.filter_by(id=current_user.id).first()
    if user is None:
        print("Doesn't exist!")
        return redirect(url_for('index'))
    if user.id == viewing_user.id:
        return redirect(url_for('my_profile'))
    return render_template('profile.html', user=user, viewing_user=viewing_user)

@app.route('/follow/<int:id>')
@login_required
def follow(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        print("User not found!")
        return redirect(url_for('index'))
    if user == current_user:
        print("Can't yourself!!")
        return redirect(url_for('index'))
    current_user.follow(user)
    db.session.commit()
    print("Success!")
    return redirect(url_for('index'))

@app.route('/unfollow/<int:id>')
@login_required
def unfollow(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        print("User not found!")
        return redirect(url_for('index'))
    if user == current_user:
        print("Following ourself!")
        return redirect(url_for('index'))
    current_user.unfollow(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/my_profile')
@login_required
def my_profile():
    user = User.query.filter_by(id=current_user.get_id()).first()
    # rec_query = Event.query.paginate(1,5,False)
    # events_query = Event.query.filter_by(user_id=user.id).paginate(1,5,False)
    followed_events = user.get_events() 
    
    return render_template('my_profile.html', events=followed_events, user=user)


@app.route('/events')
def events():
    return redirect("events/1")

@app.route('/events/<int:page>')
def events_page(page):
    if page < 1: return redirect("/events/1")
    rec_query = Event.query.paginate(page, 5, False) 
    print(rec_query.items)
    if len(rec_query.items) == 0: 
        if page == 1:
            return redirect(url_for("my_profile"))
        return redirect("/events/"+str(page-1))
    return render_template('events.html', events=rec_query.items, page_num=page)

@app.route('/attractions/')
def attractions():
    return redirect(("attractions/1"))

@app.route('/attractions/<int:page>')
def attractions_page(page):
    if page < 1: return redirect("attractions/1")
    rec_query = Attraction.query.paginate(page, 5, False) 
    if len(rec_query.items) == 0: 
        if page == 1:
            return redirect(url_for("profile"))
        return redirect("/attractions/"+str(page-1))
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