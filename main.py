from fetch_articles import fetch_articles
from summarize import summarize_article, is_relevant_article

def run():
    keyword = "intelligence artificielle"
    articles = fetch_articles(keyword)

    print(f"\n📰 Articles pertinents pour : {keyword}\n")

    for article in articles:
        title = article['title']
        link = article['link']
        raw_summary = article['summary']

        if not is_relevant_article(title, raw_summary):
            print(f"⏭ Article ignoré (non pertinent) : {title}\n")
            continue

        print(f"🔗 {title}\n{link}")
        summary = summarize_article(raw_summary)
        print(f"🧠 Résumé :\n{summary}\n{'-'*60}")

if __name__ == "__main__":
    run()