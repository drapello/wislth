class Schema(object):

    def response_data(self):
        return {
                  "processo" : {
                        "properties" : {
                            "titulo" : {"type" : "string", "store" : "yes"},
                            "descricao" : {"type" : "string", "store" : "yes"},
                            "autor" : {"type" : "string", "store" : "yes"}
                        }
                  }
              }