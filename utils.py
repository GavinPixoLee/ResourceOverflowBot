import requests

api_endpoint = "https://ResourceOverflowBot.pixo.repl.co/api"

def get_topics_from_type(type):
	return requests.get(f"{api_endpoint}/{type}/topics").json()

def get_resources_list(type, topic):
	return requests.get(f"{api_endpoint}/{type}/{topic}").json()

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
