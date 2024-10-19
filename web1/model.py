from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class character(db.Model):

    character_id = db.Column('character_id',db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classe.class_id"), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'), nullable=False)
    background_id = db.Column(db.Integer, db.ForeignKey('background.background_id'), nullable=False)
    
    user = db.relationship("user")
    classe = db.relationship("classe")
    race = db.relationship("race")
    background = db.relationship("background")
    def __init__(self, name):
        self.name = name

class user(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class classe(db.Model):
    class_id = db.Column('class_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __init__(self, name):
        self.name = name
    

class class_Abibilities(db.Model):
    class_Abibilities_id = db.Column('class_Abilities_id', db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("classe")
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    def __init__(self, name, description):
        self.name = name
        self.description = description

class class_Attributes(db.Model):
    class_Attributes = db.Column('class_Attributes', db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("class")
    name = db.Column(db.String(50))
    value = db.Column(db.Integer)
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
class class_Skills(db.Model):
    id = db.Column('class_Skills', db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("classe")
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'))
    skill = db.relationship("skill")

class skill(db.Model):
    id = db.Column('skill_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __init__(self, name):
        self.name = name

class race(db.Model):
    id = db.Column('race_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class race_Attributes(db.Model):
    race_Attributes = db.Column('race_Attributes', db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'))
    race = db.relationship("race")
    name = db.Column(db.String(50))
    value = db.Column(db.Integer)
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
class weapon(db.Model):
    weapon_id = db.Column('weapon_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    damage = db.Column(db.Integer)
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class weapon_properties(db.Model):
    id = db.Column('property_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __init__(self, name):
        self.name = name

class weapon_weaponProperties(db.Model):
    id = db.Column('weapon_weaponProperties', db.Integer, primary_key=True)
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapon.weapon_id'))
    weapon = db.relationship("weapon")
    property_id = db.Column(db.Integer, db.ForeignKey('weapon_properties.property_id'))
    weapon_properties = db.relationship("weapon_properties")
    
class armor(db.Model):
    id = db.Column('armor_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    defense_value = db.Column(db.Integer)
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
class background(db.Model):
    id = db.Column('background_id', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __init__(self, name):
            self.name = name

class background_Skills(db.Model):
    id = db.Column('background_Skills', db.Integer, primary_key=True)
    background_id = db.Column(db.Integer, db.ForeignKey('background.background_id'))
    background = db.relationship("background")
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'))
    skill = db.relationship("skill")

    

    
    

with app.app_context():
    db.create_all()
    # users = User('fvpoijnqerp', '4321')
    # db.session.add(users)
    # db.session.commit()
    
    