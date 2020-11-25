import numpy as np
import pandas as pd
import seaborn as sns
import folium
import webbrowser
from folium.plugins import HeatMap

f=pd.read_csv("mapa.csv",sep=';')
num = 95
lat = np.array(f["Latitude"][0:num])
lon = np.array(f["Longitude"][0:num])
js = np.array(f["Acidentes"][0:num],dtype=float)
data1 = [[lat[i],lon[i],js[i]] for i in range(num)]

map_osm = folium.Map(location=[-23.550,-46.650],zoom_start=11,control_scale=True)
lay1=folium.map.FeatureGroup(name="Marcadores", overlay=True, control=True, show=True).add_to(map_osm)
lay2=folium.map.FeatureGroup(name="HeatMap", overlay=True, control=True, show=True).add_to(map_osm)
HeatMap(data1,control=True).add_to(lay2)
for i in range (num):
    pop=folium.map.Popup(html=f["Distrito"][i]+ " "+ "Acidentes:" + str(f["Acidentes"][i]))
    folium.map.Marker([lat[i],lon[i]],popup=pop).add_to(lay1)

folium.map.LayerControl(position='topright', collapsed=True, autoZIndex=True).add_to(map_osm)
file_path = r"C:/Users/vhpad/Desktop/Acidentes_de_bicicleta_version2.html"
map_osm.save(file_path)
webbrowser.open(file_path)