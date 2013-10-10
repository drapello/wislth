from pyes import *

class ElasticSearch():

	def __init__(self):
		self.index = "processos"
		self.conn = ES('127.0.0.1:9200')
		try:
			self.conn.create_index(self.index)
		except exceptions.IndexAlreadyExistsException:
			print "index exists"
			pass
		self.conn.default_indices=[self.index]

	def mapping(self,obj):
		self.conn.put_mapping(obj.__classname__(), {'properties':obj.mapping()}, [self.index])
		return self.conn.get_mapping(obj.__classname__(), self.index).as_dict()

	def save(self, obj):
		self.conn.index(obj.to_json(), self.index, obj.__classname__(), 1)

