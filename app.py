from app import run_app
import platform

HOSTNAME = platform.uname().node

if __name__ == "__main__":
	app = run_app()
	app.run(host=HOSTNAME, debug=True)
