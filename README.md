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
- ✅ Black
- ✅ isort
- ✅ Flake8
- ✅ Bandit
- ✅ pre-commit

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
├── .flake8
├── .pre-commit-config.yaml
├── .env.example
├── .gitignore
├── compose.yaml
├── pyproject.toml
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

## Outils de qualité

- Black 26.5.1
- isort 8.0.1
- Flake8 7.3.0
- Bandit 1.9.4
- pre-commit 4.6.1

---

# Prérequis

Avant de lancer le projet, assurez-vous de disposer des outils suivants :

- Git
- Docker Desktop
- Python 3.14+ sur la machine hôte pour installer `pre-commit`

> **Remarque :**
> L'application Django et les principaux outils de développement sont exécutés dans des conteneurs Docker.
> Un environnement virtuel Python local (`.venv`) est utilisé uniquement pour exécuter `pre-commit` comme hook Git sur la machine du développeur.

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

## 2. Préparer l'environnement local pour pre-commit

Créer un environnement virtuel Python :

```bash
python -m venv .venv
```

Installer `pre-commit` :

```bash
.venv\Scripts\python.exe -m pip install pre-commit==4.6.1
```

Installer le hook Git :

```bash
.venv\Scripts\pre-commit.exe install
```

Vérifier l'installation :

```bash
.venv\Scripts\pre-commit.exe --version
```

---

## 3. Créer le fichier `.env`

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

## 4. Construire et démarrer les conteneurs

```bash
docker compose up --build -d
```

Vérifier que les conteneurs sont démarrés :

```bash
docker compose ps
```

---

## 5. Appliquer les migrations

```bash
docker compose exec web python manage.py migrate
```

---

## 6. Créer un superutilisateur (optionnel)

```bash
docker compose exec web python manage.py createsuperuser
```

Cette commande permet de créer un superutilisateur Django.

---

## 7. Initialiser les données de développement

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

## 8. Vérifier la configuration

```bash
docker compose exec web python manage.py check
```

La commande doit retourner :

```text
System check identified no issues (0 silenced).
```

---

## 9. Exécuter les tests

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

### Vérifier la qualité du code

Les outils de qualité sont exécutés automatiquement par `pre-commit` avant chaque commit.

Pour exécuter manuellement tous les hooks sur l'ensemble du projet :

```bash
.venv\Scripts\pre-commit.exe run --all-files
```

---

## 10. Obtenir un JWT

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

## 11. Accéder à l'application

API REST

```text
http://localhost:8000/
```

Administration Django

```text
http://localhost:8000/admin/
```

## 12. Documentation de l'API

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

## Qualité du code

Exécuter tous les hooks `pre-commit` sur l'ensemble du projet :

```bash
.venv\Scripts\pre-commit.exe run --all-files
```

---

# Workflow Git

Chaque fonctionnalité est développée dans une branche dédiée.

Le workflow suivi est le suivant :

1. Créer une branche de fonctionnalité (`feature/...`) à partir de `main`.
2. Développer la fonctionnalité.
3. Exécuter les tests avec Pytest.
4. Ajouter les fichiers à l'index avec `git add`.
5. Créer un ou plusieurs commits atomiques en suivant les conventions de nommage.
   Les hooks `pre-commit` exécutent automatiquement Black, isort, Flake8 et Bandit avant chaque commit.
6. Pousser la branche sur GitHub.
7. Ouvrir une Pull Request.
8. Effectuer la revue de code.
9. Fusionner la Pull Request dans `main`.
10. Revenir sur `main` et récupérer les dernières modifications.
11. Supprimer les branches locale et distante.

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

### ✅ US-401 — Mise en place de Pytest

- [x] Installation de Pytest
- [x] Configuration de Pytest
- [x] `pytest.ini`
- [x] `conftest.py`
- [x] Fixtures Pytest
- [x] Organisation des tests

### ✅ US-402 — Tests du domaine métier

- [x] Tests des modèles
- [x] Tests des règles métier couvertes
- [x] Tests unitaires

### ✅ US-403 — Tests de l'API

- [x] Tests des serializers
- [x] Tests des permissions
- [x] Tests des ViewSets
- [x] Tests d'intégration de l'API

### ✅ US-404 — Validation de la suite de tests

- [x] 117 tests automatisés
- [x] 117 tests passent

### ✅ US-405 — Formatage et organisation du code

- [x] Black
- [x] isort
- [x] Configuration du formatage
- [x] Vérification de la qualité du code

### ✅ US-406 — Analyse statique et sécurité

- [x] Flake8
- [x] Bandit
- [x] Configuration des outils
- [x] Exclusion appropriée des migrations

### ✅ US-407 — Automatisation de la qualité avec pre-commit

- [x] Configuration de `.pre-commit-config.yaml`
- [x] Installation de pre-commit
- [x] Installation du hook Git
- [x] Exécution automatique avant les commits
- [x] Exécution des hooks sur l'ensemble du projet
- [x] Black
- [x] isort
- [x] Flake8
- [x] Bandit

**État :** ✅ Terminé

---

## Sprint 5 — Alignement fonctionnel GLPI

### US-501 — Référentiel fonctionnel GLPI

- [ ] Étudier le modèle fonctionnel HelpDesk de GLPI
- [ ] Identifier les concepts métier de GLPI
- [ ] Identifier les acteurs d'un ticket
- [ ] Identifier le cycle de vie d'un ticket
- [ ] Définir le périmètre fonctionnel retenu

### US-502 — Alignement du modèle Ticket

- [ ] Comparer le modèle `Ticket` avec le modèle GLPI
- [ ] Clarifier le rôle de `requester`
- [ ] Clarifier le rôle de `owner`
- [ ] Revoir les statuts et le cycle de vie
- [ ] Revoir les priorités et catégories
- [ ] Définir les règles de fermeture et de résolution

### US-503 — Alignement du modèle Assignment

- [ ] Comparer les affectations avec le fonctionnement GLPI
- [ ] Clarifier le rôle du technicien affecté
- [ ] Clarifier le rôle de `assigned_by`
- [ ] Définir le rôle de `assigned_at`
- [ ] Définir le rôle de `ended_at`
- [ ] Décider du maintien ou de la suppression de `is_primary`
- [ ] Définir les règles de réaffectation

### US-504 — Concepts HelpDesk complémentaires

- [ ] Identifier les concepts GLPI pertinents manquants
- [ ] Étudier les observateurs
- [ ] Étudier les groupes d'affectation
- [ ] Étudier les suivis
- [ ] Étudier les tâches
- [ ] Étudier les solutions
- [ ] Intégrer uniquement les concepts retenus dans le périmètre du projet

### US-505 — Contrat d'intégration GLPI

- [ ] Identifier les ressources GLPI à intégrer
- [ ] Définir le mapping entre notre domaine et GLPI
- [ ] Définir les données échangées
- [ ] Préparer une architecture d'intégration indépendante de l'API GLPI
- [ ] Définir les principes de synchronisation

### US-506 — Tests fonctionnels

- [ ] Tester la création d'un ticket
- [ ] Tester l'affectation d'un ticket
- [ ] Tester la réaffectation
- [ ] Tester les changements de statut
- [ ] Tester la résolution
- [ ] Tester la fermeture
- [ ] Tester les règles de permissions
- [ ] Valider le comportement fonctionnel retenu

**État :** ⚪ À venir

---

## Sprint 6 — PostgreSQL avancé

### US-601 — Transactions

- [ ] Comprendre les transactions PostgreSQL
- [ ] Comprendre ACID
- [ ] Comprendre `COMMIT` et `ROLLBACK`
- [ ] Comprendre les niveaux d'isolation
- [ ] Utiliser `transaction.atomic()` avec Django
- [ ] Tester les scénarios de rollback

### US-602 — Index et optimisation des recherches

- [ ] Comprendre les index PostgreSQL
- [ ] Index simples
- [ ] Index composites
- [ ] Identifier les requêtes nécessitant des index
- [ ] Évaluer l'impact des index

### US-603 — Analyse des performances

- [ ] Comprendre `EXPLAIN`
- [ ] Comprendre `EXPLAIN ANALYZE`
- [ ] Lire un plan d'exécution
- [ ] Identifier les requêtes coûteuses
- [ ] Comparer les performances avant/après optimisation

### US-604 — Contraintes et intégrité

- [ ] Approfondir les contraintes PostgreSQL
- [ ] `PRIMARY KEY`
- [ ] `FOREIGN KEY`
- [ ] `UNIQUE`
- [ ] `NOT NULL`
- [ ] `CHECK`
- [ ] Renforcer l'intégrité des données

### US-605 — Fonctions et procédures stockées

- [ ] Comprendre les fonctions PostgreSQL
- [ ] Comprendre les procédures stockées
- [ ] Paramètres et valeurs de retour
- [ ] Appeler des fonctions/procédures depuis Django
- [ ] Identifier les cas d'utilisation pertinents
- [ ] Évaluer leurs limites

### US-606 — Triggers et vues

- [ ] Comprendre les triggers PostgreSQL
- [ ] Identifier les cas d'utilisation des triggers
- [ ] Comprendre les vues SQL
- [ ] Créer une vue
- [ ] Exploiter une vue depuis Django
- [ ] Évaluer les avantages et limites

### US-607 — Optimisation et validation

- [ ] Analyser la base de données du projet
- [ ] Identifier les optimisations pertinentes
- [ ] Appliquer les optimisations retenues
- [ ] Ajouter les tests nécessaires
- [ ] Valider les performances
- [ ] Documenter les choix techniques

**État :** ⚪ À venir

---

## Sprint 7 — CI/CD & Industrialisation

### US-701 — CI avec GitHub Actions

- [ ] GitHub Actions
- [ ] Exécution automatique des tests
- [ ] Contrôles de qualité
- [ ] Exécution de pre-commit en CI
- [ ] Validation des Pull Requests

### US-702 — Image Docker de production

- [ ] Dockerfile de production
- [ ] Optimisation de l'image
- [ ] Séparation développement / production
- [ ] Build de l'image de production

### US-703 — Serveur d'application et reverse proxy

- [ ] Gunicorn
- [ ] Nginx
- [ ] Configuration de production
- [ ] Gestion des fichiers statiques

### US-704 — Configuration et secrets

- [ ] Gestion des variables d'environnement
- [ ] Gestion des secrets
- [ ] Séparation configuration développement / production
- [ ] Sécurisation de la configuration

### US-705 — Déploiement

- [ ] Préparer l'environnement de production
- [ ] Déployer l'application
- [ ] Vérifier l'application en production
- [ ] Documenter le processus de déploiement

**État :** ⚪ À venir

---

## Sprint 8 — Intégration GLPI

### US-801 — Configuration de GLPI

- [ ] Préparer l'environnement GLPI
- [ ] Configurer l'API GLPI
- [ ] Configurer les accès API
- [ ] Tester la communication avec GLPI

### US-802 — Client REST GLPI

- [ ] Créer le client HTTP GLPI
- [ ] Gérer l'authentification
- [ ] Gérer les requêtes API
- [ ] Gérer les erreurs
- [ ] Gérer les timeouts

### US-803 — Synchronisation des tickets

- [ ] Récupérer les tickets GLPI
- [ ] Créer les tickets dans notre application
- [ ] Mettre à jour les tickets
- [ ] Synchroniser les statuts
- [ ] Synchroniser les priorités et catégories

### US-804 — Synchronisation des utilisateurs et acteurs

- [ ] Synchroniser les utilisateurs
- [ ] Synchroniser les techniciens
- [ ] Synchroniser les demandeurs
- [ ] Synchroniser les affectations

### US-805 — Synchronisation bidirectionnelle

- [ ] Définir le sens des synchronisations
- [ ] Gérer les conflits
- [ ] Éviter les doublons
- [ ] Garantir l'idempotence
- [ ] Gérer les erreurs de synchronisation

### US-806 — Tests d'intégration GLPI

- [ ] Tests du client GLPI
- [ ] Tests des synchronisations
- [ ] Tests des erreurs API
- [ ] Tests des conflits
- [ ] Tests d'intégration avec une instance GLPI

**État :** ⚪ À venir

---

## Sprint 9 — Kubernetes

### US-901 — Découverte de Kubernetes

- [ ] Comprendre les concepts Kubernetes
- [ ] Pods
- [ ] Deployments
- [ ] Services
- [ ] ConfigMaps
- [ ] Secrets

### US-902 — Déploiement de l'application

- [ ] Conteneuriser l'application pour Kubernetes
- [ ] Déployer Django
- [ ] Déployer PostgreSQL
- [ ] Configurer les services
- [ ] Configurer les variables et secrets
- [ ] Health checks

### US-903 — Exposition et scaling

- [ ] Ingress
- [ ] Exposition de l'API
- [ ] Scaling horizontal
- [ ] Gestion des ressources
- [ ] Vérification du déploiement

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

## ✅ Sprint 4 — Qualité et tests

Objectif : mettre en place une stratégie de tests automatisés et améliorer la qualité et la sécurité du code.

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