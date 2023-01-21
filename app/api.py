from flask import Blueprint, request, make_response, jsonify
from werkzeug.exceptions import HTTPException
from jsonschema import ValidationError
from flask_expects_json import expects_json
from .utils import payload_generator, valid_ip, valid_port

# Blueprinting to allow for modular code.
api = Blueprint("api", __name__)

# Return JSON for ValidationError errors.
@api.errorhandler(400)
def bad_request(error):
	if isinstance(error.description, ValidationError):
		original_error = error.description
		return make_response(jsonify({'error': original_error.message}), 400)
	# Else return HTML error as JSON.
	else:
		response = {
			"error code": error.code,
			"name": error.name,
			"description": error.description,
		}
		return response, 400

# Required JSON Schema for host submission data.
schema = {
    'type': 'object',
    'properties': {
		'host': {'type': 'string'},
		'port': {'type': 'number'},
		'lang': {'type': 'string'},
		'shell': {'type': 'string'},
	},
	'required': ['host', 'port', 'lang', 'shell']
}


@api.route('api', methods=['POST'])
@expects_json(schema)

def api_logic():

	if not request.data:
		return {"Error":"Post Failed"}, 400

	poll = request.get_json()

	ip = poll['host']
	port = poll['port']
	lang = poll['lang']
	shell = poll['shell']

	supported_langs = ["bash", "python", "perl", "php", "awk"]
	supported_shells = ["bash", "sh", "csh", "ksh", "zsh"]
	
	is_valid_ip = valid_ip(ip)
	is_valid_port = valid_port(port)

	if (not is_valid_ip) or (not is_valid_port):
		first = "Invalid IP" if (not is_valid_ip) else ""
		and_string = " and " if (not is_valid_ip and not is_valid_port) else ""
		second = "Invalid Port" if (not is_valid_port) else ""
		return {"Error": first + and_string + second}, 400

	if lang not in supported_langs:
		return {"Error":"Unsupported lang value!"}, 400
	if shell not in supported_shells: 		
		return {"Error": "Unsupported shell value!"}, 400

	return payload_generator(ip, port, lang, "n", shell, True)

