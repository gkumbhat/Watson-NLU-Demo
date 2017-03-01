from flask import (Flask, render_template, Response, request,
    Blueprint, redirect, send_from_directory, send_file, jsonify, g, url_for, flash)
from splash import *
from main import app
import json
import pdb
import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

splash = Blueprint('splash', __name__, template_folder="templates")

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    use_vcap_services=True)

@splash.route('/')
def index():
    return render_template('home.html')

@splash.route('/analyze', methods=['POST'])
def analyze():
    inputType = request.form['button']
    if inputType == "Text":
        input = request.form['text-analysis']
        concepts = nlu.analyze(text=input, features=[features.Concepts()])
        # categories = nlu.analyze(text=input, features=[features.Categories()])
    else:
        input = request.form['url-analysis']
        concepts = nlu.analyze(url=input.strip(), features=[features.Concepts()])
        # categories = nlu.analyze(url=input.strip(), features=[features.Categories()])

    return jsonify({'concepts': concepts["concepts"]})


