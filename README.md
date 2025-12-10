🚚 Transport SaaS — Analyse automatisée des trajets de transport
🔎 Présentation du projet

Ce projet est un MVP (Minimum Viable Product) d'une solution SaaS destinée aux transporteurs routiers, exploitants et TPE/PME du secteur logistique.

L’objectif : fournir un outil simple et automatisé permettant d’analyser la rentabilité des trajets à partir de leurs données de transport.

Grâce à l’API, il est possible de :

calculer automatiquement les distances entre deux villes

estimer les coûts logistiques

déterminer la marge dégagée

suivre les indicateurs clés (CA, distance totale, coût/km, marge totale)

connecter les résultats à Power BI pour un dashboard professionnel

Ce MVP sert de base pour développer une plateforme SaaS complète.

🚀 Fonctionnalités principales
📦 Endpoint : /trajets

Retourne l’ensemble des trajets avec :

Distance calculée (géocodage + haversine)

Coût par kilomètre

Marge estimée

Chiffres clés du transport (CA, tonnage, prix HT…)

💡 Exemple de réponse JSON
[
  {
    "Exp.Date": "2025-11-01",
    "Voyage N°": "TR001",
    "Départ": "Limoges",
    "Arrivée": "Bordeaux",
    "Poids": 1200,
    "Montant HT": 850,
    "Distance (km)": 210.45,
    "€/km": 4.04,
    "Marge estimée (€)": 726.72
  }
]

🧠 Logique métier

Voici les règles métier intégrées dans le calcul :

Distance (km) = formule haversine

Coût logistique (€) = poids (tonnes) × distance × 0.45 €/km/tonne

Prix au km (€ / km) = montant HT / distance

Marge = montant HT – coût logistique estimé

Géocodage des villes avec geopy

Pipeline Python automatisé pour enrichir les colonnes manquantes

🧰 Technologies utilisées
Backend

FastAPI

Pydantic

Python (pandas, geopy, haversine)

Data Engineering

Nettoyage et enrichissement du DataFrame

Calculs automatisés

Préparation pour dashboard Power BI

Infrastructure

API REST

Architecture prête pour futur déploiement (Docker / Azure / AWS)


📊 Intégration Power BI

L’API peut s'intégrer directement dans Power BI grâce à une requête Web.
Cela permet de produire un dashboard contenant :

Distance totale parcourue

Coût total des trajets

Marge globale

Top destinations

Carte interactive des trajets

Evolution mensuelle des marges


🛣️ Roadmap (évolution future du SaaS)
Phase 2 : amélioration

✔ Géocodage plus précis (Google Maps API)

✔ Gestion des temps de trajet

✔ Coût carburant dynamique (API carburant)

Phase 3 : Dashboard & produit SaaS

Interface web (Streamlit / React)

Authentification utilisateur

Multi-entreprises

Export PDF intégré

Connexion automatique à des TMS

🛡️ Sécurité & bonnes pratiques

Aucun fichier CSV sensible n’est stocké dans le dépôt

.gitignore protège les données du transporteur

API sécurisable via token ou OAuth2

👤 Auteur

Développé par Yass893
Passionné par l’automatisation & les solutions SaaS transport.
