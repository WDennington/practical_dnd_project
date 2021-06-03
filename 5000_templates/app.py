from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import requests
import os


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    char_class = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(20), nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
db.drop_all()
db.create_all()


@app.route('/')
def home():
    name = requests.get('http://name_class:5001/gen_name')
    char_class = requests.get('http://name_class:5001/gen_class')
    race = requests.get('http://name_class:5001/gen_race')
    stats = requests.get('http://stats:5002/gen_stats')
    
    payload = dict(stats=stats.json(), char_class=char_class.text)
    stats_class = requests.post('http://character:5003/gen_char', json=payload)
    
    
    strength, dexterity, constitution, intelligence, wisdom, charisma = stats_class.json()
    new_char =  Characters(
            name = name.text,
            char_class = char_class.text,
            race = race.text,
            strength = strength,
            dexterity = dexterity,
            constitution = constitution,
            intelligence = intelligence,
            wisdom = wisdom,
            charisma = charisma
        )
    db.session.add(new_char)
    db.session.commit()
    all_chars = Characters.query.limit(5).all()
    return render_template('index.html', 
        name=name.text,
        char_class=char_class.text,
        race=race.text,
        strength = strength,
        dexterity = dexterity,
        constitution = constitution,
        intelligence = intelligence,
        wisdom = wisdom,
        charisma = charisma,
        all_chars = all_chars
        
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)