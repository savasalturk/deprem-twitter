import streamlit as st
import streamlit.components.v1 as components
import folium
from folium.plugins import MarkerCluster
import json

m = folium.Map([37.265763040011514, 36.610105733926865],zoom_start = 10)
folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ).add_to(m)
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
    popup = folium.Popup(iframe, min_width=500, max_width=500)
    marker  = folium.Marker([i["geometry"]["coordinates"][1],i["geometry"]["coordinates"][0]],popup=popup,icon=folium.Icon(color="red", icon="info-sign"))
    marker_cluster.add_child(marker)

#m.save("index.html")
m.fit_bounds(m.get_bounds())



st.set_page_config(layout="wide")
#st.title('Deprem - Yardım istenilen konumlar')
st.markdown("""<h3> Deprem - Yardım İstenilen Konumlar </h3>""",unsafe_allow_html=True)




#a = open("index.html","r",encoding="UTF-8").read()
a = m._repr_html_()
components.html(a,height= 500,scrolling=False)
