from fastapi import FastAPI
from sentiment import get_emotion
from fetch_playlist import get_playlist  # Fixed import
import uvicorn  # Import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Emotion-Based Playlist API"}

@app.get("/playlist")
def playlist(text: str):
    emotion = get_emotion(text)
    playlist_url = get_playlist(emotion)
    return {"emotion": emotion, "playlist": playlist_url}

# ✅ Add this to specify port
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)


