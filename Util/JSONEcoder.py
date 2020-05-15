from json import JSONEncoder

class JSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__