from flask import render_template
from app import app
import requests
import json


@app.route('/')
@app.route('/index')
def index():

    current_games = []
    match_list = []
    fmatch_list = []
    goals_list_h = []
    goals_list_a = []

    games = requests.get('http://worldcup.sfg.io/matches/').json()
    games_n = requests.get('http://worldcup.sfg.io/matches/current').json()
    for game in games:
        if game['status'] in ('in progress'):
            current_games.append(game)
			
    for game in games:
        if game['status'] in ('completed'):
            match_list.append(game)
			
    for game in games:
        if game['status'] in ('future'):
            fmatch_list.append(game)
			
    for goals in games_n:
        for g in goals['home_team_events']:
            if g['type_of_event'] == 'goal':
                goals_list_h.append(g['player'] +' '+ g['time'])
					
    for goals in games_n:
        for g in goals['away_team_events']:
            if g['type_of_event'] == 'goal':
                goals_list_a.append(g['player'] +' '+ g['time'])
	
    
	
    return render_template('index.html' ,title='World Cup 2018', match_list=match_list, current_games=current_games,fmatch_list=fmatch_list, goals_list_a=goals_list_a, goals_list_h=goals_list_h)