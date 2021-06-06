from flask import Flask
import random

app = Flask(__name__)
names = ['Al E. Gater', 'Funder Dew Drop', 'Ah Chew', 'Chimpo Shumpooli', 'Sam "The pie flinger" Jones',
            'Wumbo Toot', 'Bibble', 'Eggbert Headington', 'Droop', 'Lou Sirr', 'Dalton Brul']
@app.route("/gen_name", methods=['GET'])
def gen_name():
    return random.choice(names)


classes = ['Barbarianv2', 'Bardv2', 'Clericv2', 'Druidv2', 'Fighterv2', 'Monkv2', 'Paladinv2', 'Rangerv2', 'Rougev2', 'Sorcererv2', 'Warlockv2', 'Wizardv2']
@app.route("/gen_class", methods=['GET'])
def gen_class():
    return random.choice(classes)

races = ['Dwarven Brute', 'High Elf', 'Gnomish Street Urchin', 'Halfling of Bagend', 'Human of Stormwind']
@app.route("/gen_race", methods=['GET'])
def gen_race():
    return random.choice(races)

if __name__ == "__main__": app.run(host="0.0.0.0", port=5001, debug=True)