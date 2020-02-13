import json
from bs4 import BeautifulSoup

artist_list = []
title_list = []

track_list = zip(title_list, artist_list)
track_dict = {}


with open('project-file/shazam.html', 'r') as shazamFile:
    shazamSoup = BeautifulSoup(shazamFile, 'html.parser')

    # get `details` div
    details = shazamSoup.find_all('div', attrs={'class':'details'})

    for i in details:
        # loop through `details` div and get `artist` div
        artist = i.find('div', attrs={'class':'artist'})

        # loop through `artist` div and get a.text
        try:
            artist_list.append(" ".join(artist.a.text.split()))
        except AttributeError:
            artist_list.append(" ")


        # loop through `details` div and get `title` div
        title = i.find('div', attrs={'class':'title'})

        # loop through `title` div and get a.text
        try:
            title_list.append(" ".join(title.a.text.split()))
        except AttributeError:
            title_list.append(" ")

track_dict.update(list(track_list))

with open('./track-list.json', 'w') as trackFile:
    trackFile.write(json.dumps(track_dict))