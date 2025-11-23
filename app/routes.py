from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import newClass, log_in_form, register_form
from .models import Alien
from . import db
from .models import User

main = Blueprint("main", __name__)
auth = Blueprint("auth", __name__)

#Data of the username, in the future, we will sumbit it to the database

#I used an array to store every alien
"""
aliens = [
    {"Name": "Xenomorph",
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
        "Description": "The Naytibas are biomechanical alien organisms that invaded Earth, annihilating most of humanity. Their bodies fuse flesh and machinery, capable of regenerating and adapting to combat. They are driven by a hive-like will and worship an ancient entity known as the Elder Naytiba."
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
    },
    {
        "Name": "Darkin",
        "Danger": "High",
        "Class": "Destructor",
        "Origin": "Runaterra",
        "Description": "From the planet Runaterra, they are considered fallen ascended in their worlds. Their minds have become corrupted by the endless wars in their lands. Known for their destructive nature, all darkins have been imprisioned in weapons"
    },
    {
        "Name": "Na'vi",
        "Danger": "Low",
        "Class": "humanoid",
        "Origin": "Pandora",
        "Description": "The Na'vi, from Pandora, are considered one of the few intelligent species in their planet. They posses a 'braid' that connects to other creatures and plants of their planet. They have bioluminescent markings on their skin and emi-prehensile tails. Their appearence posses some feline-like physical traits,including large eyes and swiveling ears.    "
    }
]
"""
@main.route('/')
@main.route('/index')
def index():
    aliens = Alien.query.all()
    return render_template('main/index.html', aliens = aliens)


@main.route('/information')
def information():
    return render_template('main/information.html')

@main.route('/species')
def species():
    aliens = Alien.query.all()
    return render_template('main/species.html', aliens = aliens )
