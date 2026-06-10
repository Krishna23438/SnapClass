import streamlit as st
import base64
from pathlib import Path

def header_home():
   logo_path = Path(__file__).parent.parent / "logo.jpg"
   

   with open(logo_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

   st.markdown(f"""
        
      
        <div style="display:flex;flex-direction:column; align-items:center;justify-content:center;margin-bottom:30px">
            <img src="data:image/jpeg;base64,{encoded}" height="100">
            <h1 style ='text-align:center; color:#E0E3FF'>SNAP<br/> CLASS </h1>
        </div>
        


        """,unsafe_allow_html=True)