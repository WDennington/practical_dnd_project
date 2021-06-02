from flask import Flask
import requests


app = Flask(__name__)

@app.route('/gen_char', methods=['POST'])
def gen_char():
    stats = requests.get('http://5002-stats_api:5003/gen_stats')
    char_class = requests.get('http://5001-name-class_api:5001/gen_class')
    if char_class == 'Dwarf':
        stats["constitution"] += 2
    elif char_class == 'Elf' or char_class == 'Halfling':
        stats["dexterity"] += 2
    elif char_class == 'Gnome':
        stats["intelligence"] += 2
    elif char_class == 'Human':
        stats["strength"] += 1
        stats["dexterity"] += 1
        stats["constitution"] += 1
        stats["intelligence"] += 1
        stats["wisdom"] += 1
        stats["charisma"] += 1 
    else:
        return stats   
    return stats



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)