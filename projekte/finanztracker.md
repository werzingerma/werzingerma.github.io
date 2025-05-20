---
layout: page
title: Persönlicher Finanztracker
permalink: /projekte/finanztracker/
---

# Persönlicher Finanztracker

![Finanztracker Screenshot](/assets/images/finanztracker-dashboard.png)

## Projektbeschreibung

Der Persönliche Finanztracker ist eine Webanwendung, die es Benutzern ermöglicht, ihre Einnahmen und Ausgaben zu verfolgen, Kategorien zuzuweisen und Trends über Zeit zu visualisieren.

## Funktionen

- Erfassung von Einnahmen und Ausgaben mit Datum, Betrag und Kategorie
- Dashboard mit Monats- und Jahresübersicht
- Visualisierung von Ausgabentrends nach Kategorien
- Export der Daten als CSV oder PDF
- Responsive Design für Desktop und Mobile

## Technischer Stack

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python Flask
- **Datenbank**: SQLite (Entwicklung), PostgreSQL (Produktion)
- **Deployment**: Heroku

## Implementierungsdetails

### Datenbankschema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);