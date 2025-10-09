from flask import Blueprint, render_template, redirect, url_for
from .forms import MessageForm
main = Blueprint("main", __name__)

aliens = [
    {
        "Name": "Xenomorph",
        "Danger": "extreme",
        "Class": "parasyte",
        "Origin": "open space, not confirmed",
        "Description": "The Xenomorph is a highly aggressive extraterrestrial species with a unique life cycle and a deadly hunting instinct. It is known for its biomechanical appearance, acid blood, and ability to adapt to various environments. The Xenomorph is a formidable predator that poses a significant threat to any life form it encounters.",
    },
    {
        "Name": "Naytibas",
        "Danger": "Extreme",
        "Class": "Bio-mechanical",
        "Origin": "Earth (post-human epoch)",
        "Description": "he Naytibas are biomechanical alien organisms that invaded Earth, annihilating most of humanity. Their bodies fuse flesh and machinery, capable of regenerating and adapting to combat. They are driven by a hive-like will and worship an ancient entity known as the Elder Naytiba."
    },
    {
        "Name": "Lord of Cinder",
        "Danger": "Extreme",
        "Class": "Humanoid",
        "Origin": "Lordran",
        "Description": "Specie ascended by absorbing a legendary artifact in Lordran, the First flame. After ascending, any specimen becomes extremely powerful, being considered even gods in their planets"
    },
    {
        "Name": "Radiance",
        "Danger": "Extreme",
        "Class": "Parasyte",
        "Origin": None,
        "Description": "A specimen from the kindom of Hallownest, part of a planet of intelligent insects. Survives by invading the mind of other living being, and inducing them to a dream. If the subject is in the dream, Radiance has full control of the body, being able to destroy entire kindoms"
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
            "Name": form.name.data,
            "Danger": form.danger.data,
            "Class": form.class_imput.data,
            "Origin": form.origin.data,
            "Description": form.description.data
        }
        
        aliens.append(new_alien)
        return redirect(url_for('main.species'))
        
        
    return render_template('form.html', aliens = aliens, form =form)
