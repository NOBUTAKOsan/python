import json
from datetime import datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o): # pylint: disable=method-hidden
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)