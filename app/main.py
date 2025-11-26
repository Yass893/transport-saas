from fastapi import FastAPI
import pandas as pd
from pathlib import Path
from geopy.distance import geodesic
import requests

app = FastAPI()

CSV_PATH = Path(__file__).parent.parent / "data" / "trajets.csv"
COUT_TONNE_KM = 0.45  # coût estimé par tonne.km
API_KEY = "5b6d17f6321848f78d30d66ade65a6a4"

# Fonction de géocodage avec Geoapify
def get_coords(ville: str):
    url = f"https://api.geoapify.com/v1/geocode/search?text={ville},France&format=json&apiKey={API_KEY}"
    response = requests.get(url).json()
    if response.get("results"):
        lat = response["results"][0]["lat"]
        lon = response["results"][0]["lon"]
        return (lat, lon)
    return (None, None)

@app.get("/trajets")
def get_trajets():
    df = pd.read_csv(CSV_PATH)

    # Forcer les colonnes à être numériques (sécurité)
    df["Montant HT"] = pd.to_numeric(df["Montant HT"], errors="coerce")
    df["Poids"] = pd.to_numeric(df["Poids"], errors="coerce")

    distances, couts_par_km, marges = [], [], []

    for _, row in df.iterrows():
        coord_depart = get_coords(row["Départ"])
        coord_arrivee = get_coords(row["Arrivée"])

        if None not in coord_depart + coord_arrivee:
            distance = round(geodesic(coord_depart, coord_arrivee).km, 2)
        else:
            distance = None

        distances.append(distance)

        if distance and distance > 0:
            montant = row["Montant HT"]
            poids = row["Poids"]
            cout_km = round(montant / distance, 2)
            cout_estime = COUT_TONNE_KM * (poids / 1000) * distance
            marge = round(montant - cout_estime, 2)
        else:
            cout_km = None
            marge = None

        couts_par_km.append(cout_km)
        marges.append(marge)

    df["Distance (km)"] = distances
    df["€/km"] = couts_par_km
    df["Marge estimée (€)"] = marges

    return df.to_dict(orient="records")

@app.get("/stats")
def get_stats():
    df = pd.read_csv(CSV_PATH)

    # Sécuriser les colonnes numériques
    df["Montant HT"] = pd.to_numeric(df["Montant HT"], errors="coerce")
    df["Poids"] = pd.to_numeric(df["Poids"], errors="coerce")

    distances, couts_par_km, marges = [], [], []

    for _, row in df.iterrows():
        coord_depart = get_coords(row["Départ"])
        coord_arrivee = get_coords(row["Arrivée"])

        if None not in coord_depart + coord_arrivee:
            distance = round(geodesic(coord_depart, coord_arrivee).km, 2)
        else:
            distance = None

        distances.append(distance)

        if distance and distance > 0:
            montant = row["Montant HT"]
            poids = row["Poids"]
            cout_km = round(montant / distance, 2)
            cout_estime = COUT_TONNE_KM * (poids / 1000) * distance
            marge = round(montant - cout_estime, 2)
        else:
            cout_km = None
            marge = None

        couts_par_km.append(cout_km)
        marges.append(marge)

    df["Distance (km)"] = distances
    df["€/km"] = couts_par_km
    df["Marge estimée (€)"] = marges

    # Nettoyer les lignes avec valeurs manquantes
    df_clean = df.dropna(subset=["Distance (km)", "€/km", "Marge estimée (€)", "Montant HT"])

    return {
    "Nombre de trajets": int(len(df_clean)),
    "Distance totale (km)": float(round(df_clean["Distance (km)"].sum(), 2)),
    "Chiffre d'affaires (€)": float(round(df_clean["Montant HT"].sum(), 2)),
    "Marge totale (€)": float(round(df_clean["Marge estimée (€)"].sum(), 2)),
    "Coût moyen au km (€)": float(round(df_clean["€/km"].mean(), 2))
}
