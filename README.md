# WebGuardian Scanner 🛡️

**WebGuardian Scanner** est un scanner léger de vulnérabilités web, écrit en Python et entièrement dockerisé. Il permet d’analyser rapidement les sites web pour détecter les failles courantes de sécurité, comme les headers manquants, les formulaires, les vulnérabilités XSS et SQL Injection.

---

## 🌟 Fonctionnalités

- Détection des **en-têtes de sécurité** : Content-Security-Policy, X-Frame-Options, X-XSS-Protection, HSTS
- Détection du **serveur web** et informations associées
- **Scan des formulaires** présents sur les pages
- Tests de **vulnérabilités XSS**
- Tests de **vulnérabilités SQL Injection**
- Entièrement **dockerisé** pour une exécution portable et rapide

---

## 📦 Prérequis

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé et en fonctionnement
- Windows, Linux ou macOS
- Connexion internet pour scanner les sites

---

## 🚀 Installation et lancement avec Docker

1️⃣ **Cloner le dépôt GitHub** :

```bash
git clone https://github.com/YassineZheou/WebGuardian-Scanner.git
cd WebGuardian-Scanner
