from flask import Flask
import git 

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello From FLask"

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

if __name__ == "__main__":
	app.run()
