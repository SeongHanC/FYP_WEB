import json

json_string = """{"Event Suppliers":[
	{"state":"Selangor"}
]}"""

input_s = json.loads(json_string)
print input_s['Event Suppliers']