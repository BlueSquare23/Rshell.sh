import pytest
from flask import json

# Test api route.
def test_api(app, client):
	# GET Request tests.
	response = client.get('/api')
	assert response.status_code == 405	# Return's 405 to GET requests.

	# POST Request tests.

	# Lang test func.
	def test_lang(lang):
		response = client.post(
			'/api', 
			data=json.dumps({"host":"127.0.0.1","port":12345,"lang":f"{lang}", "shell":"bash"}), 
			content_type='application/json'
		)
		return response

	response = test_lang("bash")
	assert response.status_code == 200	# Return's 200 to POST requests.

	response = test_lang("python")
	assert response.status_code == 200	# Return's 200 to POST requests.

	# Payloads get to unweildy to test for response.text to each.
	response = test_lang("perl")
	assert response.status_code == 200	# Return's 200 to POST requests.

	response = test_lang("php")
	assert response.status_code == 200	# Return's 200 to POST requests.

	response = test_lang("awk")
	assert response.status_code == 200	# Return's 200 to POST requests.

	# Test failures.

	# Bad port.
	response = client.post(
		'/api', 
		data=json.dumps({"host":"127.0.0.1","port":"fart","lang":"bash", "shell":"bash"}), 
		content_type='application/json'
	)

	assert response.status_code == 400	# Return's 400 to bad port.
	assert response.text == '{"error":"\'fart\' is not of type \'number\'"}\n'

	response = client.post(
		'/api', 
		data=json.dumps({"host":"127.0.0.1","port":77777777777777,"lang":"bash", "shell":"bash"}), 
		content_type='application/json'
	)

	assert response.status_code == 400	# Return's 400 to bad port.
	assert response.text == '{"Error":"Invalid IP or Port!"}\n'

	# Bad host.
	response = client.post(
		'/api', 
		data=json.dumps({"host":"127.0.0","port":1234,"lang":"bash", "shell":"bash"}), 
		content_type='application/json'
	)

	assert response.status_code == 400	# Return's 400 to bad host.
	assert response.text == '{"Error":"Invalid IP or Port!"}\n'

	response = client.post(
		'/api', 
		data=json.dumps({"host":"wopaguz","port":1234,"lang":"bash", "shell":"bash"}), 
		content_type='application/json'
	)

	assert response.status_code == 400	# Return's 400 to bad host.
	assert response.text == '{"Error":"Invalid IP or Port!"}\n'
