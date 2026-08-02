# HelpDesk API

## Description

HelpDesk API est une application Backend développée avec Django et Django REST Framework. Elle permet de gérer un système de support technique en offrant des fonctionnalités telles que la gestion des utilisateurs, des tickets, des commentaires, des pièces jointes et des notifications.

Ce projet est réalisé dans un objectif d'apprentissage afin de reproduire les bonnes pratiques utilisées dans les équipes Backend professionnelles.

---

## État actuel du projet

À ce stade, le projet permet de :

* Exécuter Django dans des conteneurs Docker.
* Utiliser PostgreSQL comme base de données.
* Gérer la configuration avec des variables d'environnement.
* Appliquer les migrations Django.
* Disposer d'une base de projet professionnelle pour développer l'API HelpDesk.

---

## Objectifs

Ce projet a pour objectifs de :

* Comprendre l'architecture d'une application Django professionnelle.
* Maîtriser Django et Django REST Framework.
* Concevoir et développer une API REST robuste et maintenable.
* Appliquer les bonnes pratiques de développement Backend.
* Utiliser PostgreSQL comme base de données relationnelle.
* Conteneuriser l'application avec Docker.
* Mettre en place des tests automatisés.
* Intégrer des outils de qualité de code.
* Construire une pipeline CI/CD.
* Déployer une application Django dans un environnement de production.
* Comprendre l'intégration avec GLPI.
* Découvrir Kubernetes du point de vue d'un développeur Backend.

---

## Architecture actuelle

```text
helpdesk-api/
├── docker/
│   └── Dockerfile
├── requirements/
│   └── development.txt
├── src/
│   ├── config/
│   └── manage.py
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

---

## Stack technique

### Backend

* Python 3.13
* Django 5.2
* Django REST Framework 3.16

### Base de données

* PostgreSQL 17

### Conteneurisation

* Docker
* Docker Compose

### Gestion de configuration

* django-environ 0.12

### Versionnement

* Git
* GitHub

### Outils prévus

* Black
* isort
* Flake8
* Bandit
* pre-commit
* Pytest
* GitHub Actions
* Gunicorn
* Nginx
* Kubernetes

---

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé :

* Git
* Docker Desktop

Aucun environnement virtuel Python n'est nécessaire. Le projet est exécuté entièrement dans des conteneurs Docker.

---

## Installation

### 1. Cloner le dépôt

```bash
git clone <repository-url>
cd helpdesk-api
```

### 2. Créer le fichier `.env`

Copiez le fichier `.env.example` et renommez-le en `.env`.

Renseignez ensuite les variables nécessaires.

### 3. Construire les conteneurs

```bash
docker compose up --build -d
```

### 4. Appliquer les migrations

```bash
docker compose exec web python manage.py migrate
```

### 5. Accéder à l'application

L'application est disponible à l'adresse :

```text
http://localhost:8000
```

---

## Variables d'environnement

Le projet utilise des variables d'environnement pour sa configuration.

Le fichier `.env.example` sert de modèle.

Les variables actuellement utilisées sont :

```env
POSTGRES_DB=helpdesk_db
POSTGRES_USER=helpdesk_user
POSTGRES_PASSWORD=change_me

POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=True
DJANGO_SECRET_KEY=change_me
```

> **Important**
>
> * Le fichier `.env` ne doit jamais être versionné.
> * En développement, remplacez `change_me` par vos propres valeurs.
> * En production, générez une nouvelle `DJANGO_SECRET_KEY`.

---

## Commandes utiles

Construire les conteneurs :

```bash
docker compose up --build -d
```

Arrêter les conteneurs :

```bash
docker compose down
```

Afficher les conteneurs :

```bash
docker compose ps
```

Afficher les logs :

```bash
docker compose logs web
```

Exécuter une commande Django :

```bash
docker compose exec web python manage.py <commande>
```

Appliquer les migrations :

```bash
docker compose exec web python manage.py migrate
```

---

## Roadmap

* [x] Initialisation du projet
* [x] Configuration Docker
* [x] Configuration PostgreSQL
* [x] Variables d'environnement
* [x] Première migration Django
* [ ] Création de l'application `tickets`
* [ ] Authentification
* [ ] API REST
* [ ] Tests
* [ ] Documentation OpenAPI
* [ ] CI/CD
* [ ] Déploiement
* [ ] Kubernetes

---

## Licence

Projet réalisé dans un objectif d'apprentissage.