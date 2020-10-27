from top_five_app import app

from flask import render_template

# Default home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/topfive')
def testRoute():
    names = ['Kid Cudi','xxxtentacion','Earl Sweatshirt','21','Baby Keem']
    return render_template('topfive.html',list_names = names)
    #adding context to this template, this context is going to be names

@app.route('/about')
def about():
    return render_template('about.html')