# Import Flask and templates
from flask import Flask
from flask import render_template

# Create Flask object
app = Flask(__name__)


# Url addresses are assigned by function decoration
@app.route('/')
@app.route('/index')
def index():

    # Generate html
    return render_template('index.html', message='Hello World!')


# Enable python script to be executable
if __name__ == "__main__":
    app.run()
