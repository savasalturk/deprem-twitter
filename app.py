import streamlit as st
import streamlit.components.v1 as components
import folium
import json

m = folium.Map([37.265763040011514, 36.610105733926865],zoom_start = 8)
f = open(r"data\v6.geojson","r",encoding="utf-8").read()
js = json.loads(f)
fields = ['1', 'sehir', 'ilce', 'mah', 'Adres', 'Apartman Adı', 'Sokak/Cadde/Bulvar', 'Dış Kapı/Blok', 'İç Kapı', 'Kat', 'isim', 'tel', 'kaynak', 'tel.1', 'adres_birlesik', 'konum', 'x', 'y']
folium.GeoJson(data=js,popup=folium.GeoJsonPopup(fields=fields)).add_to(m)
m.save("index.html")




st.set_page_config(layout="wide")
st.title('Twitter - Deprem')





a = open("index.html","r",encoding="UTF-8").read()

components.html(a,height= 750,scrolling=False)