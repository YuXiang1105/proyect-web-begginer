from flask import Blueprint, render_template
from .forms import MessageForm
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
    return render_template('index.html', aliens = aliens)

@main.route('/information')
def information():
    return render_template('information.html')

@main.route('/species')
def species():
    return render_template('species.html', aliens = aliens)

@main.route('/form' ,methods =['GET', 'POST'])
def form():
    form = MessageForm()
    name = None
    class_imput = None
    origin = None
    danger = None
    description = None
    
    new_alien={}
    
    if form.validate_on_submit():
        
        new_alien = {
            "name": form.name.data,
            "danger": form.danger.data,
            "class": form.class_imput.data,
            "origin": form.origin.data,
            "description": form.description.data
        }
        
        aliens.append(new_alien)
        
        
    return render_template('form.html', class_imput = class_imput,name = name,
        form = form,origin = origin, danger = danger, description = description, aliens = aliens)
