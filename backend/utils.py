from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playercareerstats
import pydash

all_players = players.get_players()

def get_random_player():
    """Retrieves a random player from NBA history.
    Players are dicts like the following example:
    {'id': 201167,
    'full_name': 'Arron Afflalo',
    'first_name': 'Arron',
    'last_name': 'Afflalo',
    'is_active': False}
    """
    target_player = pydash.sample(all_players)
    return target_player

def get_player_seasons(id):
    """"""
