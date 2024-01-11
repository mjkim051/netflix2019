from flask import Flask, render_template, request, jsonify
from pathlib import Path

app = Flask(__name__)

examples = [(i, 'ex' + str(i)) for i in range(10)]

import os
import pandas

nf = pandas.read_csv('netflix_titles.csv')
movie_tv_count = nf['type'].value_counts()

rate_count = nf['rating'].value_counts().to_frame()
rate_count.columns = ['count']
rating_count_html = rate_count.to_html()

type_count = nf['type'].value_counts().to_frame()
type_count.columns = ['type']
type_count_html = type_count.to_html()

nf['cast'].value_counts()
d_count = nf['cast'].tail(10).to_frame()
d_count.columns = ['count']
d_count_html = d_count.to_html()

# David_info = nf['cast'].value_counts().to_frame()
# David_info.columns = ['David']
# David_info_html = David_info.to_html()


app = Flask(__name__)



#rec application
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', examples = examples)
    
@app.route('/results')
def result():
    return render_template('results.html', counts = movie_tv_count, rate = rating_count_html)

@app.route('/ex1')
def ex1():
    return render_template('ex1.html', counts = movie_tv_count, rate = rating_count_html, type = type_count_html)

@app.route('/ex2')
def ex2():
    return render_template('ex2.html', d_c = d_count_html)

@app.route('/ex3')
def ex3():
    return render_template('ex3.html')

if __name__ == '__main__':
    app.run(debug = True)