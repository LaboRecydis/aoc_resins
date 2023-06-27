import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import json
#import plotly.express as px
import altair as alt





if __name__=="__main__":
    st.set_page_config(
        page_title="Streamlit basics app",
        layout="centered"
    )

    st.title("Inventaire gaz")

    st.write("Auteur : Brahim AIT OUALI  - Technicien chimiste")
  
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    
  
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)

    
    st.write(" * ## Butane / Propane")
    
    st.write("* Première partie : détail sur la vidéo")
    video_file = open('prop-1_zmdZtHeY.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Deuxième partie : détail sur la vidéo")
    video_file = open('PROP_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Troisième partie : détail sur la vidéo")
    video_file = open('PROP_3.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Quatième partie")
    img_PROP_4 = Image.open("PROP_4.jpg")
    st.image(img_PROP_4, width=700)
    
    st.write("* Cinquième partie ")
    img_PROP_5 = Image.open("PROP_5.jpg")
    st.image(img_PROP_5, width=700)
    
    st.write("* Sixième partie : détail sur la vidéo")
    video_file = open('PROP_6.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("------------------------------------------------ ")
    
    st.write(" * ## Helium")
    st.write("* Première partie")
    img_He_1 = Image.open("He_1.jpg")
    st.image(img_He_1, width=700)
    
    st.write("* Deuxième partie : détail sur la vidéo")
    st.write("Détail sur la vidéo")
    video_file = open('He_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("------------------------------------------------ ")
  
    st.write(" * ## CO2")
    img_CO2 = Image.open("CO2.jpg")
    st.image(img_CO2, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## N2")
    img_N2 = Image.open("N2.jpg")
    st.image(img_N2, width=700)
    
    st.write("------------------------------------------------ ")
       
    st.write(" * ## O2")
    st.write("* Première partie ")
    img_O2_1 = Image.open("O2_1.jpg")
    st.image(img_O2_1, width=700)
    
    st.write("* Deuxième partie : détail sur la vidéo")
    video_file = open('02_1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Troisiemière partie : détail sur la vidéo")
    video_file = open('O2_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Quatrième partie ")
    img_O2_3 = Image.open("O2_3.jpg")
    st.image(img_O2_3, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## CCl2F2")
    img_CCL2F2 = Image.open("CCL2F2.jpg")
    st.image(img_CCL2F2, width=700)
    
    st.write("------------------------------------------------ ")
        
    st.write(" * ## UN3501")
    st.write("* Première partie")
    img_CCL2F2 = Image.open("UN3501_2.jpg")
    st.image(img_CCL2F2, width=700)
    
    st.write("* Deuxième partie : détail sur la vidéo")
    video_file = open('UN3501.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
            
   
    st.write("------------------------------------------------ ")
    
    st.write(" * ## Bouteilles de protoxyde d'azote N2O ")
    st.write("* Première partie (les grandes) : détail sur la vidéo")
    video_file = open('N20_1.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("* Deuxième partie (les petites) : 12 caisses 600L pleines, détail sur la vidéo")
    video_file = open('NO2_2.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("------------------------------------------------ ")
    
    st.write(" * ## 58 cartouches de propylène ")
    st.write("* Détail sur la vidéo")
    video_file = open('PROPYLENE.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
    st.write("------------------------------------------------ ")
    
    st.write(" * ## Cartouches sodastream")
    img_soda = Image.open("soda.jpg")
    st.image(img_soda, width=700)



  
    



