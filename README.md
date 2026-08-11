# HelpDesk API

Backend REST développé avec **Django** et **Django REST Framework** permettant de gérer un système de support informatique inspiré de **GLPI**.

Ce projet est réalisé dans un objectif d'apprentissage afin d'appliquer les bonnes pratiques de développement utilisées dans les équipes Backend professionnelles.

L'objectif n'est pas uniquement de développer une API fonctionnelle, mais aussi de reproduire un workflow de développement proche de celui utilisé dans les équipes professionnelles :

- Architecture modulaire
- Git Flow
- Pull Requests
- Revues de code
- Documentation
- Tests
- Intégration Continue (CI/CD)
- Déploiement

---

# Objectifs

Ce projet a pour objectifs de :

- Comprendre l'architecture d'une application Django professionnelle.
- Maîtriser Django, Django REST Framework et les bonnes pratiques de développement Backend.
- Concevoir une API REST robuste et maintenable.
- Utiliser PostgreSQL comme base de données relationnelle.
- Approfondir PostgreSQL et SQL avancé.
- Comprendre les transactions, les index, les fonctions, les procédures stockées, les triggers et les vues SQL.
- Analyser et optimiser les performances des requêtes SQL.
- Conteneuriser l'application avec Docker et Docker Compose.
- Mettre en place des tests automatisés.
- Intégrer des outils de qualité de code.
- Construire une pipeline d'intégration et de déploiement continus (CI/CD).
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
- ✅ Authentification JWT
- ✅ Protection des endpoints avec JWT

## Domaine métier

- ✅ Gestion des statuts
- ✅ Gestion des priorités
- ✅ Gestion des catégories
- ✅ Gestion des tickets
- ✅ Gestion des affectations

## Administration

- ✅ Interface d'administration Django
- ✅ Gestion des rôles utilisateurs
- ✅ Contrôle d'accès basé sur les rôles (RBAC) et les règles métier

## Base de données

- ✅ PostgreSQL
- ✅ Gestion des migrations Django
- ✅ Commande d'initialisation des utilisateurs (`seed_users`)
- ✅ Commande d'initialisation des données de référence (`seed_tickets`)

## API REST

- ✅ Django REST Framework
- ✅ API REST des statuts
- ✅ API REST des priorités
- ✅ API REST des catégories
- ✅ API REST des tickets
- ✅ API REST des affectations
- ✅ API REST des utilisateurs
- ✅ Authentification JWT
- ✅ Contrôle d'accès basé sur les rôles (RBAC) et les règles métier
- ✅ Permissions métier sur les tickets, affectations et données de référence
- ✅ Documentation OpenAPI
- ✅ Swagger UI
- ✅ ReDoc

## Qualité et tests

- ✅ Tests des modèles
- ✅ Tests des permissions
- ✅ Tests des serializers
- ✅ Tests des ViewSets
- ✅ Fixtures Pytest
- ✅ `conftest.py`
- ✅ Tests unitaires
- ✅ Tests d'intégration de l'API
- ✅ 117 tests automatisés
- ✅ 117 tests passent

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
│   │   │   ├── management/
│   │   │   │   └── commands/
│   │   │   │       └── seed_users.py
│   │   │   ├── migrations/
│   │   │   ├── admin.py
│   │   │   ├── models.py
│   │   │   ├── permissions.py
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   │
│   │   └── tickets/
│   │       ├── management/
│   │       │   └── commands/
│   │       │       └── seed_tickets.py
│   │       ├── migrations/
│   │       ├── admin.py
│   │       ├── models.py
│   │       ├── permissions.py
│   │       ├── serializers.py
│   │       ├── urls.py
│   │       └── views.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   └── manage.py
│
├── tests/
│   ├── tickets/
│   │   ├── conftest.py
│   │   ├── test_models.py
│   │   ├── test_permissions.py
│   │   ├── test_serializers.py
│   │   └── test_views.py
│   │
│   ├── users/
│   │   ├── conftest.py
│   │   ├── test_models.py
│   │   ├── test_permissions.py
│   │   ├── test_serializers.py
│   │   └── test_views.py
│   │
│   └── test_smoke.py
│
├── compose.yaml
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md
```

> **Remarque :**
> Cette arborescence présente uniquement les principaux fichiers du projet afin de faciliter la lecture du README.

## Organisation du projet

- **docker/** : configuration de l'image Docker.
- **requirements/** : dépendances Python du projet.
- **src/apps/users/** : gestion des utilisateurs, des rôles et des permissions.
- **src/apps/tickets/** : gestion des tickets, des affectations et des données de référence.
- **src/config/** : configuration globale de Django (settings et routes principales).
- **tests/** : tests automatisés organisés par application et par responsabilité (modèles, permissions, serializers et ViewSets).

---

# Stack technique

## Backend

- Python 3.13
- Django 5.2.6
- Django REST Framework 3.16.1
- Simple JWT 5.5.1
- drf-spectacular 0.29.0

## Base de données

- PostgreSQL 17
- psycopg 3.3.4

## Conteneurisation

- Docker
- Docker Compose

## Configuration

- django-environ 0.12.0
- Variables d'environnement (`.env`)

## Versionnement

- Git
- GitHub

## Tests

- Pytest 9.1.1
- pytest-django 4.12.0

## Outils de qualité et d'industrialisation

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

Avant de lancer le projet, assurez-vous de disposer des outils suivants :

- Git
- Docker Desktop

> **Remarque :**
> Aucun environnement virtuel Python n'est nécessaire. L'ensemble de l'application et des outils de développement s'exécute dans des conteneurs Docker.

---

# Installation

Les commandes suivantes doivent être exécutées depuis un terminal.

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

Puis adaptez les valeurs à votre environnement.

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

## 5. Créer un superutilisateur (optionnel)

```bash
docker compose exec web python manage.py createsuperuser
```

Cette commande permet de créer un superutilisateur Django.

---

## 6. Initialiser les données de développement

```bash
docker compose exec web python manage.py seed_users

docker compose exec web python manage.py seed_tickets
```

Ces commandes initialisent les données de développement en créant automatiquement :

- les utilisateurs de démonstration ;
- les statuts ;
- les priorités ;
- les catégories.

Le mot de passe des utilisateurs créés est défini par la variable d'environnement :

```text
DEFAULT_USER_PASSWORD
```

Les commandes sont **idempotentes** : elles peuvent être exécutées plusieurs fois sans créer de doublons.

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

## 8. Exécuter les tests

### Exécuter l'ensemble de la suite de tests : 

```bash
docker compose exec web pytest
```

### Exécuter les tests de l'application `users` : 

```bash
docker compose exec web pytest tests/users/
```

### Exécuter les tests de l'application `tickets` : 

```bash
docker compose exec web pytest tests/tickets/
```

La suite actuelle contient `117 tests automatisés.`

---

## 9. Obtenir un JWT

Authentifiez-vous avec l'un des utilisateurs créés par `seed_users` ou avec votre superutilisateur.

### Endpoint

```text
POST /api/token/
```

### Corps de la requête

```json
{
    "username": "votre_username",
    "password": "votre_mot_de_passe"
}
```

### Réponse

```json
{
    "access": "...",
    "refresh": "..."
}
```

Le token d'accès doit être envoyé dans les requêtes protégées :

```text
Authorization: Bearer <access_token>
```

---

## 10. Accéder à l'application

API REST

```text
http://localhost:8000/
```

Administration Django

```text
http://localhost:8000/admin/
```
## 11. Documentation de l'API

Swagger UI :

```text
http://localhost:8000/api/docs/
```

ReDoc :

```text
http://localhost:8000/api/redoc/
```

Schéma OpenAPI : 

```text
http://localhost:8000/api/schema/
```

---

# Variables d'environnement

Le fichier `.env.example` sert de modèle pour créer le fichier `.env`.

```env
POSTGRES_DB=helpdesk_db
POSTGRES_USER=helpdesk_user
POSTGRES_PASSWORD=change_me

POSTGRES_HOST=db
POSTGRES_PORT=5432

DJANGO_DEBUG=True
DJANGO_SECRET_KEY=change_me

DEFAULT_USER_PASSWORD=change_me
```

## Générer une `SECRET_KEY`

Exécutez la commande suivante pour générer une clé secrète :

```bash
docker compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Remplacez ensuite :

```text
DJANGO_SECRET_KEY=change_me
```

par la clé générée.

## `DEFAULT_USER_PASSWORD`

Cette variable définit le mot de passe utilisé par la commande `seed_users` pour créer les utilisateurs de démonstration.

Vous pouvez la modifier avant d'exécuter la commande :

```bash
docker compose exec web python manage.py seed_users
```

> **Important :**
> Le fichier `.env` contient des informations sensibles et ne doit jamais être versionné.

---

# Commandes de développement

## Docker

Construire et démarrer les conteneurs :

```bash
docker compose up --build -d
```

Démarrer les conteneurs sans reconstruire les images : 

```bash
docker compose up -d
```

Arrêter les conteneurs :

```bash
docker compose down
```

Arrêter les conteneurs et supprimer les données PostgreSQL :

```bash
docker compose down -v
```

Afficher les conteneurs en cours d'exécution :

```bash
docker compose ps
```

Afficher les logs du conteneur web :

```bash
docker compose logs web
```

Ouvrir un terminal dans le conteneur web :

```bash
docker compose exec web bash
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

Initialiser les données de développement :

```bash
docker compose exec web python manage.py seed_users

docker compose exec web python manage.py seed_tickets
```

Créer un superutilisateur :

```bash
docker compose exec web python manage.py createsuperuser
```

Exécuter une commande Django :

```bash
docker compose exec web python manage.py <commande>
```

## Tests

Exécuter l'ensemble de la suite de tests : 

```bash
docker compose exec web pytest
```

Exécuter les tests de l'application `users`: 

```bash
docker compose exec web pytest tests/users/
```

Exécuter les tests de l'application `tickets`: 

```bash
docker compose exec web pytest tests/tickets/
```

---

# Workflow Git

Chaque fonctionnalité est développée dans une branche dédiée.

Le workflow suivi est le suivant :

1. Créer une branche de fonctionnalité (`feature/...`) à partir de `main`.
2. Développer la fonctionnalité.
3. Tester le code.
4. Mettre à jour le README si nécessaire.
5. Créer un ou plusieurs commits atomiques en suivant les conventions de nommage.
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

Le projet suit la convention **Conventional Commits** afin de produire un historique Git clair, cohérent et facilement exploitable.

Les principaux types utilisés sont :

| Type | Description |
|------|-------------|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Refactorisation sans modification fonctionnelle |
| `test` | Ajout ou modification de tests |
| `chore` | Tâches de maintenance |

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
- centrés sur une seule fonctionnalité ;
- rédigés en anglais.

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
- [x] Interface d'administration Django

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

- [x] Configuration de l'administration Django

---

## Sprint 3 — API REST

### ✅ US-301 — Configuration de Django REST Framework

- [x] Installation de Django REST Framework
- [x] Configuration du projet

### ✅ US-302 — API des statuts

- [x] Serializer
- [x] ViewSet
- [x] Endpoints

### ✅ US-303 — API des modèles de référence

- [x] API des priorités
- [x] API des catégories

### ✅ US-303.5 — Données de référence

- [x] Commande `seed_users`
- [x] Commande `seed_tickets`

### ✅ US-304 — API des tickets

- [x] Serializer
- [x] ViewSet
- [x] Endpoints

### ✅ US-305 — API des affectations

- [x] Serializer
- [x] ViewSet
- [x] Endpoints

### ✅ US-306 — Authentification JWT

- [x] Installation de Simple JWT
- [x] Endpoints JWT
- [x] Authentification par défaut
- [x] Protection des endpoints
- [x] Utilisation de `request.user`

### ✅ US-307 — API des utilisateurs

- [x] `UserReadSerializer`
- [x] `UserViewSet`
- [x] Endpoints
- [x] `ReadOnlyModelViewSet`

### ✅ US-308 — Gestion des rôles et permissions

- [x] Permissions basées sur les rôles
- [x] Contrôle d'accès selon le rôle utilisateur
- [x] Protection des endpoints
- [x] Permissions sur les tickets
- [x] Permissions sur les affectations
- [x] Permissions sur les données de référence (`Status`, `Priority`, `Category`)

### ✅ US-309 — Documentation OpenAPI

- [x] Installation de drf-spectacular
- [x] Génération du schéma OpenAPI
- [x] Documentation interactive avec Swagger UI
- [x] Documentation avec ReDoc
- [x] Intégration de l'authentification JWT

---

## Sprint 4 — Qualité

- [x] Tests des modèles
- [x] Tests des permissions
- [x] Tests des serializers
- [x] Tests des ViewSets
- [x] Fixtures Pytest
- [x] `conftest.py`
- [x] Tests unitaires
- [x] Tests d'intégration de l'API
- [x] Pytest
- [x] 117 tests automatisés
- [ ] Black
- [ ] isort
- [ ] Flake8
- [ ] Bandit
- [ ] pre-commit

**État :** 🟡 En cours

---

## Sprint 5 — PostgreSQL avancé

- [ ] Comprendre les transactions PostgreSQL
- [ ] Comprendre les niveaux d'isolation
- [ ] Approfondir les contraintes d'intégrité
- [ ] Index et index composites
- [ ] Requêtes SQL avancées
- [ ] Fonctions PostgreSQL
- [ ] Procédures stockées
- [ ] Triggers PostgreSQL
- [ ] Vues SQL
- [ ] Analyse des performances avec `EXPLAIN`
- [ ] Analyse des performances avec `EXPLAIN ANALYZE`
- [ ] Intégration des fonctionnalités PostgreSQL avec Django

**État :** ⚪ À venir

---

## Sprint 6 — Industrialisation

- [ ] GitHub Actions
- [ ] Gunicorn
- [ ] Nginx
- [ ] Déploiement

**État :** ⚪ À venir

---

## Sprint 7 — Intégration GLPI

- [ ] Authentification GLPI
- [ ] Synchronisation avec GLPI

**État :** ⚪ À venir

---

## Sprint 8 — Kubernetes

- [ ] Découverte de Kubernetes
- [ ] Déploiement de l'application

**État :** ⚪ À venir

---

# Historique des sprints

## ✅ Sprint 1 — Infrastructure

Objectif : mettre en place les fondations techniques du projet.

User Stories réalisées :

- US-101 — Initialisation du projet
- US-102 — Configuration PostgreSQL
- US-103 — Application `users`

---

## ✅ Sprint 2 — Domaine métier

Objectif : modéliser le domaine fonctionnel du HelpDesk.

User Stories réalisées :

- US-201 — Modèles de référence
- US-202 — Modèle `Ticket`
- US-203 — Modèle `Assignment`
- US-204 — Administration Django

---

## ✅ Sprint 3 — API REST

Objectif : exposer le domaine métier via une API REST sécurisée.

User Stories réalisées :

- US-301 — Configuration de Django REST Framework
- US-302 — API REST des statuts
- US-303 — API REST des priorités et catégories
- US-303.5 — Initialisation des données de référence
- US-304 — API REST des tickets
- US-305 — API REST des affectations
- US-306 — Authentification JWT
- US-307 — API REST des utilisateurs
- US-308 — Gestion des rôles et permissions
- US-309 — Documentation OpenAPI

---

## 🟡 Sprint 4 — Qualité et tests

Objectif : mettre en place une stratégie de tests automatisés et améliorer la qualité du code.

Travail réalisé :

- Tests des modèles
- Tests des permissions
- Tests des serializers
- Tests des ViewSets
- Fixtures Pytest
- Organisation des fixtures avec `conftest.py`
- Tests unitaires
- Tests d'intégration de l'API
- 117 tests automatisés
- 117 tests passent

Travail restant :

- Black
- isort
- Flake8
- Bandit
- pre-commit

---

# À propos du projet

Ce projet est réalisé dans un objectif d'apprentissage.

Il a pour but de mettre en pratique les bonnes pratiques de développement Backend avec Django, Django REST Framework et les outils couramment utilisés dans les équipes professionnelles.

Le projet évolue progressivement au fil des sprints afin de reproduire un cycle de développement proche de celui rencontré en entreprise.