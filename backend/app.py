from flask import Flask, jsonify
from utils import get_random_player, get_player_season, generate_question_data

app = Flask(__name__)

#add api variables here

#Routes#

#GETs

#landing page/begin game -- not needed, actually
@app.get('/player')
def get_new_player():
    """Returns a dictionary of a player in a season of their career.
    """
    player = get_random_player()
    season = get_player_season(player['id'])
    question_dict = generate_question_data(player, season)

    return jsonify(question_dict)

# @app.post('/player')
# def check_player_answer():
#     """"""
#player data page(name, picture, year)

#results page (correct or incorrect)

#POSTs

#send answer