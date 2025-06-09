import feedparser
from urllib.parse import quote

def fetch_articles(keyword: str, max_results: int = 5):
    """
    Récupère les derniers articles Google News en lien avec un mot-clé.

    Args:
        keyword (str): Le mot-clé à rechercher.
        max_results (int): Nombre d'articles à retourner.

    Returns:
        list: Liste de dictionnaires contenant titre, lien, résumé brut.
    """
    query = quote(keyword)
    url = f"https://news.google.com/rss/search?q={query}&hl=fr&gl=FR&ceid=FR:fr"
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:max_results]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary
        })
    return articles