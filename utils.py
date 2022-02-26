import requests

api_endpoint = "https://ResourceOverflowBot.pixo.repl.co/api"

def get_resource_types():
	return requests.get(f"{api_endpoint}/resources").json()

def get_books_topics():
	return requests.get(f"{api_endpoint}/books/topics").json()

def get_courses_topics():
	return requests.get(f"{api_endpoint}/courses/topics").json()

def get_distinct_book(btopic):
	return requests.get(f"{api_endpoint}/books/" + btopic).json()

def get_distinct_course(ctopic):
	return requests.get(f"{api_endpoint}/courses/" + ctopic).json()
