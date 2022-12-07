from flask import Flask,request
import git 

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello From FLask"

@app.route('/update_server', methods=['POST'])
def webhook():
	print("line no:12")
	if request.method == 'POST':
		print("line no:14")
		repo = git.Repo('./GitTracker')
		print("line no:16")
		origin = repo.remotes.origin
		origin.pull()
		print("line no:19")
		return 'Updated PythonAnywhere successfully', 200
	else:
		print("line no:20")
		return 'Wrong event type', 400

if __name__ == "__main__":
	app.run()
