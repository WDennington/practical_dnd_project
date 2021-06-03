from flask import Flask
import random

app = Flask(__name__)

@app.route("/gen_name", methods=['GET'])
def gen_name():
    names = ['Al E. Gater', 'Funder Dew Drop', 'Ah Chew', 'Chimpo Shumpooli', 'Sam "The pie flinger" Jones',
            'Wumbo Toot', 'Bibble', 'Eggbert Headington', 'Droop', 'Lou Sirr']
    return random.choice(names)



@app.route("/gen_class", methods=['GET'])
def gen_class():
    classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rouge', 'Sorcerer', 'Warlock', 'Wizard', ]
    return random.choice(classes)

@app.route("/gen_race", methods=['GET'])
def gen_race():
    races = ['Dwarf', 'Elf', 'Gnome', 'Halfling', 'Human']
    return random.choice(races)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)