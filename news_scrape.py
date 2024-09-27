# Able to scrape for news sources

from newsapi import NewsApiClient
from flask import Flask, jsonify, request
from datetime import datetime, timedelta

# Flask API for website 
app = Flask(__name__)

# API endpoint
@app.route('/api')






# API keys
API_KEY = '11c33e616e574cdf9020fb031b17e0fe'
# Init
newsapi = NewsApiClient(api_key=API_KEY)

# runs the main
def main():
    # user search field
    KEYWORD = input('Keyword: ')
    LANG = 'en'
    TODAY = datetime.now()
    TWO_DAYS_AGO = TODAY - timedelta(days=2)

    user = input('Want the top headlines or everything? (y/n): ')

    # Retrieves the news
    if (user == 'y'):
        try:
            #SOURCE = input("Source: ")

            top_headlines = newsapi.get_top_headlines(q=KEYWORD,
                                            #sources=SOURCE,
                                            language=LANG)
            if top_headlines['articles']:
                for article in top_headlines['articles']:
                    print(f"Title: {article['title']}")
                    print(f"Description: {article['description']}")
                    print(f"URL: {article['url']}\n")
            else:
                print("No headlines found.")

        except Exception as e:
            print(f'An error has occured: {e}')

    if (user == 'n'):

        try:
            all_articles = newsapi.get_everything(q=KEYWORD,
                                        from_param=TWO_DAYS_AGO,
                                        to=TODAY,
                                        language=LANG,
                                        sort_by='relevancy',
                                        page=2)
            if all_articles['articles']:
                for article in all_articles['articles']:
                    print(f"Title: {article['title']}")
                    print(f"Description: {article['description']}")
                    print(f"URL: {article['url']}\n")
            else:
                print("No articles found.")

        except Exception as e:
            print(f'An error has occured: {e}')    

if __name__ == '__main__':
    main()