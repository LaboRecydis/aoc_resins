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

    st.title("Echantillons AOC mai 2023")

    st.write("Auteur : Brahim AIT OUALI  - Technicien chimiste")
  
   
    # Display the LOGO
    img1 = Image.open("IMG_PAPREC.jpg")
    img2 = Image.open("IMG_RECYDIS.jfif") 
    
  
    st.sidebar.image(img1, width=250)
    st.sidebar.image(img2, width=250)

    st.write(" * ## cuve N°1")
    st.write("* Liquide acide PH<1")
    cuve1=Image.open("cuve1.jpg")
    st.image(cuve1, width=700)


    st.write(" * ## cuve N°2")
    st.write("* Mélange acide + solvant")
    cuve1=Image.open("cuve2.jpg")
    st.image(cuve1, width=700)

    st.write(" * ## Echantillon R15 ")
    st.write("* Résine très visqueuse")
    R15=Image.open("R15.jpg")
    st.image(R15, width=700)

    video_file = open('R15_video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.write(" * ## Echantillon R16 ")
    st.write("* L'échantillon est devenu dur")
    R15=Image.open("R16.jpg")
    st.image(R15, width=700)
    
    video_file = open('R16_video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.write(" * ## Echantillon R20 ")
    st.write("* Liquide visquex")
    R20=Image.open("R20.jpg")
    st.image(R20, width=700)
    
    video_file = open('R20_video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.write(" * ## Eau glycolée ")
    st.write("* Liquide de PH = 7, il y a  1 GRV 1000L (ARF)")

    st.write(" * ## Eaux poluées ")
    st.write("* eaux souillées de résine (odeur de résine) , PH = 7, il y a 9 GRV 1000L.")
    eau_poluee=Image.open("eau_poluee.jpg")
    st.image(eau_poluee, width=700)

    st.write(" * ## Déchet résineux, il y a 1 GRV")
    st.write("* Echantillon visqueux, la partie supéreiure de l'échantillon  a durci. En bas liquide non acide")
    
    st.write(" * ## Déchet scrubber G19, il y a 1 GRV ")
    st.write("* Résine liquide visqueuse, PH acide = le PH vire au rouge quelques instants aprés.")

    st.write(" * ## E 252 polué, il y a 4 GRV ")
    st.write("* Résine liquide un peu visqueuse")
    st.write("* GRV N°1 : l'échantillon en majorité liquide mais avec une petite partie solide")
    st.write("* GRV N°2 : l'échantillon a durci en majorité")
    st.write("* GRV N°3 et 4 : résine liquide visqueuse")

    st.write(" * ## Déchet G 019 R 001, il y a 3 GRV .")
    st.write("* Les échantillons ne sont pas acide.")
    st.write("* GRV N°1 : résine visqueuse + solvant")
    st.write("* GRV N°2 : liquide de PH neutre trés visqueux")
    st.write("* GRV N°3 : solvant")

    st.write(" * ## Déchet E271 + B 110, il y a 2 fûts .")
    st.write("* solvant non acide.")

