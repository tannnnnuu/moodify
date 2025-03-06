from sentiment import get_emotion
import random

# Emotion-to-genre mapping
emotion_to_genre = {
    "joy": ["pop", "dance", "electronic", "funk"],
    "happiness": ["pop", "k-pop", "latin", "disco"],
    "sadness": ["blues", "acoustic", "soft rock", "lo-fi"],
    "anger": ["rock", "metal", "punk", "hardcore"],
    "fear": ["classical", "ambient", "dark wave"],
    "surprise": ["indie", "jazz", "experimental", "fusion"],
    "neutral": ["lo-fi", "chillhop", "jazz", "instrumental"],
    "love": ["r&b", "soul", "romantic ballads", "indie pop"],
    "excitement": ["edm", "house", "hip-hop", "trance"],
    "nostalgia": ["retro", "synthwave", "oldies", "classic rock"],
    "disappointment": ["emo", "gothic rock", "alternative"],
    "hope": ["gospel", "uplifting trance", "orchestral"],
    "calmness": ["piano", "acoustic", "meditation", "ambient"],
    "loneliness": ["indie folk", "melancholic rock", "soft jazz"],
    "confidence": ["rap", "trap", "afrobeat", "power metal"],
    "relaxation": ["chillhop", "lo-fi", "smooth jazz", "new age"]
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

from sentiment import get_emotion
import random


