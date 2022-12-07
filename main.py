from flask import Flask,request
import git 

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello From FLask"

@app.route('/update_server')
def webhook():
	try:
		repo = git.Repo('./')
		origin = repo.remotes.origin
		origin.pull()
		return 'Updated PythonAnywhere successfully', 200
	except:
		print("line no:20")
		return 'Wrong event type', 400

if __name__ == "__main__":
	app.run()
