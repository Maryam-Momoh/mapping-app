import folium
import pandas

map = folium.Map(location=[48.85, 2.35], tiles="Mapbox Bright", zoom_start=2)
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgm = folium.FeatureGroup(name="Marker layer")

for lt, ln, el in zip(lat, lon, elev):
    fgm.add_child( folium.CircleMarker( location=[lt, ln], popup=str(el)+" m", fill_color=color_producer(el),
    fill=True, color="gray", radius=6, opacity=0.7))

fgp = folium.FeatureGroup(name="Population layer")

fgp=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), 
style_function = 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")