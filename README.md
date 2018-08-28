# FlaskTutorial
Collection of simple Flask webpages(https://hello-thatflippingfool.herokuapp.com/)

How to create the "Hello World!" page
---
#### STEP 1 - Make the following Flask python "app.py" script in the new directory you want your project to be in:
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()
```
#### STEP 2 - At the root of the directory, create a python environment to set up web app dependencies:
```
pipenv install  # create Pipfile and Pipfile.lock which list the project dependencies
pipenv install flask  # add flask as a dependency to the project and Pipfile
pipenv install gunicorn  # add gunicorn as a dependency to the project and Pipfile
```
#### STEP 3 - Create an extensionless Procfile that tells heroku how to run your web app:
```
echo 'web: gunicorn app:app' > Procfile
```
#### STEP 4 - Check that it works on local host in your browser
```
python app.py
```
#### STEP 5 - Upload into a remote Git repository and deploy on Heroku!
