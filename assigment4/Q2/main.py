import streamlit as st
import pandas as pd
import os
from datetime import datetime


# CSV Files

user_file = "user.csv"
files_file = "userfiles.csv"

if not os.path.exists(user_file):
    pd.DataFrame(columns=["userid", "username", "password"]).to_csv(user_file, index=False)

if not os.path.exists(files_file):
    pd.DataFrame(columns=["userid", "filename", "upload_datetime"]).to_csv(files_file, index=False)


# Session state initialization

if "is_authenticate" not in st.session_state:
    st.session_state.is_authenticate = False
    st.session_state.userid = None
    st.session_state.username = None


# Sidebar Menu

with st.sidebar:
    st.header("Menu")

    if not st.session_state.is_authenticate:
        mode = st.selectbox("Select", ["Home", "Login", "Register"])
    else:
        mode = st.selectbox("Select", ["Explore CSV", "See History", "Logout"])

# Home Page

if mode == "Home":
    st.title("Welcome...")
    st.write("Please Login or Register to continue.")

# Register Page

elif mode == "Register":
    st.title("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        users_df = pd.read_csv(user_file)

        if username in users_df["username"].values:
            st.error("Username already exists")
        else:
            userid = len(users_df) + 1
            new_user = pd.DataFrame(
                [[userid, username, password]],
                columns=["userid", "username", "password"]
            )
            users_df = pd.concat([users_df, new_user], ignore_index=True)
            users_df.to_csv(user_file, index=False)
            st.success("Registration successful! Please login.")

# Login Page

elif mode == "Login":
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users_df = pd.read_csv(user_file)

        user = users_df[
            (users_df["username"] == username) &
            (users_df["password"] == password)
        ]

        if not user.empty:
            st.session_state.is_authenticate = True
            st.session_state.userid = int(user.iloc[0]["userid"])
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")


# Explore CSV Page

elif mode == "Explore CSV":
    st.title("Upload & Explore CSV")
    st.write(f"Logged in as: **{st.session_state.username}**")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        history_df = pd.read_csv(files_file)
        new_entry = pd.DataFrame(
            [[st.session_state.userid, uploaded_file.name, datetime.now()]],
            columns=["userid", "filename", "upload_datetime"]
        )

        history_df = pd.concat([history_df, new_entry], ignore_index=True)
        history_df.to_csv(files_file, index=False)

        st.success("File uploaded and history saved")


# See History Page

elif mode == "See History":
    st.title("Your Upload History")

    history_df = pd.read_csv(files_file)
    user_history = history_df[history_df["userid"] == st.session_state.userid]

    if user_history.empty:
        st.info("No uploads yet")
    else:
        st.dataframe(user_history)


# Logout

elif mode == "Logout":
    st.session_state.is_authenticate = False
    st.session_state.userid = None
    st.session_state.username = None
    st.success("Logged out successfully")
    st.rerun()