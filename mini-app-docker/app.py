
from flask import Flask, jsonify

app = Flask(__name__)

voitures = [
    {"id": 1, "marque": "Toyota", "modele": "Yaris"},
    {"id": 2, "marque": "Renault", "modele": "Clio"},
    {"id": 3, "marque": "Peugeot", "modele": "208"}
]

@app.route("/")
def accueil():
    return jsonify({"message": "Bienvenue dans notre service de location !"})

@app.route("/voitures")
def liste_voitures():
    return jsonify(voitures)

@app.route("/voitures/<int:id>")
def detail_voiture(id):
    voiture = next((v for v in voitures if v["id"] == id), None)

    if voiture is None:
        return jsonify({"erreur": "Voiture introuvable"}), 404

    return jsonify(voiture)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
