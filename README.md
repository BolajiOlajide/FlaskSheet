# FlaskSheet
This project makes use of Google Spreadsheets as backend for storing information. It is a simple ToDo List application built with Flask.

### INSTALLATION

Before starting up the application locally, you'll need to get your credentials from [Google](https://google.com) and turn on the Google Sheets API. To do this follow the instructions:

- Use [this wizard](https://console.developers.google.com/start/api?id=sheets.googleapis.com) to create or select a project in the Google Developers Console and automatically turn on the API. Click **Continue**, then **Go to credentials**.
- On the **Add credentials** to your project page, click the **Cancel** button.
- At the top of the page, select the **OAuth consent** screen tab. Select an **Email address**, enter a **Product name** if not already set, and click the **Save** button.
- Select the **Credentials** tab, click the **Create credentials** button and select **OAuth client ID**.
- Select the application type **Other**, enter the name "Google Sheets API Quickstart", and click the **Create** button.
- Click **OK** to dismiss the resulting dialog.
- Click the (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it **_client_secret.json_**.

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

**Bolaji Olajide**
