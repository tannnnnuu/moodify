from spotify_auth import sp  # Import authenticated Spotipy instance

try:
    # Get the authenticated user's profile
    user_info = sp.current_user()
    print(f"Logged in as: {user_info['display_name']}")
except Exception as e:
    print(f"Spotify authentication failed: {e}")
