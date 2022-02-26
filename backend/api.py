from flask import Blueprint, jsonify
from .database import database

api = Blueprint("api", 'app', url_prefix="/api")

@api.route('/resources')
def resources():
	return jsonify(database.get_resource_types()), 200

@api.route('/books/topics')
def book_topics():
	return jsonify(database.get_book_topics()), 200

@api.route('/courses/topics')
def course_topics():
	return jsonify(database.get_course_topics()), 200

@api.route('/books/<string:topic>')
def books(topic):
	return jsonify(database.get_books(topic)), 200

@api.route('/courses/<string:topic>')
def courses(topic):
	return jsonify(database.get_courses(topic)), 200