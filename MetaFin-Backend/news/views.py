from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newspaper import Article
import yfinance as yf
import os
import logging
import traceback
from google import genai
from dotenv import load_dotenv
from trades.views import TopTradedAssetsView

load_dotenv()
logger = logging.getLogger(__name__)


class news(APIView):
    def get(self, request):
        try:
            ticker_param = request.query_params.get('tickers', '')

            if ticker_param:
                tickers = ticker_param.split(',')
                source = 'user_specified'
            else:
                try:
                    top_assets_view = TopTradedAssetsView()
                    top_assets_response = top_assets_view.get(request)
                    top_assets_data = top_assets_response.data

                    tickers = [asset['asset_name'] for asset in top_assets_data]
                    source = 'top_traded'

                    if not tickers:
                        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']
                        source = 'default'

                except Exception as e:
                    logger.error(f"Error fetching top assets: {str(e)}")
                    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA']
                    source = 'default (after error)'

            tickers = tickers[:5]

            news_data = self.get_news(tickers)

            return Response({
                "status": "success",
                "source": source,
                "tickers": tickers,
                "data": news_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error in Trade_News API: {str(e)}")
            logger.error(traceback.format_exc())
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def generate_text(self, text):
        try:
            GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
            if not GEMINI_API_KEY:
                return "API key not found. Please set the GEMINI_API_KEY environment variable."

            client = genai.Client(api_key=GEMINI_API_KEY)

            prompt = f"You are a finance expert. Please provide a summary of following news: {text} generate summary give complete text only"

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt]
            )

            return response.text

        except Exception as e:
            logger.error(f"Error generating summary: {str(e)}")
            return f"Unable to generate summary: {str(e)}"

    def get_news(self, tickers):
        articles = {}

        for ticker in tickers:
            try:
                art = {}
                search_result = yf.Search(ticker, max_results=10, news_count=10, include_research=True)
                news_data = search_result.news

                for article_info in news_data:
                    try:

                        article = Article(article_info['link'])
                        article.download()
                        article.parse()

                        if len(article.text.strip()) >= 500:
                            summary = self.generate_text(article.text[:4000])

                            art['title'] = article.title
                            art['summary'] = summary
                            articles[ticker] = art
                            break



                    except Exception as e:
                        logger.warning(f"Error processing article for {ticker}: {str(e)}")
                        continue


            except Exception as e:
                logger.error(f"Error fetching news for {ticker}: {str(e)}")
                articles[ticker] = [{"error": f"Failed to fetch news: {str(e)}"}]

        return articles