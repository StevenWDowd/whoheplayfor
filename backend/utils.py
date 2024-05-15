from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playercareerstats
import pydash
import pandas

all_players = players.get_players()
#all_teams = teams.get_teams()
headshot_url_stub = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/'

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

def get_player_season(id):
    """Takes a player ID and returns a dict representing a season from that
    player's career, like so:


    'PLAYER_ID': [201167],
    'SEASON_ID': ['2015-16'],
    'LEAGUE_ID': ['00'],
    'TEAM_ID': [1610612752],
    'TEAM_ABBREVIATION': ['NYK'],
    'PLAYER_AGE': [30.0],
    'GP': [71],
    'GS': [57],
    'MIN': [2371.0],
    'FGM': [354],
    'FGA': [799],
    'FG_PCT': [0.443],
    'FG3M': [91],
    'FG3A': [238],
    'FG3_PCT': [0.382],
    'FTM': [110],
    'FTA': [131],
    'FT_PCT': [0.84],
    'OREB': [23],
    'DREB': [243],
    'REB': [266],
    'AST': [144],
    'STL': [25],
    'BLK': [10],
    'TOV': [82],
    'PF': [142],
    'PTS': [909]}"""

    career = playercareerstats.PlayerCareerStats(player_id=id)

    seasons_table = career.get_data_frames[0]

    season = seasons_table.sample().to_dict('list')

    return season

#def get_team(id):
    """Takes a team ID and returns a team dict like so:
    {'id': 1610612752,
    'full_name': 'New York Knicks',
    'abbreviation': 'NYK',
    'nickname': 'Knicks',
    'city': 'New York',
    'state': 'New York',
    'year_founded': 1946}"""

def generate_question_data(player, season):
    """Returns a dictionary on a player, containing information needed
    for the front end."""
    player_team = teams.find_team_name_by_id(season['TEAM_ID'][0])

    player_id_str = str(player['id'])

    player_headshot = f'{headshot_url_stub}{player_id_str}.png'

    question_dict = {
        'player_name': player['full_name'],
        'season': season['SEASON_ID'][0],
        'team' : player_team,
        'img_source': player_headshot,
    }

    return question_dict







