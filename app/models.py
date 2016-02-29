from . import db  
class Myprofile(db.Model):   
from random import getrandbits    
    
    id = db.Column(db.Integer, primary_key=True)     
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80)) 
    nickname = db.Column(db.String(80), unique=True)    
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    password = Column(db.String(80))
    
    
    def generate_user_id(self):
        return '6200%d' % getrandbits(16)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r %r %r %r %r %d %r %r>' % (self.user_id , self.firstname , self.lastname , self.nickname , self.email, self.age, self.sex)