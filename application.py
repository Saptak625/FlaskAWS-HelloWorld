from flask import Flask
application = Flask(__name__)

@application.route('/')
@application.route("/home")
def hello_world():
	return 'Hello World'