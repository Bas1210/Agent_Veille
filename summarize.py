from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_article(text: str) -> str:
    prompt = (
        "Tu es un expert en synthèse d'informations. Résume cet article "
        "de façon claire et détaillée en 8 à 10 lignes, pour un lecteur professionnel "
        "souhaitant comprendre les nouveautés autour de l'intelligence artificielle :\n\n"
        f"{text[:3000]}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Erreur lors du résumé : {e}")
        return "Résumé non disponible."
    
def is_relevant_article(title: str, raw_summary: str) -> bool:
    prompt = f"""Voici un article à évaluer :

Titre : {title}
Résumé : {raw_summary}

Est-ce que cet article est pertinent pour une veille professionnelle sur l'intelligence artificielle ?
Réponds simplement par "oui" ou "non"."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip().lower()
        return "oui" in answer
    except Exception as e:
        print(f"⚠️ Erreur vérification pertinence : {e}")
        return True  # Par défaut, on garde l'article si doute