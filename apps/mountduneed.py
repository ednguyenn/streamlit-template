import streamlit as st
import leafmap.foliumap as leafmap
import leafmap

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
    m.draw_control()

    if m.user_roi_bounds() is not None:
        bbox = m.user_roi_bounds()
        image = "satellite.tif"
        tms_to_geotiff(output=image, bbox=bbox, zoom=20, source="Satellite", overwrite=True)
        m.layers[-1].visible = False  # turn off the basemap
        m.add_raster(image, layer_name="Image")
        sam = LangSAM()
        text_prompt = "tree"
        sam.predict(image, text_prompt, box_threshold=0.24, text_threshold=0.24)
        sam.show_anns(
            cmap='Greens',
            add_boxes=False,
            alpha=0.5,
            title='Automatic Segmentation of Trees',
)
        m.to_streamlit(height=700)   
        
 