# Import Flask module
from flask import Flask

# Create Flask object
app = Flask(__name__)


# Url addresses are assigned by function decoration
@app.route('/')
def index():

    # Generate html
    return '<h1>Hello World!</h1>'


# Enable python script to be executable
if __name__ == "__main__":
    app.run()