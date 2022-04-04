import streamlit as st
import pandas as pd
import folium
from folium import Marker
from folium.plugins import HeatMap, MarkerCluster
import math
from streamlit_folium import folium_static

df = pd.read_csv('D:/Kaggle/apartment_data.csv')

st.title('Geospatial Analysis of Apartments in Bangalore')

st.markdown('_This website shows the prices of different apartments in Banglore along with their Geolocation_')
st.markdown('This website is developed by **Suhas C B**')

st.dataframe(df)
df.head()

st.subheader('Geolocation of apartments in Bangalore')
m2 = folium.Map(location=[12.972442, 77.580643], tiles='cartodbpositron', zoom_start=13)

st.markdown('**Hover** on the marker to show the _Name_ of the _Apartment_')
st.markdown('**Click** on the marker to show the _Starting Price_ of the _Apartment_')

mc = MarkerCluster()
for idx, row in df.iterrows():
    if not math.isnan(row['lon']) and not math.isnan(row['lat']):
        tooltip = tooltip = '<strong>' + row['names'] + '</strong>'
        popup = popup = '<strong>' + 'starting price ' + '</strong>' + row['Starting Price']
        mc.add_child(Marker([row['lat'], row['lon']], tooltip=tooltip, popup=popup))

m2.add_child(mc)
folium_static(m2)

selectbox = df['Unit Type'].unique()

selected = st.selectbox('Select the type of apartment you want', selectbox)

Select = df[df['Unit Type'] == selected]

m3 = folium.Map(location=[12.972442, 77.580643], tiles='cartodbpositron', zoom_start=10)


mc = MarkerCluster()
for idx, row in Select.iterrows():
    if not math.isnan(row['lon']) and not math.isnan(row['lat']):
        tooltip = tooltip = '<strong>' + row['names'] + '</strong>'
        popup = popup = '<strong>' + 'starting price ' + '</strong>' + row['Starting Price']
        mc.add_child(Marker([row['lat'], row['lon']], tooltip=tooltip, popup=popup))

m3.add_child(mc)
folium_static(m3)

m4 = folium.Map(location=[12.972442, 77.580643], tiles='cartodbpositron', zoom_start=10)

HeatMap(data=df[['lat', 'lon']], radius=10).add_to(m4)

st.write('Heat Map of Apartments in Bangalore')

folium_static(m4)



