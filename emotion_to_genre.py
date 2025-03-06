from sentiment import get_emotion
import random

# Improved emotion-to-genre mapping
emotion_to_genre = {
    "joy": ["pop", "dance", "electronic"],
    "sadness": ["blues", "acoustic", "soft rock"],
    "anger": ["rock", "metal", "punk"],
    "fear": ["classical", "ambient", "lo-fi"],
    "surprise": ["indie", "jazz", "experimental"],
    "neutral": ["lo-fi", "chillhop", "jazz"]
}

def get_music_genre(text):
    """
    Detects emotion and returns a list of matching music genres.
    """
    emotion = get_emotion(text)  # Detect emotion
    genres = emotion_to_genre.get(emotion.lower(), ["chill"])  # Get genres for detected emotion
    return random.sample(genres, min(len(genres), 2))  # Return up to 2 random genres

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    genres = get_music_genre(text)
    print(f"Recommended Music Genres: {genres}")
