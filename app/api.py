from flask import Blueprint, request, make_response, jsonify
from werkzeug.exceptions import HTTPException
from jsonschema import ValidationError
from flask_expects_json import expects_json
from .validate_and_generate import payload_generator, valid_ip, valid_port

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
	},
	'required': ['host', 'port', 'lang']
}


@api.route('api', methods=['POST'])
@expects_json(schema)

def api_logic():

	if(request.data):

		poll = request.get_json()

		ip = poll['host']
		port = poll['port']
		lang = poll['lang']

		supported_langs = ["bash", "python", "perl", "php", "awk"]

		if valid_ip(ip) == True and valid_port(port) == True:
			if lang in supported_langs:
				return payload_generator(ip, port, lang, "n", True)
			else:
				return {"Error":"Unsupported lang value!"}, 400
		else:
			return {"Error":"Invalid IP or Port!"}, 400
	else:
		return {"Error":"Post Failed"}, 400
