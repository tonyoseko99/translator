import requests
import os
import uuid
import json
from dotenv import load_dotenv
from flask import Flask, redirect, url_for, request, render_template, session

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    # read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['REGION']

    # indicate that we want to translate and the API verson (3.0) and the target language
    path = '/translate?api-version=3.0'

    # add the target language parameter
    target_language_parameter = '&to=' + target_language

    # create the full url
    constructed_url = endpoint + path + target_language_parameter

    # setup the header information which includes the subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    # Create the body of the request with the text to be translated
    body = [{'text': original_text}]

    # Make the call using post
    translator_request = requests.post(
        constructed_url, headers=headers, json=body)

    # Retrieve the JSON response
    translator_response = translator_request.json()

    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )
