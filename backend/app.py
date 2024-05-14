from flask import Flask

app = Flask(__name__)

#add api variables here

#Routes#

#GETs

#landing page/begin game -- not needed, actually
@app.get('/')
def show_homepage():
    """Show game homepage"""
#player data page(name, picture, year)

#results page (correct or incorrect)

#POSTs

#send answer