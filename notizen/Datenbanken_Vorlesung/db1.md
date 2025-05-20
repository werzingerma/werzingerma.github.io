---
layout: page
title: DB1 - Einführung in Datenbanksysteme
permalink: /notizen/Datenbanken_Vorlesung/db1/
---

# DB1: Einführung in Datenbanksysteme

*Vorlesungsdatum: 05.11.2024*

## Grundlegende Konzepte

### Was ist eine Datenbank?

Eine Datenbank ist eine organisierte Sammlung von Daten, die elektronisch gespeichert und abgerufen werden kann. Sie wird verwendet, um Daten effizient zu speichern, zu verwalten und abzufragen.

### Datenbanksystem vs. Datenbankmanagementsystem (DBMS)

- **Datenbank**: Die eigentlichen gespeicherten Daten
- **DBMS**: Die Software, die den Zugriff auf die Datenbank ermöglicht
- **Datenbanksystem**: Die Kombination aus Datenbank und DBMS

### Historische Entwicklung

1. **Hierarchische Datenbanken** (1960er): Baumstruktur (z.B. IBM IMS)
2. **Netzwerk-Datenbanken** (1970er): Erweiterte Verknüpfungsmöglichkeiten
3. **Relationale Datenbanken** (ab 1970): Basierend auf Edgar Codds Relationalem Modell
4. **Objektorientierte Datenbanken** (1980er-1990er): Speicherung komplexer Datentypen
5. **NoSQL-Datenbanken** (ab 2000): Nicht-relationale Ansätze für große Datenmengen
6. **NewSQL** (ab 2010): Kombination aus relationalen und NoSQL-Konzepten

## Vor- und Nachteile von Datenbanksystemen

### Vorteile
- **Datenintegrität**: Gewährleistung der Genauigkeit und Konsistenz
- **Datensicherheit**: Zugriffskontrollen und Verschlüsselung
- **Datenunabhängigkeit**: Trennung von Anwendungslogik und Datenstruktur
- **Konkurrenz-Management**: Mehrere Benutzer können gleichzeitig zugreifen
- **Effiziente Abfragen**: Optimierte Suche und Verarbeitung

### Nachteile
- **Komplexität**: Erfordert spezielles Wissen zur Verwaltung
- **Kosten**: Kommerzielle DBMS können teuer sein
- **Leistung**: Bei schlechtem Design können Leistungsprobleme auftreten

## DBMS-Architekturen

### Drei-Schichten-Architektur
1. **Externe Ebene**: Benutzersichten
2. **Konzeptionelle Ebene**: Logische Gesamtstruktur
3. **Interne Ebene**: Physische Speicherung

![Drei-Schichten-Architektur](/assets/images/dbms-architecture.png)

## ACID-Eigenschaften

- **Atomicity** (Atomarität): Transaktionen werden vollständig oder gar nicht ausgeführt
- **Consistency** (Konsistenz): Datenbank bleibt in einem konsistenten Zustand
- **Isolation** (Isolation): Transaktionen sind voneinander isoliert
- **Durability** (Dauerhaftigkeit): Änderungen sind permanent gespeichert

## Übungsaufgaben

1. Unterscheide zwischen den Begriffen "Datenbank", "Datenbankmanagementsystem" und "Datenbanksystem".
2. Nenne und erkläre die ACID-Eigenschaften einer Datenbanktransaktion.
3. Vergleiche die Vor- und Nachteile von Datenbankansätzen gegenüber Dateisystemen.

## Kommende Vorlesung

In der nächsten Vorlesung werden wir das relationale Datenbankmodell im Detail betrachten und die Grundlagen der relationalen Algebra einführen.

## Notizen für mich

- Dozent empfiehlt die Installation von PostgreSQL als Übungsumgebung
- Projekt-Deadline: 15.12.2024
- Fragen zu klären: Unterschied zwischen B-Baum und B+-Baum Indizierung