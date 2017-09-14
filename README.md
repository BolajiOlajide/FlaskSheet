# FlaskSheet
This project makes use of Google Spreadsheets as backend for storing information. It is a simple ToDo List application built with Flask.

### SETUP
- Clone the project from my [github repo](https://github.com/BolajiOlajide/FlaskSheet)
- Change the `.env.sample` file to `.env` and replace the placeholder to the ID of your spreadsheet
- Create your virtual environment
- Install the application's dependencies with the command `pip install -r requirements.txt`
- Start the application with the command: `python main.py`
- Navigate to `localhost:5000` on your browser and the application displays a simple form and table.
- Add a todo list and submit it, the page will be re-rendered and you should see your entry rendered.

### NOTE

When you run the application for the first time, you'll need to authenticate it with your google account.
Once this is done, access to the spreadsheet is confirmed and all will work fine.

### Notes

- Authorization information is stored on the file system, so subsequent executions will not prompt for authorization.
- The authorization flow in this example is designed for a command-line application. For information on how to perform authorization in a web application, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/api-client-library/python/auth/web-app).

### Author

*Bolaji Olajide*
