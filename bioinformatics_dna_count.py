#Import libraries
from tkinter import image_names
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#Page Title
image = Image.open('dna.jpeg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')




