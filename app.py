import streamlit as st
from spotify_auth import sp  # Authenticated Spotify instance
from sentiment import get_emotion  # Import sentiment function
from fetch_playlist import get_playlist  # Import playlist function

# 🎵 App Title
st.title("🎶 Emotion-Based Playlist Generator")

# 📝 User Input
user_input = st.text_area("💬 How are you feeling today?")

# 🎯 Generate Playlist Button
if st.button("🎵 Generate Playlist"):
    if user_input.strip():
        # Detect Emotion
        emotion = get_emotion(user_input)

        # Fetch Playlist
        playlist_url = get_playlist(emotion)

        # 🎧 Display Playlist
        if "spotify.com" in playlist_url:
            st.markdown(f"### 🎼 Your Playlist: [Click here]({playlist_url})", unsafe_allow_html=True)
        else:
            st.error("🚫 No playlist found. Try again with a different input.")

    else:
        st.warning("⚠️ Please enter some text to analyze your emotion.")
