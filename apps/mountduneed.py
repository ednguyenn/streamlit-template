import streamlit as st
import leafmap.foliumap as leafmap

from samgeo import tms_to_geotiff, split_raster
from samgeo.text_sam import LangSAM

def app():

    st.title("mount-duneed")

    ##to do: create a GPTAPI to retrieve the latitude and longitude of a input location
    latitude = -38.2426
    longitude = 144.3056
    m = leafmap.Map(center=[latitude, longitude], zoom=19)
    m.add_basemap("SATELLITE")
    
    m.to_streamlit(height=700)

    if m.user_roi_bounds() is not None:
        bbox = m.user_roi_bounds()
    else: bbox = [-95.3704, 29.6762, -95.368, 29.6775]