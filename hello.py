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

if __name__ == "__main__":
	app.run()

