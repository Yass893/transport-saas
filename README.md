# 🚚 Transport SaaS — Analyse automatisée des trajets de transport

Ce projet est un **MVP (Minimum Viable Product)** d'une solution SaaS conçue pour les **acteurs du transport routier** souhaitant mieux comprendre la **rentabilité de leurs trajets**.

🎯 **Objectif du MVP :**
> Offrir une API simple et automatisée permettant aux transporteurs de :
> - Calculer les distances entre villes
> - Estimer les coûts logistiques en €/km
> - Identifier la **marge dégagée sur chaque trajet**
> - Accéder à une synthèse claire du chiffre d'affaires et de la rentabilité

💡 Ce MVP répond à un **besoin concret métier** : aider les exploitants à piloter leur activité à partir des données terrain.  
Il peut être connecté à un outil de BI (ex: Power BI) ou enrichi pour devenir une application complète.

---

## 🔍 Fonctionnalités

### 📦 Endpoint `/trajets`

Retourne l’ensemble des trajets avec :
- Distance calculée entre départ et arrivée (à vol d’oiseau)
- Coût par kilomètre
- Marge estimée selon un coût logistique moyen (0,45€/tonne/km)

👉 Exemple de sortie :

```json
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
  },
  ...
]
