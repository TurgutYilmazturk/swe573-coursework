import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from praw.models import MoreComments


reddit = praw.Reddit(
     client_id="J5ECOUqkljDYvQ",
     client_secret="HWN03vk8ykTOEm3zTCTfJShlLsnHrw",
     user_agent="www.turgutcemyilmazturk.com /tubikcan",
     username="tubikcan",
     password="redditicinpass",
 )

sia = SentimentIntensityAnalyzer()
