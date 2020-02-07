import requests
from bs4 import BeautifulSoup

artist_list = []
title_list = []

track_list = zip(title_list, artist_list)
track_dict = {}


with open('project-file/shazam.min.html', 'r') as shazamFile:
    shazamSoup = BeautifulSoup(shazamFile, 'html.parser')

    # get div with class title
    for trackTitle in shazamSoup.find_all('div', attrs={'class':'title'}):
        title_list.append(trackTitle.find('a').contents[0])

    # get div with class artist
    for trackArtist in shazamSoup.find_all('div', attrs={'class':'artist'}):
        if trackArtist.find('a') != None:
            artist_list.append(trackArtist.find('a').contents[0])


track_dict.update(list(track_list))
print(len(track_dict))