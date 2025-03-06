from fastapi import FastAPI
from sentiment import get_emotion
from fetch_playlist import get_playlist  # Fixed import

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Emotion-Based Playlist API"}

@app.get("/playlist")
def playlist(text: str):
    emotion = get_emotion(text)
    playlist_url = get_playlist(emotion)
    return {"emotion": emotion, "playlist": playlist_url}
