from datetime import datetime

def generate_html_report(articles: list, keyword: str) -> str:
    """
    Génère une page HTML contenant le rapport de veille.
    
    Args:
        articles (list): liste d'articles pertinents (title, url, summary)
        keyword (str): mot-clé de la veille
    
    Returns:
        str: HTML complet
    """
    date = datetime.now().strftime("%d/%m/%Y")
    
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Rapport de veille - {keyword}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f8f9fa;
                color: #333;
            }}
            h1 {{
                color: #0066cc;
            }}
            .article {{
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #ccc;
            }}
            a {{
                color: #0066cc;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <h1>🧠 Rapport de veille - {keyword.title()}</h1>
        <p><em>Date : {date}</em></p>
        <p>Ce rapport regroupe les articles récents les plus pertinents concernant <strong>{keyword}</strong>, accompagnés de résumés détaillés.</p>
        <hr>
    """

    for article in articles:
        html += f"""
        <div class="article">
            <h2>{article['title']}</h2>
            <p><a href="{article['url']}" target="_blank">Lire l'article original</a></p>
            <p>{article['summary']}</p>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return html