from fetch_articles import fetch_articles

def run():
    keyword = "intelligence artificielle"
    articles = fetch_articles(keyword)

    print(f"\n📰 Articles trouvés pour : {keyword}\n")
    for article in articles:
        print(f"- {article['title']}\n  {article['link']}\n")

if __name__ == "__main__":
    run()