# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request, redirect, url_for
from flask import render_template
from app import app
import pickle
import logging
import json
import requests

logging.basicConfig(format='%(asctime)s : %(levelname)s: %(message)s', level=logging.INFO)

rovi_artist_search_url = "https://9r32j6gkb1.execute-api.eu-west-1.amazonaws.com/default/panda_Rovi-API"
"""
dict_keys(['ids', 'name', 'isGroup', 'primaryMedia', 'musicGenres', 
'movieGenres', 'active', 'birth', 'death', 'country', 'period', 
'headlineBio', 'classicalBio', 'classicalBioUri', 'discography', 
'discographyUri', 'filmography', 'filmographyUri', 'followers', 
'followersUri', 'groupMembers', 'groupMembersUri', 'memberOf', 
'memberOfUri', 'images', 'imagesUri', 'influencers', 'influencersUri', 
'similars', 'similarsUri', 'moods', 'moodsUri', 'movieBio', 
'movieBioUri', 'musicBio', 'musicBioUri', 'musicCredits', 
'musicCreditsUri', 'songs', 'songsUri', 'musicStyles', 
'musicStylesUri', 'themes', 'themesUri', 'videos', 'videosUri', 
'movieStyles', 'movieStylesUri', 'contemporaries', 'contemporariesUri', 
'associatedWith', 'associatedWithUri', 'collaboratorWith', 'collaboratorWithUri', 
'compositions', 'compositionsUri', 'aliases', 'aliasesUri', 'web', 'webUri', 
'factsheets', 'factsheetsUri', 'schedule', 'scheduleUri', 'credits', 'creditsUri'])
"""

def getComponent(metaresult, key):
    component = metaresult[key]
    datalist = []
    if component:
        if isinstance(component, list) and isinstance(component[0], dict):
            datalist = [item['name'] for item in metaresult[key]]
        elif isinstance(component, list):
            datalist = component
    return datalist

@app.route('/<string:name>', methods=['GET', 'POST'])
def index(name):
    response = requests.get(rovi_artist_search_url, params = {"name":name})
    content = json.loads(response.content)
    result = content['searchResponse']['results'][0]
    metaresult = result['name']
    artistname = metaresult['name']
    activedecades = getComponent(metaresult, 'active')
    genres = getComponent(metaresult, 'musicGenres')
    headlinebio = metaresult['headlineBio']
    classicalbio = metaresult['classicalBio']
    followers = getComponent(metaresult, 'followers')
    influencers = getComponent(metaresult, 'influencers')
    similars = getComponent(metaresult, 'similars')
    collaboratorWith = getComponent(metaresult, 'collaboratorWith')
    moods = getComponent(metaresult, 'moods')
    musicStyles = getComponent(metaresult, 'musicStyles')

    return render_template('index_simple.html', 
                            artistname = artistname,
                            activedecades=activedecades,
                            genres = genres,
                            headlineBio = headlinebio,
                            classicalBio = classicalbio,
                            followers = followers,
                            influencers = influencers,
                            similars = similars,
                            moods = moods,
                            musicStyles = musicStyles,
                            collaboratorWith = collaboratorWith
    )

