#!/usr/bin/python
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")

def hello_world():
	return "Hey now brown cow"


#dynamic route 
@app.route("/search/<search_query>")
def search(search_query):
	return "i know im idiot but {}".format(search_query)

#dynamic rout with URL types 
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1 
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"
#added 
@app.route("/name/<name>")
def index(name):
	if name.lower() == "mohammad":
		return "Hello, {}".format(name)
	else:
		return "Not Found!", 404


if __name__ == "__main__":
	app.run()

