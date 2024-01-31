import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Michael Klassen - Data Analyst", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

# --- Load Assets ---
lottie_data = "https://lottie.host/adb125c8-62d2-46d0-98af-b614cf6854a5/u9i9XkplED.json"
img_F1Dashboard = Image.open("images/Dashboard.png")
img_F1Relations = Image.open("images/Relations.png")

# --- HEADER SECTION ---
with st.container():
    st.subheader("Hi, I am Michael :wave:")
    st.title("A Data Analyst from germany")
    st.write("I am passionate about finding ways to squeeze the last bit of performance out of your data!")
    st.write("[Learn more and reach out on LinkedIn: >](https://www.linkedin.com/in/michael-klassen-5ab5b7147/)")

# --- WHAT I DO ---


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a Data Analyst who wants to bring essential value for your business! 
            To help with tasks as 
            - gathering data from different systems, spreadsheets, databases, etc. 
            - transform the data in usable form 
            - clean the to improve the significance
            - provide the data to given visualization tools
            - visualize the data so YOU can make smart, data-driven decisions
            
            I use programming languages, tools and techniques such as
            - Python
            - SQL
            - Excel
            - PowerBI
            """
        )

    with right_column:
        st_lottie(lottie_data, height=500, key="coding")


# --- PROJECTS

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_F1Dashboard)
        st.image(img_F1Relations)
        
    with text_column:
        st.subheader("Formula 1 End-To-End Webscraping Project")
        st.write(
            """
            I created this project trying to showcase all different kinds of skills and tools I'm offering. 
            - I startet gathering 
            """
        )
        
    