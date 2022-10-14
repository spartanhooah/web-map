import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
features = folium.FeatureGroup(name="My Map")

volcanoes = pandas.read_csv("Volcanoes.csv")
lats = list(volcanoes["LAT"])
lons = list(volcanoes["LON"])
elevs = list(volcanoes["ELEV"])
names = list(volcanoes["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

for lat, lon, elev, name in zip(lats, lons, elevs, names):
    features.add_child(folium.Circle(location=[lat, lon], radius=5000, popup=f'{name} - {elev}m', color='gray', weight=2, fill_color=color_producer(elev), fill_opacity=1))
map.add_child(features)

map.save("Map1.html")