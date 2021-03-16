"""This is the main flask app file"""
from flask import Flask, render_template
import names

app = Flask(__name__)

def generate_names(numberofnames):
    """Generate random names"""
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())
        print(i)

    return nlist

namelist = generate_names(50)

@app.route('/')
def home():
    """Render Homepage"""
    return render_template('home.html', namelist=namelist)
