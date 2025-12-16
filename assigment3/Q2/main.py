import streamlit as st
import requests
import os
from dotenv import load_dotenv

# ---------------- Load Environment ----------------
load_dotenv()

API_KEY = os.getenv("OPENWEATHER")
URL = "https://api.openweathermap.org/data/2.5/weather"

# ---------------- Session State Init ----------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------------- Login Page ----------------
def login_page():
    st.title(" Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == password and username != "":
            st.session_state.logged_in = True
            st.session_state.page = "weather"
            st.success("Login Successful")
        else:
            st.error("Invalid Login")


# ---------------- Weather Page ----------------
def weather_page():
    st.title(" Weather App")

    city = st.text_input("Enter City Name")

    if st.button("Get Weather"):
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            response = requests.get(URL, params=params)
            data = response.json()

            if str(data.get("cod")) == "200":
                st.subheader(f"Weather in {city}")
                st.write(" Temperature:", data["main"]["temp"], "°C")
                st.write(" Humidity:", data["main"]["humidity"], "%")
                st.write(" Wind Speed:", data["wind"]["speed"], "m/s")
                st.write(" Condition:", data["weather"][0]["description"])
            else:
                st.error(data.get("message", "Invalid City"))
        else:
            st.warning("Please enter a city name")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "thanks"


# ---------------- Thank You Page ----------------
def thanks_page():
    st.title(" Thank You")
    st.write("You have logged out successfully.")


# ---------------- Main Controller ----------------
if st.session_state.logged_in:
    weather_page()
elif st.session_state.page == "login":
    login_page()
else:
    thanks_page()