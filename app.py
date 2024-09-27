# Able to scrape for news sources

from newsapi import NewsApiClient
from flask import Flask, jsonify, request, render_template, url_for
from datetime import datetime, timedelta

# API keys
API_KEY = '11c33e616e574cdf9020fb031b17e0fe'
# Init
newsapi = NewsApiClient(api_key=API_KEY)

# Flask API for website 
app = Flask(__name__)

# API endpoint
@app.route('/')
def index():
    return render_template('index.html')

# search, user inputs info
@app.route('/search', methods=['POST'])
def search():
    # user search field
    KEYWORD = request.form.get('keyword')
    SOURCE = request.form.get('source').lower()
    clear = request.form.get('clear')
    # default variables
    LANG = 'en'
    TODAY = datetime.now()
    TWO_DAYS_AGO = TODAY - timedelta(days=2)

    SOURCE_MAPPINGS = {
        'fox news': 'fox-news',
        'cnn': 'cnn',
        'bbc news': 'bbc-news',
        'abc news': 'abc-news',
        'fox business' : 'fox-business',
        'the new york times': 'the-new-york-times',
        'al jazeera': 'al-jazeera-english',
    }
    
    if not KEYWORD:
        return render_template('index.html', error='Please provide a keyword.')

    if clear:
            return render_template('index.html', headlines=None)

    if SOURCE:
        SOURCE = SOURCE_MAPPINGS.get(SOURCE, None)
        if not SOURCE:
            return render_template('index.html', error="Unsupported News Source!")
    # Retrieves the news
    try:
        if SOURCE:
            articles = newsapi.get_top_headlines(q=KEYWORD,sources=SOURCE, language=LANG)
        else:
            articles = newsapi.get_everything(q=KEYWORD,
                                    from_param=TWO_DAYS_AGO,
                                    to=TODAY,
                                    language=LANG)
        # get the articles from api response
        headlines = articles.get('articles', 'url')

        if headlines:
            return render_template('index.html', headlines=headlines)
        else:
            return render_template('index.html', error="No articles found.")


    except Exception as e:
        return render_template('index.html', error=f"an error occured: {e}")

if __name__ == '__main__':
    app.run(debug=True)