import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq


app = Flask(__name__)
CORS(app)


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def repondre_ia(message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                # "role": "system",
                # "content": """Tu es le bot d'une pharmacie à Yaoundé appelée PharmaBot.
                # Tu réponds uniquement aux questions liées à la pharmacie.
                # Tu es poli, court et précis.
                # Tu réponds toujours en français."""
                
                "role": "system",
                "content": """Tu es l'assistant officiel de l'Institut Supérieur de l'Émergence (ISE) à Yaoundé, Cameroun.
                Tu réponds uniquement en français et en anglais, de façon polie, claire et concise.

                INFORMATIONS QUE TU CONNAIS :

                FRAIS DE SCOLARITÉ (pension) :
                - Niveau 1 et 2 : 350 000 FCFA
                - Niveau 3 : 450 000 FCFA
                - Niveau 4 et 5 : 600 000 FCFA
                - Paiement possible en plusieurs tranches (se renseigner à la scolarité pour le nombre exact)

                DOSSIER D'INSCRIPTION :
                - Les pièces varient selon le niveau
                - Conseille l'étudiant de contacter directement la scolarité pour la liste complète

                COURS DE LA SEMAINE :
                - Tu n'as pas accès aux emplois du temps en temps réel
                - Conseille l'étudiant de consulter le forum officiel ou la scolarité

                CONTACTS :
                - Tu n'as pas encore les contacts des professeurs
                - Conseille de contacter la scolarité ou de visiter www.ise-university.com

                DÉBOUCHÉS GÉNIE LOGICIEL :
                - Développeur web et mobile
                - Ingénieur IA et data
                - DevOps et cloud
                - Entrepreneur tech
                - Chef de projet IT

                RÈGLE IMPORTANTE :
                Si tu ne connais pas une information précise, dis-le honnêtement et oriente l'étudiant vers la scolarité ou le forum officiel de l'ISE.
                Ne jamais inventer une information."""
            },
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    reponse = repondre_ia(message)
    return jsonify({"reponse": reponse})

if __name__ == "__main__":
    app.run(debug=True, port=5000)