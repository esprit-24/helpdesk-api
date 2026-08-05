# HelpDesk API

Backend REST développé avec **Django** et **Django REST Framework** permettant de gérer un système de support informatique inspiré de **GLPI**.

Ce projet est réalisé dans un objectif d'apprentissage afin d'appliquer les bonnes pratiques utilisées dans les équipes Backend professionnelles.

L'objectif n'est pas uniquement de développer une API fonctionnelle, mais également de reproduire un workflow de développement utilisé dans les équipes professionnelles :

- Architecture modulaire
- Git Flow
- Pull Requests
- Revues de code
- Documentation
- Tests
- Intégration Continue (CI)
- Déploiement

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

## Infrastructure

- ✅ Conteneurisation avec Docker
- ✅ Base de données PostgreSQL
- ✅ Configuration avec les variables d'environnement
- ✅ Architecture Django professionnelle

## Authentification

- ✅ Modèle utilisateur personnalisé (`Custom User Model`)

## Domaine métier

- ✅ Gestion des statuts
- ✅ Gestion des priorités
- ✅ Gestion des catégories
- ✅ Gestion des tickets
- ✅ Gestion des affectations

## Administration

- ✅ Interface d'administration Django

## Base de données

- ✅ Gestion des migrations
- ✅ Commande d'initialisation des données (`seed_data`)

## API REST

## API REST

- ✅ Django REST Framework
- ✅ API REST des statuts
- ✅ API REST des priorités
- ✅ API REST des catégories
- ✅ API REST des tickets

---

# Architecture du projet

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
│   │   │   ├── admin.py
│   │   │   ├── models.py
│   │   │   └── serializers.py
│   │   │
│   │   └── tickets/
│   │       ├── management/
│   │       │   └── commands/
│   │       │       └── seed_data.py
│   │       ├── migrations/
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
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

- django-environ 0.12

## Versionnement

- Git
- GitHub

## Outils prévus

- Pytest
- Black
- isort
- Flake8
- Bandit
- pre-commit
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

L'ensemble de l'application s'exécute dans Docker.

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/esprit-24/helpdesk-api.git
```

Se placer dans le dossier du projet :

```bash
cd helpdesk-api
```

---

## 2. Créer le fichier `.env`

Copier le fichier :

```text
.env.example
```

vers :

```text
.env
```

Puis adapter les valeurs à votre environnement.

---

## 3. Construire et démarrer les conteneurs

```bash
docker compose up --build -d
```

Vérifier que les conteneurs sont démarrés :

```bash
docker compose ps
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

Cette commande crée automatiquement :

- les statuts ;
- les priorités ;
- les catégories.

La commande est **idempotente** : elle peut être exécutée plusieurs fois sans créer de doublons.

---

## 7. Vérifier la configuration

```bash
docker compose exec web python manage.py check
```

La commande doit retourner :

```text
System check identified no issues (0 silenced).
```

---

## 8. Accéder à l'application

API REST :

```text
http://localhost:8000/
```

Administration Django :

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

## Docker

Construire et démarrer les conteneurs :

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

---

## Django

Vérifier la configuration Django :

```bash
docker compose exec web python manage.py check
```

Créer des migrations :

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

# Workflow Git

Chaque fonctionnalité est développée dans une branche dédiée.

Le workflow suivi est le suivant :

1. Créer une branche de fonctionnalité à partir de `main`.
2. Développer la fonctionnalité.
3. Tester le code.
4. Mettre à jour le README si nécessaire.
5. Créer un ou plusieurs commits atomiques.
6. Pousser la branche sur GitHub.
7. Ouvrir une Pull Request.
8. Effectuer la revue de code.
9. Fusionner la Pull Request dans `main`.
10. Revenir sur `main` et récupérer les dernières modifications.
11. Supprimer les branches locale et distante.

Exemple :

```bash
git checkout main
git pull

git checkout -b feature/my-feature

# Développement...

git add .
git commit -m "feat(...): ..."
git push -u origin feature/my-feature
```

Après la fusion :

```bash
git checkout main
git pull

git branch -d feature/my-feature
git push origin --delete feature/my-feature
```

---

# Convention de commits

Le projet suit la convention **Conventional Commits**.

Les principaux types utilisés sont :

| Type | Description |
|------|-------------|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Refactorisation sans modification fonctionnelle |
| `test` | Ajout ou modification de tests |
| `chore` | Maintenance du projet |

Exemples :

```text
feat(users): create custom user model

feat(tickets): implement ticket management domain

feat(api): expose reference models API

feat(seed): add reference data seeding command

docs: update README
```

Les commits doivent être :

- atomiques ;
- explicites ;
- centrés sur une seule fonctionnalité.

---

# Roadmap

## Sprint 1 — Infrastructure

### ✅ US-101 — Initialisation du projet

- [x] Structure du projet
- [x] README
- [x] Docker

### ✅ US-102 — Configuration

- [x] PostgreSQL
- [x] Variables d'environnement

### ✅ US-103 — Authentification

- [x] Application `users`
- [x] Modèle utilisateur personnalisé
- [x] Django Admin

---

## Sprint 2 — Domaine métier

### ✅ US-201 — Modèles de référence

- [x] Statuts
- [x] Priorités
- [x] Catégories

### ✅ US-202 — Tickets

- [x] Modèle `Ticket`

### ✅ US-203 — Affectations

- [x] Modèle `Assignment`

### ✅ US-204 — Administration

- [x] Django Admin

---

## Sprint 3 — API REST

### ✅ US-301 — Configuration de Django REST Framework

- [x] Installation de Django REST Framework
- [x] Configuration du projet

### ✅ US-302 — API des statuts

- [x] Serializer
- [x] ViewSet
- [x] Routes

### ✅ US-303 — API des modèles de référence

- [x] API des priorités
- [x] API des catégories

### ✅ US-303.5 — Données de référence

- [x] Commande `seed_data`

### ✅ US-304 — API des tickets

- [x] Serializer
- [x] ViewSet
- [x] Endpoints

### ⏳ US-305 — API des affectations

- [ ] Serializer
- [ ] ViewSet
- [ ] Endpoints

### ⏳ US-306 — Authentification JWT

- [ ] JWT
- [ ] Permissions

### ⏳ US-307 — Documentation OpenAPI

- [ ] Documentation interactive

---

## Sprint 4 — Qualité

- [ ] Tests unitaires
- [ ] Tests d'API
- [ ] Pytest
- [ ] Black
- [ ] isort
- [ ] Flake8
- [ ] Bandit
- [ ] pre-commit

---

## Sprint 5 — Industrialisation

- [ ] GitHub Actions
- [ ] Déploiement
- [ ] Gunicorn
- [ ] Nginx

---

## Sprint 6 — Intégration GLPI

- [ ] Authentification GLPI
- [ ] Synchronisation avec GLPI

---

## Sprint 7 — Kubernetes

- [ ] Découverte de Kubernetes
- [ ] Déploiement de l'application

---

# Historique des sprints

## Sprint 1

- US-101 — Initialisation du projet
- US-102 — Configuration PostgreSQL
- US-103 — Application `users`

---

## Sprint 2

- US-201 — Modèles de référence
- US-202 — Modèle `Ticket`
- US-203 — Modèle `Assignment`
- US-204 — Administration Django

---

## Sprint 3

- US-301 — Configuration de Django REST Framework
- US-302 — API REST des statuts
- US-303 — API REST des priorités et catégories
- US-303.5 — Commande `seed_data`
- US-304 — API REST des tickets

---

# Licence

Projet réalisé dans un objectif d'apprentissage.

L'ensemble du code est développé dans le but d'apprendre les bonnes pratiques de développement Backend avec Django et Django REST Framework.