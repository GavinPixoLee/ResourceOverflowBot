import os
import pymongo

class Database:
	def __init__(self):
		self.client = pymongo.MongoClient(os.environ['DB_URI'])
		self.database = self.client["ResourceOverflow"]

	def get_resource_types(self):
		return self.database.list_collection_names()

	def get_book_topics(self):
		return self.get_distinct_topics('books')

	def get_course_topics(self):
		return self.get_distinct_topics('courses')

	def get_distinct_topics(self, resource):
		return self.database[resource].distinct("topic")

	def get_books(self, topic):
		return self.search_resource('books', topic)

	def get_courses(self, topic):
		return self.search_resource('courses', topic)

	def search_resource(self, resource, topic):
		return list(self.database[resource].find(
			{"topic": topic},
			{'_id': False}
		))

database = Database()