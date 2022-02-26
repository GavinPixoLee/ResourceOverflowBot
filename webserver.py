from flask import Flask
from threading import Thread
from backend import api

app = Flask('app')

@app.route('/')
def main():
	return "Webserver Online"

app.register_blueprint(api)

def run():
	app.run(host="0.0.0.0", port=8080)

def start():
	server = Thread(target=run)
	server.start()