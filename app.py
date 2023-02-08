import streamlit as st
import streamlit.components.v1 as components
import folium
from folium.plugins import MarkerCluster
import json

m = folium.Map([37.265763040011514, 36.610105733926865],zoom_start = 8,crs='EPSG4326')
marker_cluster = MarkerCluster().add_to(m)
f = open("data/v6.geojson","r",encoding="utf-8").read()
js = json.loads(f)
#fields = ['1', 'sehir', 'ilce', 'mah', 'Adres', 'Apartman Adı', 'Sokak/Cadde/Bulvar', 'Dış Kapı/Blok', 'İç Kapı', 'Kat', 'isim', 'tel', 'kaynak', 'tel.1', 'adres_birlesik', 'konum', 'x', 'y']
#folium.GeoJson(data=js,popup=folium.GeoJsonPopup(fields=fields)).add_to(marker_cluster)

for i in js["features"]:
    ht = []
    
    for j in list(i["properties"].items()):
        html = """<br> <strong>{} : </strong> {}</br>""".format(j[0],j[1])
        ht.append(html)
    iframe = folium.IFrame("".join(ht))
    popup = folium.Popup(iframe, min_width=300, max_width=500)
    folium.Marker(i["geometry"]["coordinates"],popup=popup).add_to(marker_cluster)
m.save("index.html")




st.set_page_config(layout="wide")
st.title('Twitter - Deprem')





a = open("index.html","r",encoding="UTF-8").read()

components.html(a,height= 750,scrolling=False)
