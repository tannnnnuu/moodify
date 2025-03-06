from transformers import pipeline

# Load the pre-trained sentiment analysis model
sentiment_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def get_emotion(text):
    """
    This function takes user input text and returns the detected emotion label.
    """
    result = sentiment_pipeline(text)  # Run sentiment analysis
    return result[0]['label'].lower()  # Convert emotion to lowercase

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    emotion = get_emotion(text)
    print(f"Detected Emotion: {emotion}")
