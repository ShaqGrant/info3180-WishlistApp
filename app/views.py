"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,jsonify,g,session, flash, json
from app import db
import os, time

from flask.ext.wtf import Form 
from wtforms.fields import TextField # other fields include PasswordField 
from wtforms.validators import Required, Email
from app.models import User
from app.forms import LoginForm
from werkzeug.utils import secure_filename
from flask.ext.login import login_user, logout_user, current_user, login_required
from datetime import datetime
from random import getrandbits 




# @app.before_request
# def before_request():
#     g.user = current_user
    
###
# Routing for your application.
###
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = None
    try:
        if request.method == 'POST':
            attempted_username = request.form['username']
            db_username = User_profile.query.filter(User_profile.username == attempted_username).one()
            attempted_password = request.form['password']
            
            if attempted_username == db_username.username and attempted_password == "password":
                return redirect(url_for('profile_list'))
            else:
                error = 'Invalid username or password'
        return render_template("login.html",error=error,form=form)
    except Exception as e:
        flash(e)
        return render_template("login.html",error=error,form=form)


SECRET_KEY="super secure key"
app.config.from_object(__name__)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile/', methods=['POST','GET'])
def profile():
    form = LoginForm()
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        user_name = request.form['last_name']
        age = request.form['age']
        sex = request.form['sex']
        file = request.file['image']
        image = secure_filename(file.filename)
        file.save(os.path.join("app/static/uploads", image))
        user = User(id, first_name=first_name, last_name=last_name, user_name=user_name, age=age, sex=sex, img_file=image)
       
        # write the information to the database
        # newprofile = User_profile(first_name=first_name,
        #                       last_name=last_name)
        db.session.add(user)
        db.session.commit()
        flash('New User Profile created')
        return redirect(url_for('profile_list' , id=user.id))
    else:
        return render_template('profile_add.html',form=form)

        # return "{} {} was added to the database".format(request.form['first_name'],
        #                                      request.form['last_name'])

        

@app.route('/profiles/',methods=["POST","GET"])
def profile_list():
    users = db.session.query(User).all()
    userlist=[]
    for user in users:
        userlist.append({'username':user.username,'userid':user.userid})
        if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
            return jsonify(users=userlist)
        return render_template('profile_list.html', users=users)

@app.route('/profile/<int:id>')
def profile_view(id):
    timeinfo = time.strftime("%a, %b %d %Y")
    user = User.query.filter_by(id=id).first()
    if not user:
      flash("No such user")
    else:
      image = '/static/uploads/' + user.image
      if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
            return jsonify(userid=user.userid, image=image,username=user.username, sex=user.sex, age=user.age,profile_added_on=user.profile_added_on)
      else:
            user = {'id':user.userid,'image':image, 'user_name':user.user_name,'first_name':user.first_name, 'last_name':user.last_name,'age':user.age, 'sex':user.sex,'date_added':timeinfo(user.date_added)}
            return render_template('profile_add.html', user=user)
    return redirect(url_for("profiles"))


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
