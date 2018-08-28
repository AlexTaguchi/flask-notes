# FlaskTutorial
Collection of simple Flask webpages(https://hello-thatflippingfool.herokuapp.com/)

How to create the "Hello World!" page
---
STEP 1 - Make the following Flask python "app.py" script in a new directory you want your project to be in:
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
return 'Yo, it works!'

if __name__ == "__main__":
app.run()

STEP 2 - At the root of the directory, create a python environment to set up web app dependencies:
Type - "pipenv install" (create Pipfile and Pipfile.lock which list
the project dependencies)
Type - "pipenv install flask" (add flask as a dependency to the
project and Pipfile)
Type - "pipenv install gunicorn" (add gunicorn as a dependency to the
project and Pipfile)

STEP 3 - Create an extensionless "Procfile" that tells heroku how to run your web app:
Make an extensionless file "Procfile" and put in the following:
web: gunicorn app:app

STEP 4 - Check that it works locally by typing "python app.py" and check your browser

STEP 5 - Create a new app on Heroku and follow the git instructions to upload
