import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
features = folium.FeatureGroup(name="My Map")

volcanoes = pandas.read_csv("Volcanoes.csv")
for index, row in volcanoes.iterrows():
    features.add_child(folium.Marker(location=[row["LAT"], row["LON"]], popup=row["NAME"], icon=folium.Icon(color="green")))

map.add_child(features)

map.save("Map1.html")