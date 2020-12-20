#!/bin/python3
# -*- coding: utf-8 -*-
'''
    author: LiuQiu
'''

from flask import Flask,request,render_template,session,redirect,url_for,abort,make_response,flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY',"secret_key")
app.config["WTF_I18N_ENABLED"]= False

@app.route('/')
def index():
    response = make_response(render_template("instal.html"))
    return response

@app.route('/flash')
def just_flash():
    flash('I am flash,Who is looking for me.') 
    return redirect(url_for("index"))

@app.route('/hi/<name>')
@app.route('/hi,defaults={"name": "Programmer"}')
def hi(name):
    return render_template('hello.html',name=name)