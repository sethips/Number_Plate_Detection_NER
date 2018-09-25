from flask import Flask
from flask import jsonify
import ner

import argparse
import sys
import json

app = Flask(__name__)
 
@app.route('/')
def hello():
	return "NER extractor for Name, Location, Organization and Number Plate. Please put a query in the link "

@app.route('/<user_input>')
def detect_entities(user_input):
	dict_out = {'Entity': ner.polyglot_ner(user_input)}
	dict_hardcoded_ner = ner.hardcoded_ner(user_input)
	dict_final = dict(dict_out)
	dict_final.update(dict_hardcoded_ner)
	return jsonify(dict_final)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8083)
