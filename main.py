from fetch_articles import fetch_articles
from summarize import summarize_article, is_relevant_article
from generate_report import generate_html_report

def run():
    keyword = "intelligence artificielle"
    articles = fetch_articles(keyword)
    final_articles = []

    print(f"\n📌 Veille sur : {keyword}\n")

    for article in articles:
        title = article['title']
        link = article['link']
        raw_summary = article['summary']

        if not is_relevant_article(title, raw_summary):
            print(f"⏭ Article ignoré : {title}")
            continue

        print(f"✅ Article retenu : {title}")
        summary = summarize_article(raw_summary)

        final_articles.append({
            "title": title,
            "url": link,
            "summary": summary
        })

    if not final_articles:
        print("❗ Aucun article pertinent trouvé.")
        return

    html_report = generate_html_report(final_articles, keyword)
    
    with open("rapport_veille.html", "w", encoding="utf-8") as f:
        f.write(html_report)

    print("✅ Rapport généré : rapport_veille.html")

if __name__ == "__main__":
    run()