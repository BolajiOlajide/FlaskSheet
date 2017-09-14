from flask import Flask, render_template, redirect, url_for

from sheets import get_credentials, read, write
from forms import AddTodoForm


app = Flask(__name__)
app.config['DEBUG'] = True

credentials = get_credentials()

@app.route('/', methods=['GET', 'POST'])
def home():
	form = AddTodoForm(csrf_enabled=False)
	todos = read(credentials)
	if form.validate_on_submit():
		data = []
		name = form.name.data
		description = form.description.data
		status = form.status.data
		data.extend((name, description, status))
		final = []
		final.append(data)
		write(credentials, final)
		return redirect(url_for('home'))
	return render_template('index.html', todos=todos, form=form)


if __name__ == '__main__':
	app.run(debug=True)
	