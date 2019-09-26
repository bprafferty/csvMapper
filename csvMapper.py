#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:02:02 2019

@author: brianrafferty
"""

import folium
import pandas as pd
import json
from folium import plugins


def markerMap(info, mapTitle):
    usMap = folium.Map(location=[40,-100], tiles='Stamen Terrain', zoom_start = 4, control_scale=True)

    #for each row in the hashtag dataset, plot the cooresponding lat/lon on the map
    for i,row in info.iterrows():
        folium.Marker(location=[row.latitude,row.longitude], popup=row.tweet_text.decode('utf-8'), icon=folium.Icon(color='red')).add_to(usMap)
    
    legend_html =   '''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 100px; height: 90px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp; <strong>Legend</strong> <br>
                              &nbsp; Tweet &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i>
                </div>
                '''     
    usMap.get_root().html.add_child(folium.Element(legend_html))
    #save the map as an html
    usMap.save(mapTitle + '.html')

def heatMap(info, mapTitle):
    usMap = folium.Map(location=[40,-100], tiles='Stamen Terrain', zoom_start = 4, control_scale=True)

    #for each row in the Starbucks dataset, plot the corresponding lat/lon
    for i, row in info.iterrows():
        folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=0.5).add_to(usMap)
    
    #add the heatmap. The core parameters are:
    #--data: a list of points of the form (latitude, longitude) indicating locations of Starbucks stores

    #--radius: how big each circle will be around each Starbucks store

    #--blur: the degree to which the circles blend together in the heatmap
    usMap.add_child(plugins.HeatMap(data=info[['latitude','longitude']].values, radius=25, blur=10))
    
    #save the map
    usMap.save(mapTitle + '.html')

userFile = raw_input('Enter your csv file path: ')

info = pd.read_csv(userFile)

mapTitle = raw_input('Name your map: ')

print('Choose how to map: \n1 -- Marker Map\n2 -- Heat Map')

mapChoice = raw_input('Enter number for desired map type: ')

if (mapChoice == '1'):
    markerMap(info, mapTitle)

if(mapChoice == '2'):
    heatMap(info, mapTitle)

if (mapChoice != '1' and mapChoice != '2'):
    print('Invalid map number. Choose from available types.')