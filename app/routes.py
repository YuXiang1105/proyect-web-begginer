from flask import Blueprint, render_template
main = Blueprint("main", __name__)

aliens = [
    {
        "name": "xenomorph",
        "danger": "extreme",
        "class": "parasyte",
        "origin": "open space, not confirmed",
        "description": "The Xenomorph is a highly aggressive extraterrestrial species with a unique life cycle and a deadly hunting instinct. It is known for its biomechanical appearance, acid blood, and ability to adapt to various environments. The Xenomorph is a formidable predator that poses a significant threat to any life form it encounters.",
    },
    {
        "name": "Gravis",
        "danger": "Low",
        "class": "Mineral",
        "origin": "Asteroids",
        "description": "Rocky creatures that manipulate gravity around them to move and defend themselves."
    },
    {
        "name": "Luminaris",
        "danger": "Moderate",
        "class": "Energy",
        "origin": "Nebulas",
        "description": "Translucent beings that emit light and communicate through pulses of energy."
    }
]

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home', aliens = aliens)

@main.route('/information')
def information():
    return render_template('information.html', title='User information')

@main.route('/species')
def species():
    return render_template('species.html', title='magic storage')

