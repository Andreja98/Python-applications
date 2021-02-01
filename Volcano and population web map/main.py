import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

# Konvertovanje LON i LAT kolona u liste da bi moglo for petljom da se prolazi kroz njih
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

# Definisemo lokaciju na kojoj ce se otvoriti mapa (podeseno na Beograd)
map = folium.Map(location=[44.78, 20.47])

# Dodavanje featureGroup
fg_volcanoes = folium.FeatureGroup(name="Volcanoes")

# Za iteriranje kroz 2 liste istvoremeno koristimo zip metodu. Pojavljuju se vulkani u Americi
for lt, ln, el in zip(lat, lon, elev):
    fg_volcanoes.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color=color(el))))


fg_population = folium.FeatureGroup(name="Population")
# Dodavanje zemalja na mapu i bojenje onih zemalja u plavo koje imaju manje od 10 miliona stanovnika
# POP2005 se nalazi u kategoriji properties
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green'
                                            if x['properties']['POP2005'] < 10000000 else 'orange'
                                            if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())
map.save("Map1.html")
