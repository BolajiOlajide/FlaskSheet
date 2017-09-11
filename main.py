from flask import Flask, render_template

from sheets import get_credentials, read

app = Flask(__name__)
credentials = get_credentials()

@app.route('/')
def home():
	details = read(credentials)
	return render_template('index.html', details=details)

if __name__ == '__main__':
	app.run(debug=True)
	