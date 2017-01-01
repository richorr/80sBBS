import json
class User:	
	def __init__(self, userkey, name):
		self.userkey = userkey
		self.name = name

def jdefault(o):
	if isinstance(o, set):
		return list(o)
	return o.__dict__

def save(user):
	return json.dumps(user, default=jdefault)

def object_hook_handler(parsed_dict):
	return User(userkey=parsed_dict['userkey'], name=parsed_dict['name'])

def load(userjson):
	return json.loads(userjson, object_hook=object_hook_handler)
