from flask import Flask, jsonify, request




app = Flask(__name__)

@app.route('/gen_char', methods=['POST'])
def gen_char():
    char_class=request.json['char_class']
    stats=request.json['stats']
    strength, dexterity, constitution, intelligence, wisdom, charisma = stats  
    if char_class == 'Dwarf':
        constitution += 2
    elif char_class == 'Elf' or char_class == 'Halfling':
        dexterity += 2
    elif char_class == 'Gnome':
        intelligence += 2
    elif char_class == 'Human':
        strength += 1
        dexterity += 1
        constitution += 1
        intelligence += 1
        wisdom += 1
        charisma += 1 
    return jsonify([strength, dexterity, constitution, intelligence, wisdom, charisma])



if __name__ == "__main__": app.run(host="0.0.0.0", port=5003, debug=True)