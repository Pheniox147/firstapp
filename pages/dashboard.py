import streamlit as st 
from matplotlib import image
import pandas as pd
import os
 
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_interest= os.path.join(PARENT_DIR,"resources")

Image_path=os.path.join(dir_interest,"titanic.jpg")
Data_path=os.path.join(dir_interest,"titanic.csv")

st.title("Dashboard-TITANIC SURVIVORS")
st.snow()
img = image.imread(Image_path)
st.image(img)

df =pd.read_csv(Data_path)
st.dataframe(df)