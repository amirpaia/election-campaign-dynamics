"""
Routes and views for the flask application.
"""

from datetime import datetime, timedelta
from flask import request, redirect
from flask import render_template
from flask.wrappers import Response
from FlaskWebsite import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Election Corpus',
        DateFrom=datetime.now().date() - timedelta(days=7),
        DateTo=datetime.now().date(),
        candidate_list = get_candidate()
    )

@app.route('/create_corpus', methods=['POST'])
def create_corpus():
    TwitterId = request.form['TwitterId']

    # your code
    return render_template(
        'index.html',
        title='Election Corpus',
        DateFrom=datetime.now().date() - timedelta(days=7),
        DateTo=datetime.now().date(),
        candidate_list = get_candidate(),
        response = 1
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )



def get_candidate():
    candidate_list = {
        'n_arthaud': 'Nathalie Arthaud',
        'upr_asselineau': 'Francois Asselineau',
        'dupontaignan': 'Nicolas Dupont-Aignan',
        'Anne_Hidalgo':'Anne Hidalgo',
        'yjadot':'Yannick Jadot',
        'jeanlassalle':'Jean Lassalle',
        'MLP_officiel':'Marine Le Pen',
        'JLMelenchon':'Jean-Luc Melenchon',
        'montebourg':'Arnaud Montebourg',
        'jfpoisson78':'Jean-Frederic Poisson',
        'PhilippePoutou':'Philippe Poutou',
        'Fabien_Roussel':'Fabien Roussel'
    }
    return candidate_list