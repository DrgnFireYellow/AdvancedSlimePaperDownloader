import requests
import streamlit as st

st.write("# AdvancedSlimePaper Downloader")

BASE_URL = "https://api.infernalsuite.com/v1/projects/asp/"

minecraft_version = st.text_input("Please enter the Minecraft version you would like to download ASP for: ", "1.21.4")

build_data = requests.get(f"{BASE_URL}mcversion/{minecraft_version}").json()[0]


for file in build_data["files"]:
    st.write(f"{file['fileName']}: [Download]({BASE_URL}{build_data['id']}/download/{file['id']})")