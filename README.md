# HelpDesk API

Backend REST développé avec **Django** et **Django REST Framework** permettant de gérer un système de support informatique inspiré de GLPI.

Le projet est réalisé dans un objectif d'apprentissage afin d'appliquer les bonnes pratiques utilisées dans les équipes Backend professionnelles.

---

# Objectifs

Ce projet a pour objectifs de :

- Comprendre l'architecture d'une application Django professionnelle.
- Maîtriser Django et Django REST Framework.
- Concevoir une API REST robuste et maintenable.
- Utiliser PostgreSQL comme base de données relationnelle.
- Conteneuriser l'application avec Docker.
- Mettre en place des tests automatisés.
- Intégrer des outils de qualité de code.
- Construire une pipeline CI/CD.
- Déployer l'application.
- Intégrer l'API GLPI.
- Découvrir Kubernetes du point de vue d'un développeur Backend.

---

# État actuel du projet

Fonctionnalités actuellement implémentées :

- ✅ Conteneurisation avec Docker
- ✅ Base de données PostgreSQL
- ✅ Configuration avec les variables d'environnement
- ✅ Architecture Django professionnelle
- ✅ Modèle utilisateur personnalisé (`Custom User Model`)
- ✅ Interface d'administration Django
- ✅ Gestion des migrations

---

# Architecture

```text
helpdesk-api/
│
├── docker/
│   └── Dockerfile
│
├── requirements/
│   └── development.txt
│
├── src/
│   ├── apps/
│   │   └── users/
│   ├── config/
│   └── manage.py
│
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

---

# Stack technique

## Backend

- Python 3.13
- Django 5.2
- Django REST Framework 3.16

## Base de données

- PostgreSQL 17

## Conteneurisation

- Docker
- Docker Compose

## Configuration

- django-environ

## Versionnement

- Git
- GitHub

## Outils prévus

- Black
- isort
- Flake8
- Bandit
- pre-commit
- Pytest
- GitHub Actions
- Gunicorn
- Nginx
- Kubernetes

---

# Prérequis

Avant de lancer le projet, installez :

- Git
- Docker Desktop

Aucun environnement virtuel Python n'est nécessaire.

Toute l'application s'exécute dans Docker.

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/esprit-24/helpdesk-api.git
```

```bash
cd helpdesk-api
```

---

## 2. Créer le fichier `.env`

Copier :

```text
.env.example
```

vers

```text
.env
```

Puis modifier les valeurs.

---

## 3. Construire les conteneurs

```bash
docker compose up --build -d
```

---

## 4. Appliquer les migrations

```bash
docker compose exec web python manage.py migrate
```

---

## 5. Créer un superutilisateur

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 6. Accéder à l'application

API :

```text
http://localhost:8000/
```

Administration :

```text
http://localhost:8000/admin/
```

---

# Variables d'environnement

Le fichier `.env.example` sert de modèle.

```env
POSTGRES_DB=helpdesk_db
POSTGRES_USER=helpdesk_user
POSTGRES_PASSWORD=change_me

POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=True
DJANGO_SECRET_KEY=change_me
```

## Générer une SECRET_KEY

Dans un terminal :

```bash
docker compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Remplacer ensuite :

```text
DJANGO_SECRET_KEY=change_me
```

par la clé générée.

> Le fichier `.env` ne doit jamais être versionné.

---

# Commandes utiles

Construire les conteneurs :

```bash
docker compose up --build -d
```

Arrêter les conteneurs :

```bash
docker compose down
```

Arrêter les conteneurs et supprimer les données PostgreSQL :

```bash
docker compose down -v
```

Afficher les conteneurs :

```bash
docker compose ps
```

Afficher les logs :

```bash
docker compose logs web
```

Créer une migration :

```bash
docker compose exec web python manage.py makemigrations
```

Appliquer les migrations :

```bash
docker compose exec web python manage.py migrate
```

Créer un superutilisateur :

```bash
docker compose exec web python manage.py createsuperuser
```

Exécuter une commande Django depuis le conteneur :

```bash
docker compose exec web python manage.py <commande>
```

---

# Roadmap

## Infrastructure

- [x] Initialisation du projet
- [x] Docker
- [x] PostgreSQL
- [x] Variables d'environnement

## Authentification

- [x] Application `users`
- [x] Modèle utilisateur personnalisé
- [x] Django Admin

## Domaine métier

- [ ] Tickets
- [ ] Catégories
- [ ] Priorités
- [ ] Statuts
- [ ] Affectations
- [ ] Commentaires
- [ ] Pièces jointes

## API

- [ ] Django REST Framework
- [ ] Authentification JWT
- [ ] Documentation OpenAPI

## Qualité

- [ ] Tests
- [ ] Black
- [ ] isort
- [ ] Flake8
- [ ] Bandit
- [ ] pre-commit

## DevOps

- [ ] GitHub Actions
- [ ] Déploiement
- [ ] Intégration GLPI
- [ ] Kubernetes

---

# Licence

Projet réalisé dans un objectif d'apprentissage.