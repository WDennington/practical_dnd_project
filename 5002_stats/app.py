from flask import Flask, jsonify
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

@app.route("/gen_stats", methods=['GET'])
def gen_stats():
    
    strength = roll_dice()
    dexterity = roll_dice()
    constitution = roll_dice()
    intelligence = roll_dice()
    wisdom = roll_dice()
    charisma = roll_dice()
    

    return jsonify([strength, dexterity, constitution, intelligence, wisdom, charisma])

if __name__ == "__main__": app.run(host="0.0.0.0", port=5002, debug=True)
