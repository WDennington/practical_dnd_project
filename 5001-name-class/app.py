from flask import Flask
from os import getenv
import random

app = Flask(__name__)

@app.route("/gen_name")
def gen_name():
    names = ['Al E. Gater', 'Funder Dew Drop', 'ah chew', 'chimpo shumpooli', 'Sam "The pie flinger" jones',
            'wumbo toot', 'bibble', 'eggbert headington', 'droop', 'Lou Sirr']
    return random.choice(names)



@app.route("/gen_class")
def gen_class():
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rouge', 'Sorcerer', 'Warlock', 'Wizard', 'Artificer']
    return random.choice(classes)

