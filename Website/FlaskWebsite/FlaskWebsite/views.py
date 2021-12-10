"""
Routes and views for the flask application.
"""

from datetime import datetime, timedelta
from flask import request, redirect
from flask import render_template
from flask import Flask, make_response, send_file
from flask.wrappers import Response

import csv
from datetime import datetime
import io
from io import StringIO
import pandas as pd

from FlaskWebsite import app
from FlaskWebsite.data.twitter import get_tweets

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
    twitterId = request.form['TwitterId']
    dateFrom = request.form['DateFrom']
    dateTo = request.form['DateTo']
    dfTweeets = get_tweets(twitterId, dateFrom, dateTo)

    # your code
    return render_template(
        'index.html',
        title='Election Corpus',
        DateFrom=datetime.now().date() - timedelta(days=7),
        DateTo=datetime.now().date(),
        candidate_list = get_candidate(),
        column_names= dfTweeets.columns.values,
        tweets = list(dfTweeets.values.tolist())
    )

@app.route('/download_corpus', methods=['POST'])
def download_corpus():
    twitterId = request.form['TwitterId']
    dateFrom = request.form['DateFrom']
    dateTo = request.form['DateTo']
    dfTweeets = get_tweets(twitterId, dateFrom, dateTo)

    dateToday = datetime.now()
    resp = make_response(dfTweeets.to_csv(sep ='\t'))
    resp.headers["Content-Disposition"] = f'attachment; filename={twitterId}-{dateToday}.csv'
    resp.headers["Content-Type"] = "text/csv"
    return resp

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