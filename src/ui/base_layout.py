import streamlit as st

def style_background_home():
  st.markdown("""
        <style>
              .stApp{
                background:#5865F2 !important;
              }

              .stApp div[data-testid="stColumn"]{
              background-color:#E0E3FF!important;
              padding:2.5rem !important;
              border-radius:5rem !important;
              }
        </style>  

  
            """,unsafe_allow_html=True)


def style_background_dashboard():
  st.markdown("""
        <style>
              .stApp{
                background:#E0E3FF !important;
              }
        </style>  

  
            """,unsafe_allow_html=True)

def style_base_layout():
# asdasd
  st.markdown("""
        <style>
              
            @import url('https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&family=Baloo+Bhaina+2:wght@400..800&family=Climate+Crisis:YEAR@1979&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&family=Roboto+Slab:wght@100..900&family=Roboto:ital,wght@0,100..900;1,100..900&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap');
              
            @import url('https://fonts.googleapis.com/css2?family=Arimo:ital,wght@0,400..700;1,400..700&family=Baloo+Bhaina+2:wght@400..800&family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&family=Roboto+Slab:wght@100..900&family=Roboto:ital,wght@0,100..900;1,100..900&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap');
              
            /* hide Top Bar of streamlit*/
              #MainMenu,header, footer{
                visibility:hidden;
              }
              .block-container{
                  padding-top:1.5rem !important;
              }

              h1{
                  font-family: 'Climate Crisis',sans-serif !important;
                  font-size: 3.5rem ! important;
                  line-height: 1.1rem , !important;
                  margin-bottom:0rem !important
                  color:#E0E3FF !important;
              }
              h2{
                  font-family: 'Climate Crisis',sans-serif !important;
                  font-size: 2rem ! important;
                  line-height: 0.9rem , !important;
                  margin-bottom:0rem !important
                  color:#E0E3FF 
              }
              h3, h4, p{
                font-family:'Outfit', sans-serif
              }

              button{
                  border-radius: 1.5rem !important;
                  background: #5865F2 !important;
                  color: white !important;
                  padding: 10px 20px !important
                  tansition: transform 0.25s ease-in-out !important;
              }
              button[kind="secondary"]{
                  border-radius: 1.5rem !important;
                  background: #EB459E !important;
                  color: white !important;
                  padding: 10px 20px !important
                  tansition: transform 0.25s ease-in-out !important;
              }
              button[kind="tertiary"]{
                  border-radius: 1.5rem !important;
                  background: black !important;
                  color: white !important;
                  padding: 10px 20px !important
                  tansition: transform 0.25s ease-in-out !important;
              }

              button:hover{
                transform: scale(1.05)
              }
        </style>  

  
            """,unsafe_allow_html=True)