import tornado.web
import requests
import json
from infra.es import *
from model.processo import *
import pyes


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class ProcessoHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        self.es = ElasticSearch()

    def get(self):
        q = pyes.StringQuery("", default_operator="AND")
        import pdb; pdb.set_trace()
        result = self.es.conn.search(query=q, indices=[self.es.index])
        self.write(result)
    
    def post(self):
        self.write(self._schema)
    
    def put(self):
        self.write(self._schema)

    def delete(self):
        self.write(self._schema)

class SchemaHandler(tornado.web.RequestHandler):
    
    def initialize(self):
        self._schema = ElasticSearch().mapping(Processo())

    def get(self):
        self.write(self._schema)

def url_specs():
    return [
        (r'/', MainHandler),
        (r'/schema', SchemaHandler),
        (r'/processo', ProcessoHandler),
    ]