from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/skill/')
def skill_drill():
	return 'Did the skill drill work?'