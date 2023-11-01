# Read Me for YouTube Comment Analyzer

## Table of Contents

1. [Introduction](#Introduction)
2. [Project Structure](#Project-Structure)
3. [Dependencies](#Dependencies)
4. [Installation Guide](#Installation-Guide)
5. [Usage](#Usage)
6. [Data Collection and Preprocessing](#Data-Collection-and-Preprocessing)
7. [Algorithms and Methods](#Algorithms-and-Methods)
8. [Output and Metrics](#Output-and-Metrics)
9. [Contributing](#Contributing)

## Introduction
This project is aimed at analyzing the sentiment of YouTube comments using the Natural Language Toolkit (NLTK) in Python. The script fetches comments from a specific YouTube video, analyzes their sentiment, and displays the count of positive and negative comments.

## Project Structure
The code structure is organized into the following segments:
1. Importing Dependencies
2. YouTube API Setup
3. Data Collection
4. Sentiment Analysis
5. Data Framing and Output

## Dependencies
* Python 3.x
* NLTK
* pandas
* googleapiclient

## Installation Guide
1. Clone the repository
2. Run `pip install -r requirements.txt` to install the necessary packages
3. Obtain a YouTube Data API key and place it in the `api_key` variable.

## Usage
Insert the YouTube video ID you wish to analyze in the `video_id` variable, then run the Python file from the command line or IDE.

## Data Collection and Preprocessing

### YouTube API
The YouTube comments are fetched using YouTube Data API v3. The maximum number of comments fetched per API call is set to 100, which can be adjusted as per your requirement.

### Text Preprocessing
The NLTK VADER lexicon is used for sentiment analysis which does not require any specific text preprocessing.

## Algorithms and Methods

### Sentiment Analysis
The project uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon for sentiment analysis, part of the NLTK library. VADER is particularly suited for sentiment analysis of social media text.

#### Sentiment Scoring
* Positive if compound score >= 0.05
* Negative if compound score <= -0.05
* Neutral otherwise

## Output and Metrics

### Data Summary
The comments along with their sentiment labels are framed into a pandas DataFrame.

### Metrics
* Count of Positive Comments
* Count of Negative Comments

## Contributing
Contributions to improve the code are welcome. Please fork the repository and submit a pull request for any enhancements.

### References
1. [VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text](http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf)
2. [YouTube API v3 Documentation](https://developers.google.com/youtube/v3/docs)
