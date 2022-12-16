from flask import Flask,request
import git 
import os
import requests


username = 'arjun23'
token = '89c97a4b1c2a411708c49137804bb3c364d5a97c'
host = 'arjun23.pythonanywhere.com'

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello From FLask-1.0"

@app.route('/update_server', methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo('./GitTracker/')
		origin = repo.remotes.origin
		origin.pull()
		response = requests.post(
		f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{host}/reload/',
		headers={'Authorization': f'Token {token}'})
		if response.status_code == 200:
			return 'Updated PythonAnywhere successfully', 200
		else:
			return 'Got unexpected status code {}: {!r}'.format(response.status_code, response.content)
	else:
		return 'Wrong event type', 400

if __name__ == "__main__":
	app.run(port=os.environ.get("PORT"))
