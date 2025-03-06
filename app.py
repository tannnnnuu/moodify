import streamlit as st
import time
import requests
from fetch_playlist import get_playlist  # Playlist function

# 🎨 Custom Styling 
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #222f3e, #341f97);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .title-text {
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            color: #f368e0;
            margin-bottom: 5px;
            transition: color 0.3s ease-in-out;
        }
        .title-text:hover {
            color: #ff9f43;
        }
        .music-emoji {
            color: #ff9f43;
        }
        .subtitle-text {
            text-align: center;
            font-size: 18px;
            color: #d2dae2;
            margin-bottom: 20px;
        }
        .spotify-button a {
            background: linear-gradient(45deg, #ff9f43, #ee5253);
            color: white;
            padding: 12px 28px;
            border-radius: 25px;
            font-size: 18px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s ease-in-out;
            box-shadow: 0 3px 12px rgba(238, 82, 83, 0.4);
            border: none;
        }
        .spotify-button a:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #ee5253, #ff9f43);
            box-shadow: 0 5px 18px rgba(238, 82, 83, 0.6);
        }
        .emotion-box {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            margin-top: 15px;
            padding: 10px 15px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            display: inline-block;
            text-transform: uppercase;
            color: #ff9f43;
        }
        .soft-gradient {
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #ff9f43, #f368e0);
            margin-bottom: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# 🎵 Title & Description
st.markdown("""
    <h1 class='title-text'><span class='music-emoji'>🎶</span> Emotion-Based Playlist Generator</h1>
    <p class='subtitle-text'>Describe your mood, and we'll create a playlist just for you! 🌟</p>
    <div class='soft-gradient'></div>
    """, unsafe_allow_html=True)

# 📝 User Input Section 
st.markdown("<b>💬 How do you feel right now?</b>", unsafe_allow_html=True)
user_input = st.text_area("", placeholder="Express your emotions here...", height=110)

# 🌐 Backend API URL
API_URL = "https://moodify-lrak.onrender.com/predict"

def get_emotion_api(text):
    """Send text to backend API and get the detected emotion."""
    response = requests.post(API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json().get("emotion", "neutral")  
    return "neutral"

# 🎯 Generate Playlist Button
if st.button("🌟 Generate Playlist", key="generate_button"):
    if user_input.strip():
        with st.spinner("🧘 Analyzing your emotions..."):
            time.sleep(1.5)  
            emotion = get_emotion_api(user_input)  # ✅ Using Backend API
        
        # 🎭 Map emotions to emojis
        emotion_emoji = {
            "joy": "😊", "sadness": "😢", "anger": "😠", 
            "love": "❤️", "fear": "😨", "surprise": "😲"
        }.get(emotion.lower(), "🎭")
        
        st.markdown(f"<div class='emotion-box'>{emotion_emoji} {emotion.capitalize()}</div>", unsafe_allow_html=True)
        
        with st.spinner("🎵 Finding your perfect playlist..."):
            time.sleep(1.5)
            playlist_url = get_playlist(emotion)  # ✅ Get playlist based on emotion

        # 🎧 Display Playlist
        if "spotify.com" in playlist_url:
            st.markdown(f"""
                <div class='spotify-button'>
                    <a href='{playlist_url}' target='_blank'>🎶 Listen Now on Spotify</a>
                </div>
                <br>
                """, unsafe_allow_html=True)
            
            # Embed Spotify Player
            embed_url = playlist_url.replace("open.spotify.com", "open.spotify.com/embed")
            st.markdown(f"""<iframe src='{embed_url}' width='100%' height='400' frameborder='0' allowtransparency='true' allow='encrypted-media' style='border-radius: 12px;'></iframe>""", unsafe_allow_html=True)
        else:
            st.error("🚫 No playlist found. Try again with different words.")
    else:
        st.warning("⚠️ Please enter some text to analyze your emotion.")

# 👣 Footer
st.markdown("""
    <div class='soft-gradient'></div>
    <p style='text-align: center; font-size:14px; color: #d2dae2;'>Created with 🎵 Music & Emotion </p>
    """, unsafe_allow_html=True)
