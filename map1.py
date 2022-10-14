import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
volcanoes = folium.FeatureGroup(name="US Volcanoes")

volcano_data = pandas.read_csv("Volcanoes.csv")
lats = list(volcano_data["LAT"])
lons = list(volcano_data["LON"])
elevs = list(volcano_data["ELEV"])
names = list(volcano_data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

for lat, lon, elev, name in zip(lats, lons, elevs, names):
    volcanoes.add_child(folium.CircleMarker(location=[lat, lon],
        radius=7,
        popup=f'{name} - {elev}m',
        color='gray',
        weight=2,
        fill_color=color_producer(elev),
        fill_opacity=1))

populations = folium.FeatureGroup(name="World Populations")
populations.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(volcanoes)
map.add_child(populations)
map.add_child(folium.LayerControl())

map.save("Map1.html")