from datetime import datetime

def generate_html_report(articles: list, keyword: str) -> str:
    """
    Génère une page HTML contenant le rapport de veille (style startup moderne).

    Args:
        articles (list): liste d'articles pertinents (title, url, summary)
        keyword (str): mot-clé de la veille

    Returns:
        str: HTML complet
    """
    date = datetime.now().strftime("%d/%m/%Y")

    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Rapport de veille - {keyword}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Roboto, sans-serif;
                background-color: #f4f7fa;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 700px;
                margin: auto;
                background-color: #ffffff;
                padding: 40px;
                box-shadow: 0 0 20px rgba(0,0,0,0.05);
                border-radius: 10px;
                margin-top: 40px;
                margin-bottom: 40px;
            }}
            h1 {{
                color: #0d6efd;
                font-size: 28px;
            }}
            .date {{
                font-size: 14px;
                color: #888;
            }}
            .intro {{
                margin: 20px 0;
                font-size: 16px;
                line-height: 1.6;
            }}
            .article {{
                border-left: 4px solid #0d6efd;
                padding-left: 15px;
                margin: 30px 0;
            }}
            .article h2 {{
                font-size: 20px;
                margin-bottom: 5px;
                color: #222;
            }}
            .article p {{
                font-size: 15px;
                line-height: 1.6;
            }}
            .btn {{
                display: inline-block;
                margin-top: 10px;
                background-color: #0d6efd;
                color: white;
                padding: 8px 14px;
                text-decoration: none;
                border-radius: 6px;
                font-size: 14px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #aaa;
                margin-top: 40px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 Rapport de veille – {keyword.title()}</h1>
            <p class="date">Date : {date}</p>
            <p class="intro">Voici votre sélection d'articles récents autour de <strong>{keyword}</strong>, sélectionnés et résumés automatiquement pour vous permettre de rester informé(e) efficacement.</p>
    """

    for article in articles:
        html += f"""
            <div class="article">
                <h2>{article['title']}</h2>
                <p>{article['summary']}</p>
                <a class="btn" href="{article['url']}" target="_blank">Lire l'article</a>
            </div>
        """

    html += """
            <div class="footer">
                Rapport généré automatiquement par votre assistant de veille IA.<br>
                Vous recevez ce rapport car vous êtes inscrit à une veille thématique.
            </div>
        </div>
    </body>
    </html>
    """

    return html