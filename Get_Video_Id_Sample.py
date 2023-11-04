from googleapiclient.discovery import build
import os

# Your YouTube Data API Key
youtube_api_key = 'AIzaSyB2cyMTQYcDtNQkHLLQU6a2106ke0cUJoA'

# The channel ID you're interested in
channel_id = 'UCgNBLFrs5_0jIqnHHQKbIAQ'

# Build the YouTube client
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

# Function to get all video IDs from a channel
def get_all_video_ids(youtube, channel_id):
    # List to store all video IDs
    video_ids = []

    # Make an initial call to get the first page
    request = youtube.search().list(part='id', channelId=channel_id, maxResults=50, type='video', order='date')
    response = request.execute()

    # Fetch all pages and add video IDs to the list
    while request is not None:
        response = request.execute()
        video_ids += [item['id']['videoId'] for item in response.get('items', []) if 'videoId' in item['id']]

        # Prepare the next page request
        request = youtube.search().list_next(request, response)

    return video_ids

# Get the list of all video IDs
all_video_ids = get_all_video_ids(youtube, channel_id)

# You can now print or save these IDs to a file
print(all_video_ids)
