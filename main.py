"""
Command-line interface for the music downloader.
"""

import os
import sys
import re
from music_downloader.downloader import download_audio


def is_valid_youtube_url(url):
    youtube_pattern = re.compile(
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return bool(youtube_pattern.match(url))


def main():
    # Create a directory to store the downloaded music if it doesn't exist
    if not os.path.exists('downloaded_music'):
        os.makedirs('downloaded_music')

    # Get the video URL from the user
    video_url = input("Enter the YouTube video URL: ")

    # Check if the input URL is a valid YouTube URL
    if not is_valid_youtube_url(video_url):
        print("Invalid YouTube URL. Please enter a valid URL.")
        sys.exit(1)

    # Download the audio from the given URL
    try:
        download_audio(video_url)
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
