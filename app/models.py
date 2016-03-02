from . import db  
from datetime import datetime
from random import getrandbits 

class User(db.Model):   
    id = db.Column(db.Integer, primary_key=True)     
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80)) 
    user_name = db.Column(db.String(80), unique=True)    
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    highscore = db.Column(db.Integer)
    tdollars = db.Column(db.Integer)
    date_added = db.Column(db.DateTime)
    img_file = db.Column(db.String(400))
    
    
    def __init__(self, first_name, last_name, user_name, email, age, sex, img_file): 
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.age = age
        self.sex = sex
        self.img_file = img_file
        self.date_added = datetime.now()

    
    def generate_user_id(self):
        return '6000%d' % getrandbits(12)
        
    
    def __repr__(self):
        return '<User %r>' % (self.user_id)
        
        
    
    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2 support
    #     except NameError:
    #         return str(self.id)  # python 3 support

    
        
        