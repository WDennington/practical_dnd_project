from flask import Flask
from os import getenv
import random

app = Flask(__name__)

def roll_dice():
    result = [  
        random.randint(1, 6)
        for n
        in range(4)
    ]
    lowest = min(result)
    result.remove(lowest)
    return sum(result)

@app.route("/gen_stats")
def gen_stats():
    
    strength = roll_dice()
    dexterity = roll_dice()
    constitution = roll_dice()
    intelligence = roll_dice()
    wisdom = roll_dice()
    charisma = roll_dice()
    stats = [
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
    ]

    return stats

@app.route("/gen_gender")
def gen_gender():
    genders = [ 'male', 'female', 'non binary']
    return random.choice(genders)



