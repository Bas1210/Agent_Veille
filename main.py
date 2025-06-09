from fetch_articles import fetch_articles
from summarize import summarize_article

def run():
    keyword = "intelligence artificielle"
    articles = fetch_articles(keyword)

    print(f"\n📰 Articles trouvés pour : {keyword}\n")

    for article in articles:
        print(f"🔗 {article['title']}\n{article['link']}")

        summary = summarize_article(article['summary'])
        print(f"🧠 Résumé :\n{summary}\n{'-'*60}")

if __name__ == "__main__":
    run()