from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SentimentRequestSerializer, SentimentResponseSerializer
import praw
import pandas as pd
import yfinance as yf
from newspaper import Article
import tqdm
from transformers import pipeline
from .text_clean import clean_text
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

client = os.getenv("REDDIT_CLIENT_ID")
secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")

reddit = praw.Reddit(
    client_id=client,
    client_secret=secret,
    user_agent=user_agent
)


# Sentiment pipeline
pipe = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")


# Helper functions
def fetch_stock_posts(subreddit_names, stock_ticker, limit=10):
    posts = []
    collected_ids = set()
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=limit * 2):
            if (stock_ticker.upper() in submission.title.upper() or
                    stock_ticker.upper() in submission.selftext.upper() or
                    f'${stock_ticker.upper()}' in submission.title.upper() or
                    f'${stock_ticker.upper()}' in submission.selftext.upper()):
                if submission.id not in collected_ids:
                    posts.append({
                        'title': submission.title,
                        'selftext': submission.selftext
                    })
                    collected_ids.add(submission.id)
                if len(posts) >= limit:
                    return posts
        for submission in subreddit.search(f'${stock_ticker} OR {stock_ticker}', limit=limit * 2):
            if submission.id not in collected_ids:
                posts.append({
                    'title': submission.title,
                    'selftext': submission.selftext
                })
                collected_ids.add(submission.id)
            if len(posts) >= limit:
                return posts
    return posts[:limit]


def get_news(ticker):
    articles = []
    search_result = yf.Search(ticker, max_results=10, news_count=10, include_research=True)
    news_data = search_result.news
    for article_info in tqdm.tqdm(news_data):
        try:
            article = Article(article_info['link'])
            article.download()
            article.parse()
            articles.append(article.text[:300])
        except:
            continue
    return articles


def analyze_sentiments(texts):
    texts = [clean_text(t[:300]) for t in texts]
    results = [pipe(t)[0] for t in texts]
    df = pd.DataFrame({
        "text": texts,
        "sentiment": [r['label'] for r in results],
        "score": [r['score'] for r in results]
    })
    return df


def get_percentages(df):
    sentiments = df['sentiment'].value_counts(normalize=True) * 100
    return {
        "positive": round(sentiments.get("positive", 0.0), 2),
        "negative": round(sentiments.get("negative", 0.0), 2),
        "neutral": round(sentiments.get("neutral", 0.0), 2)
    }


class SentimentView(APIView):
    def post(self, request, format=None):
        serializer = SentimentRequestSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer.validated_data['ticker']

            # Fetch and analyze sentiment data
            subreddits = ["stocks", "investing", "IndianStockMarket"]
            reddit_posts = fetch_stock_posts(subreddits, ticker, limit=30)
            reddit_texts = [f"Title: {p['title']} Body: {clean_text(p['selftext'])}" for p in reddit_posts]

            news_articles = get_news(ticker)

            df_reddit = analyze_sentiments(reddit_texts)
            df_news = analyze_sentiments(news_articles)

            reddit_result = get_percentages(df_reddit)
            news_result = get_percentages(df_news)

            response_data = {
                'reddit': reddit_result,
                'news': news_result
            }

            response_serializer = SentimentResponseSerializer(data=response_data)
            if response_serializer.is_valid():
                return Response(response_serializer.data)
            return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    def get(self, request, format=None):
        return Response({"message": "CORS test successful"})