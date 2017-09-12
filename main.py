from flask import Flask, render_template

from sheets import get_credentials, read


app = Flask(__name__)

credentials = get_credentials()

@app.route('/')
def home():
	todos = read(credentials)
	print(todos)
	return render_template('index.html', todos=todos)


if __name__ == '__main__':
	app.run(debug=True)
	