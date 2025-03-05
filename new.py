import feedparser
from flask import Flask

app = Flask(__name__)

# Updated News RSS Feeds
rss_feeds = {
    'philnews': 'https://philnews.ph/feed/',
    'interaksyon': 'https://interaksyon.philstar.com/feed/',
    'abante_tonite': 'https://tonite.abante.com.ph/feed/'
}

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>Philippine News </h1>
        <ul>
            <li><a href="/philnews">PhilNews</a></li>
            <li><a href="/interaksyon">Interaksyon</a></li>
            <li><a href="/abante_tonite">Abante Tonite</a></li>
        </ul>
    </body>
    </html>
    """

@app.route("/philnews")
def philnews_news():
    return get_news('philnews')

@app.route("/interaksyon")
def interaksyon_news():
    return get_news('interaksyon')

@app.route("/abante_tonite")
def abante_tonite_news():
    return get_news('abante_tonite')

def get_news(publication):
    feed = feedparser.parse(rss_feeds[publication])
    if not feed.entries:
        return f"<html><body><h1>No news available for {publication.replace('_', ' ').title()}</h1><a href='/'>Back to Home</a></body></html>"
    
    articles = ""
    for entry in feed.entries[:5]:  # Display the top 5 news articles
        articles += f"""
        <h2><a href=\"{entry.link}\">{entry.title}</a></h2>
        <p><i>{entry.get('published', 'No publication date')}</i></p>
        <p>{entry.get('summary', 'No summary available')}</p>
        <hr>
        """
    
    return f"""
    <html>
    <body>
        <h1>{publication.replace('_', ' ').title()} Headlines</h1>
        {articles}
        <a href="/">Back to Home</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000, debug=True)
