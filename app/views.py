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
@app.route('/<string:name>', methods=['GET', 'POST'])
def index(name):
    response = requests.get(rovi_artist_search_url, params = {"name":name})
    content = json.loads(response.content)
    result = content['searchResponse']['results'][0]
    metaresult = result['name']
    


    return render_template('index_simple.html', 
                            artistname = metaresult['name'],
                            activedecades = '\n'.join(metaresult['active']),
                            genres = metaresult['musicGenres'],
                            headlineBio = metaresult['headlineBio'],
                            classicalBio = metaresult['classicalBio'],
                            followers = metaresult['followers'],
                            influencers = metaresult['influencers'],
                            similars = metaresult['similars'],
                            moods = metaresult['moods'],
                            musicStyles = metaresult['musicStyles'],
                            collaboratorWith = metaresult['collaboratorWith']
    )

