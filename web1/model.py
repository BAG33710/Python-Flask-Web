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
    def __init__(self, username, password):
        self.username = username
        self.password = password

class user(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class classe(db.Model):
    class_id = db.Column('class_id', db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))

class class_Abibilities(db.Model):
    class_Abibilities_id = db.Column('class_id', db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("classe")
    ability_name = db.Column(db.String(50))
    ability_description = db.Column(db.String(50))

class class_Attributes(db.Model):
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("class")
    ability_name = db.Column(db.String(50))
    ability_value = db.Column(db.Integer)
    
class class_Skills(db.model):
    class_id = db.Column(db.Integer, db.ForeignKey('classe.class_id'))
    classe = db.relationship("classe")
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'))
    skill = db.relationship("skill")

class skill(db.Model):
    skill_id = db.Column('skill_id', db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50))

class race(db.Model):
    race_id = db.Column('race_id', db.Integer, primary_key=True)
    race_name = db.Column(db.String(50))

class race_Attributes(db.Model):
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'))
    race = db.relationship("race")
    attribute_name = db.Column(db.String(50))
    attribute_value = db.Column(db.Integer)

class weapon(db.Model):
    weapon_id = db.Column('weapon_id', db.Integer, primary_key=True)
    weapon_name = db.Column(db.String(50))
    damage = db.Column(db.Integer)

class weapon_properties(db.Model):
        property_id = db.Column('property_id', db.Integer, primary_key=True)
        property_name = db.Column(db.String(50))

class weapon_weaponProperties(db.Model):
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapon.weapon_id'))
    weapon = db.relationship("weapon")
    property_id = db.Column(db.Integer, db.ForeignKey('weapon_properties.property_id'))
    weapon_properties = db.relationship("weapon_properties")
    
class armor(db.Model):
        armor_id = db.Column('armor_id', db.Integer, primary_key=True)
        armor_name = db.Column(db.String(50))
        defense_value = db.Column(db.Integer)
        
class background(db.Model):
    background_id = db.Column('background_id', db.Integer, primary_key=True)
    background_name = db.Column(db.String(50))
    
class background_Skills(db.Model):
    background_id = db.Column(db.Integer, db.ForeignKey('background.background_id'))
    background = db.relationship("background")
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'))
    

    

    
    

# with app.app_context():
#     db.create_all()
#     users = User('fvpoijnqerp', '4321')
#     db.session.add(users)
#     db.session.commit()
    
    