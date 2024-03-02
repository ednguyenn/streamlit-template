import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Mount Duneed")

    m = leafmap.Map(center=[-38.2426, 144.3056], zoom=19)
    m.add_basemap("SATELLITE")
    
    m.to_streamlit(height=700)
