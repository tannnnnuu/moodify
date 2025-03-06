import os
import uvicorn
from fastapi import FastAPI
from sentiment import get_emotion
from fetch_playlist import get_playlist

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Emotion-Based Playlist API"}

@app.get("/playlist")
def playlist(text: str):
    emotion = get_emotion(text)
    playlist_url = get_playlist(emotion)
    return {"emotion": emotion, "playlist": playlist_url}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
