moodify

Overview
The Moodifyy is a web application that recommends Spotify playlists based on the sentiment analysis of user-inputted text. This project leverages Natural Language Processing (NLP) techniques to detect emotions from text and generate a relevant playlist accordingly.

Tech Stack
•	Python: Core programming language used for building the model and backend logic.

•	FastAPI: Used to build the backend API for sentiment analysis and playlist recommendation.

•	Streamlit: Frontend framework used for creating an interactive and user-friendly UI.

•	Hugging Face Transformers: Used for implementing sentiment analysis with pre-trained NLP models.

•	Render: Deployment platform used for hosting the FastAPI backend and Streamlit frontend.

Implementation
1.	Data Processing: The user inputs text, which is preprocessed for sentiment analysis.
	
2.	Sentiment Analysis: The model classifies the input into emotions such as happy, sad, excited, etc.
	
3.	Playlist Recommendation: Based on the detected emotion, a curated Spotify playlist is suggested to the user.
	
4.	Frontend and Deployment: The project is presented using Streamlit and deployed via Render for accessibility.
