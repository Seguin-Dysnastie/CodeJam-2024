import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import plotly.express as px
import main
import classification as cl
import matplotlib.pyplot as plt
import numpy as np
#Size ajustor

st.markdown(
    """
    <style>
    /* Base font size for the entire app */
    html, body, [class*="stMarkdown"], [class*="stTitle"], [class*="stHeader"], [class*="stText"] {
        font-size: 24px; /* Adjust this value to globally increase text size */
    }
    
    /* Increase size of headings */
    h1 {
        font-size: 2.5rem !important;   
    }
    h2 {
        font-size: 2rem !important;
    }
    h3 {
        font-size: 1.75rem !important;
    }

    /* Sidebar text size */
    .sidebar .sidebar-content, .css-1d391kg { 
        font-size: 30px !important;
    }

    /* Button text size */
    .stButton button {
        font-size: 18px !important; /* Ensure buttons have larger text */
    }


    </style>
    """,
    unsafe_allow_html=True,
)


# Consolidated CSS
st.markdown(
    """
    <style>
    /* Main container and background */
    [data-testid="stAppViewContainer"] {
        min-height: 100vh;
        background-color: #b3d9ff;
        background-size: cover;
        background-attachment: fixed;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #A7C7E7; /* Blue background for the sidebar */
        color: white; /* White text color */
        font-size: 30px; /* Adjust sidebar text size */
        padding: 20px; /* Add some padding */
    }

    /* Adjust elements inside the sidebar */
    [data-testid="stSidebar"] .sidebar-content {
        overflow: auto; /* Allow scrolling if content overflows */
    }

    /* Reset sidebar search bar (if mistakenly activated) */
    input[type="search"] {
        appearance: none;
        -webkit-appearance: none;
        outline: none;
    }

    /* General app content styling */
    [data-testid="stAppViewContainer"] {
        background-color: #b3d9ff; /* Light blue background */
        padding: 10px;
    }

    /* Main content styling */
    [data-testid="stAppViewContainer"] .main {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Fonts and text styles */
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] * {
        font-family: 'Comic Neue';
        
    }


   /* Floating emojis container */
    .emoji-container {
    position: fixed;
    z-index: 0;
    pointer-events: none;
    width: 100vw; /* Full viewport width */
    height: 100vh; /* Full viewport height */
    overflow: hidden; /* Ensures anything outside is clipped */
    }
    .emoji {
        position: absolute;
        font-size: 0.8rem;
        opacity: 0.8;
    }

    /* Circular motion animations */
    @keyframes circle {
        0% { transform: rotate(0deg) translateX(50px) rotate(0deg); }
        25% { transform: rotate(90deg) translateX(50px) rotate(-90deg); }
        50% { transform: rotate(180deg) translateX(50px) rotate(-180deg); }
        75% { transform: rotate(270deg) translateX(50px) rotate(-270deg); }
        100% { transform: rotate(360deg) translateX(50px) rotate(-360deg); }
    }
    @keyframes circle-large {
        0% { transform: rotate(0deg) translateX(100px) rotate(0deg); }
        25% { transform: rotate(90deg) translateX(100px) rotate(-90deg); }
        50% { transform: rotate(180deg) translateX(100px) rotate(-180deg); }
        75% { transform: rotate(270deg) translateX(100px) rotate(-270deg); }
        100% { transform: rotate(360deg) translateX(100px) rotate(-360deg); }
    }

    /* Triangular motion animations */
    @keyframes triangle {
        0% { transform: translate(0px, 0px); }
        33% { transform: translate(80px, 0px); }
        66% { transform: translate(40px, -69.28px); }
        100% { transform: translate(0px, 0px); }
    }
    @keyframes triangle-large {
        0% { transform: translate(0px, 0px); }
        33% { transform: translate(120px, 0px); }
        66% { transform: translate(60px, -103.92px); }
        100% { transform: translate(0px, 0px); }
    }

    /* Square motion animations */
    @keyframes square {
        0% { transform: translate(0px, 0px); }
        25% { transform: translate(80px, 0px); }
        50% { transform: translate(80px, 80px); }
        75% { transform: translate(0px, 80px); }
        100% { transform: translate(0px, 0px); }
    }
    @keyframes square-large {
        0% { transform: translate(0px, 0px); }
        25% { transform: translate(120px, 0px); }
        50% { transform: translate(120px, 120px); }
        75% { transform: translate(0px, 120px); }
        100% { transform: translate(0px, 0px); }
    }

    /* Assign animations to emojis */
    .emoji:nth-child(1) { animation: circle 6s infinite linear; }
    .emoji:nth-child(2) { animation: circle-large 8s infinite linear; }
    .emoji:nth-child(3) { animation: triangle 7s infinite ease-in-out; }
    .emoji:nth-child(4) { animation: triangle-large 9s infinite ease-in-out; }
    .emoji:nth-child(5) { animation: square 6s infinite ease-in-out; }
    .emoji:nth-child(6) { animation: square-large 10s infinite ease-in-out; }
    .emoji:nth-child(7) { animation: circle 8s infinite linear; }
    .emoji:nth-child(8) { animation: triangle 10s infinite ease-in-out; }
    .emoji:nth-child(9) { animation: square-large 11s infinite ease-in-out; }
    .emoji:nth-child(10) { animation: circle-large 9s infinite linear; }
    .emoji:nth-child(11) { animation: square 7s infinite ease-in-out; }
    .emoji:nth-child(12) { animation: triangle-large 12s infinite ease-in-out; }
    .emoji:nth-child(13) { animation: circle 6s infinite linear; }
    .emoji:nth-child(14) { animation: triangle 9s infinite ease-in-out; }
    .emoji:nth-child(15) { animation: square-large 10s infinite ease-in-out; }
    .emoji:nth-child(16) { animation: circle-large 11s infinite linear; }
    .emoji:nth-child(17) { animation: square 8s infinite ease-in-out; }
    .emoji:nth-child(18) { animation: triangle-large 13s infinite ease-in-out; }
    </style>

    <div class="emoji-container">
        <div class="emoji" style="left: 30%; top: 70%;">🍎</div>
        <div class="emoji" style="left: 15%; top: 60%;">🍌</div>
        <div class="emoji" style="left: 20%; top: 65%;">🍇</div>
        <div class="emoji" style="left: 40%; top: 70%;">🍉</div>
        <div class="emoji" style="left: 40%; top: 60%;">🍒</div>
        <div class="emoji" style="left: 20%; top: 55%;">🍓</div>
        <div class="emoji" style="left: 35%; top: 70%;">🍑</div>
        <div class="emoji" style="left: 50%; top: 70%;">🍍</div>
        <div class="emoji" style="left: 10%; top: 70%;">🥝</div>
        <div class="emoji" style="left: 30%; top: 65%;">🥭</div>
        <div class="emoji" style="left: 40%; top: 65%;">🍏</div>
        <div class="emoji" style="left: 30%; top: 65%;">🍐</div>
        <div class="emoji" style="left: 40%; top: 80%;">🍋</div>
        <div class="emoji" style="left: 25%; top: 65%;">🍊</div>
        <div class="emoji" style="left: 20%; top: 65%;">🍋</div>
        <div class="emoji" style="left: 30%; top: 75%;">🥭</div>
        <div class="emoji" style="left:5 25%; top: 65%;">🍏</div>
        <div class="emoji" style="left: 35%; top: 75%;">🍐</div>
    </div>
    
    """,
    unsafe_allow_html=True
)

#Title
st.markdown(
    """
    <style>
    .centered-title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 10vh; /* Full screen height */
        width: 100%; /* Full screen width */
        position: relative;
    }

    .title-box {
        text-align: center;
        font-size: 1.5rem; /* Increased font size */
        font-weight: bold;
        color: #4CAF50;
        background: rgba(76, 175, 80, 0.1); /* Light green background */
        padding: 30px 50px; /* Padding for the rectangle */
        border-radius: 15px; /* Rounded corners */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }
    </style>

    <div class="centered-title-container">
        <div class="title-box">
            Welcome to Fruity Food Tracker!
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
page = st.sidebar.selectbox("", ["Home", "Register Food", "Tracked Items"])

# Initialize session state for food data
if "food_data" not in st.session_state:
    st.session_state.food_data = pd.DataFrame(columns=["Timestamp", "Food Item", "Group"])

# Home Page
if page == "Home":
    st.markdown(
    """
    <style>
    .centered-message-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 45vh; /* Full screen height */
        width: 100%; /* Full screen width */
        position: relative;
    }

    .message-box {
        text-align: center;
        font-size: 1rem;
        font-weight: 400;
        line-height: 2;
        color: #097969;
        background: rgba(9, 121, 105, 0.1); /* Light green background */
        padding: 20px;
        border-radius: 15px; /* Rounded corners */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }
    </style>

    <div class="centered-message-container">
        <div class="message-box">
            Track your food, track your health effortlessly.<br>
            Fruity makes it easier than ever to monitor your eating habits. <br>
            Simply snap a photo of your meal, and let our AI-powered tool do the rest! <br>
            From calorie counts to detailed nutritional breakdowns, we provide you with the insights you need to make informed choices and stay on track with your health goals. <br>
            Join us in making healthy eating fun, interactive, and simple. Your path to better nutrition starts here!<br>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Register Food Page
if page == "Register Food":
    st.header("Register Food Item")
    food_image = st.camera_input("")
    uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if food_image or uploaded_image:
        image = Image.open(food_image or uploaded_image)
        image = image.resize((640,640))
        st.image(image)
        #st.session_state["uploaded_image"] = image
        data = main.run_model(image)
        for tup in data:
            st.info(f"Name: {tup[0]}, Food Group: {tup[1]}")


    if st.button("Register Food"):
        try:   
            if data == []:
                raise NameError
            cal = cl.Calculations()
            cal.load_results('results.json')
            cal.classify(data)
            cal.save_results('results.json')
            st.info('ADDED')
        except NameError:
            st.warning("Can't recognize the food!")
    

    

# Tracked Items Page
if page == "Tracked Items":
    st.header("Tracked Food Items")
    if st.button("Plot"):
        try:
            cal = cl.Calculations()
            cal.load_results('results.json')
            labels = 'Fruit and Vegetable','Protein','Grain'
            sizes = cal.classify('results.json')

            fig1, ax1 = plt.subplots()
            wedge, text, autotext = ax1.pie(sizes, autopct='%1.1f%%')
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.legend(wedge, labels, title="Type of food",loc="lower right")            
            cal.save_results('results.json')
            st.pyplot(fig1)
        except:
            st.warning("UH OH! Something went wrong! Try to add some items first.")
    # else:
    #     st.info("No food items registered yet.")
    
    if st.button('Reset'):
        reset = cl.Calculations()
        reset.resetJson('results.json')