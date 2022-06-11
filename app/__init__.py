from flask import Flask

# Returns the main app.
def run_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = "All-Your-Base-Are-Belong-To-Us"

	# Main index routes.
	from app.index import index
	app.register_blueprint(index, url_prefix="/")

	# Main api route.
	#from app.api import api
	#app.register_blueprint(routes, url_prefix="/")

	return app
