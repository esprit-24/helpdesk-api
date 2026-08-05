# HelpDesk API

Backend REST développé avec **Django** et **Django REST Framework** permettant de gérer un système de support informatique inspiré de GLPI.

Ce projet est réalisé dans un objectif d'apprentissage afin d'appliquer les bonnes pratiques utilisées dans les équipes Backend professionnelles.

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
- ✅ Domaine métier des tickets
  - Gestion des statuts
  - Gestion des priorités
  - Gestion des catégories
  - Gestion des tickets
  - Gestion des affectations
- ✅ Interface d'administration Django
- ✅ Gestion des migrations
- ✅ API REST des modèles de référence
  - Status
  - Priority
  - Category
- ✅ Commande d'initialisation des données (`seed_data`)

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
│   │   ├── users/
│   │   └── tickets/
│   │       ├── management/
│   │       ├── migrations/
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
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

## 6. Initialiser les données de référence

```bash
docker compose exec web python manage.py seed_data
```

Cette commande crée les statuts, priorités et catégories par défaut.

---

## 7. Accéder à l'application

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

Vérifier la configuration Django :

```bash
docker compose exec web python manage.py check
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

Initialiser les données de référence :

```bash
docker compose exec web python manage.py seed_data
```

Exécuter une commande Django :

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

- [x] Tickets
- [x] Catégories
- [x] Priorités
- [x] Statuts
- [x] Affectations
- [ ] Commentaires
- [ ] Pièces jointes
- [ ] Notifications

## API

## API

- [x] Django REST Framework
- [x] API REST des statuts
- [x] API REST des priorités
- [x] API REST des catégories
- [ ] API REST des tickets
- [ ] API REST des affectations
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

# Historique des sprints

## Sprint 1

- Initialisation du projet
- Docker
- PostgreSQL
- Configuration avec les variables d'environnement
- Modèle utilisateur personnalisé
- Django Admin

## Sprint 2

- Application `tickets`
- Gestion des statuts
- Gestion des priorités
- Gestion des catégories
- Modèle `Ticket`
- Modèle `Assignment`
- Administration des tickets et des affectations

## Sprint 3

- Configuration de Django REST Framework
- API REST des statuts
- API REST des priorités
- API REST des catégories
- Commande `seed_data`
- API des tickets (en cours)

---

# Licence

Projet réalisé dans un objectif d'apprentissage.