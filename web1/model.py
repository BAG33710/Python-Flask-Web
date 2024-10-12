from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class Character(db.Model):
    character_id = db.Column('character_id',db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("class.class_id"), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'), nullable=False)
    background_id = db.Column(db.Integer, db.ForeignKey('background.background_id'), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class User(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Classes(db.Model):
    class_is = db.Column(db.Integer)
    class_name = db.Column(db.String(50))

class Class_Abibilities(db.Model):
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.class_id'))
    ability_name = db.Column(db.String(50))
    ability_description = db.Column(db.String(50))

class Class_Attributes(db.Model):
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.class_id'))
    ability_name = db.Column(db.String(50))
    ability_value = db.Column(db.Integer)
    
class Class_Skills(db.model):
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.class_id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('Skills.skill_id'))

class Skills(db.Model):
    skill_id = db.Column('skill_id', db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50))

class Race(db.Model):
    race_id = db.Column('race_id', db.Integer, primary_key=True)
    race_name = db.Column(db.String(50))

class Race_Attributes(db.Model):
    race_id = db.Column(db.Integer, db.ForeignKey('Race.race_id'))
    attribute_name = db.Column(db.String(50))
    attribute_value = db.Column(db.Integer)

class Weapon(db.Model):
    weapon_id = db.Column('weapon_id', db.Integer, primary_key=True)
    weapon_name = db.Column(db.String(50))
    damage = db.Column(db.Integer)

class Weapon_properties(db.Model):
        property_id = db.Column('property_id', db.Integer, primary_key=True)
        property_name = db.Column(db.String(50))

class Weapon_weaponProperties(db.Model):
    weapon_id = db.Column(db.Integer, db.ForeignKey('Weapon.weapon_id'))
    property_id = db.Column(db.Integer, db.ForeignKey('Weapon_properties.property_id'))
    
class Armor(db.Model):
        armor_id = db.Column('armor_id', db.Integer, primary_key=True)
        armor_name = db.Column(db.String(50))
        defense_value = db.Column(db.Integer)
        
class Background(db.Model):
    background_id = db.Column('background_id', db.Integer, primary_key=True)
    background_name = db.Column(db.String(50))
    
class Background_Skills(db.Model):
    background_id = db.Column(db.Integer, db.ForeignKey('Background.background_id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('Skills.skill_id'))
    

    

    
    

with app.app_context():
    db.create_all()
    users = User('fvpoijnqerp', '4321')
    db.session.add(users)
    db.session.commit()
    
    