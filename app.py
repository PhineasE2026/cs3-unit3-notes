from flask import Flask, render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route('/')
def index():
    name_data = 'Jimothy Bumblebottoms'
    year_data = 2026
    favorites_list = ['Glarfle', 'Sprocket', 'Zibble', 'Wobble', 'Flibber', 'Gizmo', 'Blimgog', 'Snorfle', 'Quibble', 'Dingle', 'Zazzle']
    ratings_dict = {
        'Mango': 'I rate this mango, a 3/10.',
        'Pineapple': 'This pineapple is a 4/10.',
        'Strawberry': 'I do not like this strawberry, it is a 1/10.',
        'Watermelon': 'This watermelon is not good. I give it a 2/10.',
        'Blueberry': 'No, this blueberry is a 0/10. I do not like it at all.'
    }


    # name is how we refer to it in the HTML template,
    # name_data is the variable declared here in python
    return render_template('index.html', name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict)

@app.route('/submit')
def submit():
        form_data = {
            'name': request.form.get('name'),
            'age': request.form.get('age'),
            'hobby': request.form.get('hobby'),
            'color': request.form.get('color'),
            'lucly': request.form.get('lucky')
        }

        return render_template('results.html', form_data=form_data)


def about():
    return render_template('about.html')

def contact():
    return render_template('contact.html')



# TO RUN APP - type "flask run" into TERMINAL