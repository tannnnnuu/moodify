import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_auth import sp  
from emotion_to_genre import get_music_genre 

def get_playlist(emotion):
    """
    Fetches a Spotify playlist based on detected emotion.
    """
    # Get genres from emotion
    genres = get_music_genre(emotion)
    
    try:
        # Search for a playlist with the first matching genre
        for genre in genres:
            results = sp.search(q=genre, type="playlist", limit=1)

            print(f"Spotify API Response: {results}")

            # Check if results exist and extract playlist URL
            if results.get('playlists') and results['playlists'].get('items'):
                return results['playlists']['items'][0]['external_urls']['spotify']

        return "No playlist found for this emotion."
    
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return "Error fetching playlist. Please try again."

# Test the function
if __name__ == "__main__":
    emotion = input("Enter an emotion: ")
    playlist_link = get_playlist(emotion)
    print(f"Recommended Playlist: {playlist_link}")
