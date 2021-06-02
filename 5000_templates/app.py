from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import requests
import os

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" #os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    char_class = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(20), nullable=False)
    # strength = db.Column(db.Integer, nullable=False)
    # constitution = db.Column(db.Integer, nullable=False)
    # dexterity = db.Column(db.Integer, nullable=False)
    # wisdom = db.Column(db.Integer, nullable=False)
    # intelligence = db.Column(db.Integer, nullable=False)
    # strength = db.Column(db.Integer, nullable=False)

db.create_all()


@app.route('/')
def home():
    name = requests.get('http://name_class:5001/gen_name')
    char_class = requests.get('http://name_class:5001/gen_class')
    race = requests.get('http://name_class:5001/gen_race')
    stats = requests.post('http://character:5003/gen_stats')
    all_chars = Characters.query.all()

    db.session.add(
        Characters(
            name = name.text,
            char_class = char_class.text,
            race = race.text,
            # strength = stats["strength"],
            # dexterity = stats["dexterity"],
            # constitution = stats["constitution"],
            # intelligence = stats["intelligence"],
            # wisdom = stats["wisdom"],
            # charisma = stats["charisma"]
        )
    )
    db.session.commit()

    return render_template('index.html', 
        name=name.text,
        char_class=char_class.text,
        race=race.text,
        # strength = stats["strength"],
        # dexterity = stats["dexterity"],
        # constitution = stats["constitution"],
        # intelligence = stats["intelligence"],
        # wisdom = stats["wisdom"],
        # charisma = stats["charisma"],
        # all_chars = all_chars
        
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)