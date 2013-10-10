import tornado.web
import requests
import json
from model.schema import Schema

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class SchemaHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        self._schema = Schema().response_data()

    def get(self):
        self.write(self._schema)
    
    def put(self):
        r = requests.put("http://localhost:9200/processos/")
        payload = self._schema
        r = requests.put("http://localhost:9200/processos/processo/_mapping", data=json.dumps(payload))

def url_specs():
    return [
        (r'/', MainHandler),
        (r'/schema', SchemaHandler),
    ]