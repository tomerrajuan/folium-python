
print("hola")
import json
import os

import folium
import requests

map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# global tooltip
tooltip="click for more info"

# Ceate custom marker icon
# logoIcon=folium.features.CustomIcon("tiger.jpg", icon_size=(40, 40))

# Vega data
vis= os.path.join("data", "vis.json")

# create markers
folium.Marker([42.363600, -71.099500], 
            popup='<h1>location one </h1>',
            tooltip=tooltip).add_to(map),
folium.Marker([42.333600, -71.099500], 
            popup='<h1>location Two </h1>',
            icon=folium.Icon(icon="cloud")).add_to(map),
folium.Marker([42.177120, -71.062400], 
            popup='<h1>location Three </h1>',
            icon=folium.Icon(color="purple")).add_to(map),
folium.Marker([42.374150, -71.122410], 
            popup='<h1>location Four </h1>',
            icon=folium.Icon(color="purple", icon="leaf")).add_to(map),
# folium.Marker([42.375140, -71.032450], 
#             popup='<h1>location five </h1>',
#             icon=logoIcon).add_to(map),
folium.Marker([42.315140, -71.072450], 
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),width=450,height=250))).add_to(map)

folium.PolyLine(
    locations=[
         [42.466, -70.943],
         [42.465, -70.910],
         [42.470, -70.888]
        ],
    color='red',
    fill=False).add_to(map)

# cicrle marker
folium.CircleMarker(
    location=[42.466479,-70.942110],
    radius=50,
    popup="a circle",
    color="#428bca",
    fill=True,
    fill_color="#428bca",
    
).add_to(map)



map.save('map.html')
