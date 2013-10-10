import json

class Processo():

    _mapping_name = "processo"

    def __init__(self):
        self.titulo=""
        self.descricao=""
        self.autor=""
        self.data=""

    def __classname__(self):
        return self.__module__[self.__module__.rindex(".")+1:]


    def mapping(self):
        return {
                "titulo" : {"type" : "string", "store" : "yes"},
                "descricao" : {"type" : "string", "store" : "yes"},
                "autor" : {"type" : "string", "store" : "yes"},
                "data" : {"type" : "date", "store" : "yes"}
                }