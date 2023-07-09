####Youtube Comment Analyzer####

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from googleapiclient.discovery import build


# Set up the YouTube Data API credentials (API key)
api_key = 'AIzaSyCdyHxyIjdjNZ3RuYg1yxM0uzHD0AzlUp0'

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Retrieve comments from a video
video_id = '3bT4KSBZsa8'
comments = ['Test Youtube Analyzer']

# Paginate through the comments
next_page_token = None
while True:
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,  # Adjust as per your requirement
        pageToken=next_page_token
    ).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    next_page_token = response.get('nextPageToken')

    if not next_page_token:
        break
        
# Perform sentiment analysis on the comments
sia = SentimentIntensityAnalyzer()

positive_count = 0
negative_count = 0

comment_sentiments = []
for comment in comments:
    sentiment = sia.polarity_scores(comment)
    if sentiment['compound'] >= 0.05:
        comment_sentiments.append('Positive')
        positive_count += 1
    elif sentiment['compound'] <= -0.05:
        comment_sentiments.append('Negative')
        negative_count += 1
    else:
        comment_sentiments.append('Neutral')

# Create a DataFrame with comments and their sentiment
df = pd.DataFrame({'Comment': comments, 'Sentiment': comment_sentiments})

# Display the count of positive and negative comments
print("Positive Comments:", positive_count)
print("Negative Comments:", negative_count)

# Display the DataFrame
print(df)
        

# Process the comments as per your analysis requirements
for comment in comments:
    # Perform analysis or any other actions on each comment
    print(comment)