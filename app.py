from flask import Flask
from flask import render_template

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route('/')
def index():
    name_data = None
    return render_template('index.html', name=name_data)



# TO RUN APP - type "flask run" into TERMINAL