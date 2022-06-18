# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:56:27 2022

@author: jpthoma
"""

from flask import Flask,render_template

app = Flask(__name__,template_folder="templates")

@app.route("/")
#@app.route("/home")

def home():
    return render_template("index.html")


#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():
    return "Waka Waka!"


if __name__=="__main__":
    app.run(debug=True)