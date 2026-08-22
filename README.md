# HelpDesk API

API REST Backend développée avec **Django** et **Django REST Framework** pour gérer un système de support informatique inspiré de **GLPI**.

Le projet est réalisé dans un objectif d'apprentissage afin de mettre en pratique les bonnes pratiques de développement Backend utilisées dans les équipes professionnelles.

L'objectif n'est pas uniquement de construire une API fonctionnelle, mais également de reproduire progressivement un workflow proche de celui rencontré en entreprise :

- architecture modulaire ;
- Git et branches de fonctionnalités ;
- commits structurés ;
- tests automatisés ;
- revue et amélioration du code ;
- documentation ;
- contrôle qualité ;
- CI/CD ;
- déploiement.

---

# Objectifs

Le projet a pour objectifs de :

- comprendre l'architecture d'une application Django professionnelle ;

- maîtriser Django et Django REST Framework ;

- concevoir une API REST robuste, sécurisée et maintenable ;

- utiliser PostgreSQL comme base de données relationnelle ;

- conteneuriser l'application avec Docker et Docker Compose ;

- mettre en place une stratégie de tests automatisés ;

- appliquer des outils de qualité et de sécurité du code ;

- comprendre et implémenter les permissions ainsi que les règles métier ;

- documenter l'API REST avec OpenAPI ;

- mettre en place un workflow professionnel avec Git, branches de fonctionnalités, Pull Requests et revue de code ;

- construire une chaîne d'intégration continue et de déploiement avec Jenkins ;

- automatiser progressivement les vérifications et les étapes du cycle de développement ;

- construire progressivement une architecture exploitable dans un contexte professionnel.

L'approfondissement de **PostgreSQL et du SQL avancé** constitue une étape ultérieure de la roadmap. Il ne fait pas encore partie des travaux réalisés.

---

# État actuel du projet

## Infrastructure

- ✅ Docker
- ✅ Docker Compose
- ✅ PostgreSQL
- ✅ Variables d'environnement
- ✅ Architecture Django avec séparation `src/`
- ✅ Configuration de développement conteneurisée

## Utilisateurs et authentification

- ✅ Modèle utilisateur personnalisé
- ✅ Gestion des rôles
- ✅ Authentification JWT
- ✅ Protection des endpoints
- ✅ Permissions basées sur les rôles
- ✅ API des utilisateurs
- ✅ Interface d'administration Django
- ✅ Commande `seed_users`

## Domaine métier

- ✅ Statuts
- ✅ Priorités
- ✅ Catégories
- ✅ Tickets
- ✅ Affectations de techniciens
- ✅ Règles métier sur les tickets et affectations
- ✅ Un seul assignment primaire autorisé par ticket
- ✅ Validation du rôle `TECHNICIAN` lors d'une affectation

## API REST

- ✅ Django REST Framework
- ✅ API des utilisateurs
- ✅ API des statuts
- ✅ API des priorités
- ✅ API des catégories
- ✅ API des tickets
- ✅ API des affectations
- ✅ Authentification JWT
- ✅ Permissions métier
- ✅ Documentation OpenAPI
- ✅ Swagger UI
- ✅ ReDoc

## Qualité et tests

- ✅ Pytest
- ✅ pytest-django
- ✅ Tests des modèles
- ✅ Tests des serializers
- ✅ Tests des permissions
- ✅ Tests des ViewSets
- ✅ Fixtures Pytest
- ✅ `conftest.py`
- ✅ Tests d'intégration de l'API
- ✅ 120 tests automatisés actuellement
- ✅ 120 tests passent lors du dernier pipeline CI
- ✅ Black
- ✅ isort
- ✅ Flake8
- ✅ Bandit
- ✅ pre-commit

## CI/CD et industrialisation

- ✅ Jenkins
- ✅ Jenkinsfile
- ✅ Pipeline CI
- ✅ Build Docker dédié à la CI
- ✅ Environnement CI dédié
- ✅ Exécution des tests avec Pytest dans le pipeline
- ✅ Vérification de la qualité du code
- ✅ Analyse de sécurité avec Bandit
- ✅ Gestion des secrets CI avec Jenkins Credentials
- ✅ Nettoyage de l'environnement CI
- ✅ Jenkins Multibranch Pipeline
- ✅ Détection des branches Git
- 🔄 Déclenchement automatique du pipeline via GitHub Webhook
- 🔄 Détection et traitement des Pull Requests
- 🔄 Intégration GitHub Webhook → Jenkins
- 🔄 Exposition locale de Jenkins via ngrok pour les webhooks

---

# Architecture du projet

```text
helpdesk-api/
│
├── docker/
│   ├── Dockerfile
│   └── Dockerfile.ci
│
├── requirements/
│   ├── base.txt
│   ├── ci.txt
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
│   │   │   ├── apps.py
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
│   │       ├── apps.py
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
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── .flake8
├── compose.ci.yaml
├── compose.yaml
├── Jenkinsfile
├── pyproject.toml
├── pytest.ini
└── README.md
```

Le projet suit une organisation séparant le code applicatif, la configuration, les tests et les éléments d'infrastructure.

- `src/apps/users/` : gestion des utilisateurs, rôles, permissions et authentification.
- `src/apps/tickets/` : domaine métier du HelpDesk, notamment les tickets, statuts, priorités, catégories et affectations.
- `src/config/` : configuration globale du projet Django.
- `tests/` : tests organisés par application et par responsabilité.
- `docker/` : Dockerfiles utilisés pour les différents environnements.
- `requirements/` : dépendances Python séparées par environnement.
- `Jenkinsfile` : définition du pipeline CI Jenkins.
- `compose.ci.yaml` : configuration Docker Compose spécifique à l'environnement CI.

---

# Stack technique

## Backend

- Python 3.13.15
- Django 5.2.6
- Django REST Framework 3.16.1
- djangorestframework-simplejwt 5.5.1
- drf-spectacular 0.29.0
- django-environ 0.12.0

## Base de données

- PostgreSQL 17
- psycopg 3.3.4

## Conteneurisation

- Docker
- Docker Compose

## Tests

- Pytest 9.1.1
- pytest-django 4.12.0

## Qualité et sécurité

- Black 26.5.1
- isort 8.0.1
- Flake8 7.3.0
- Bandit 1.9.4
- pre-commit 4.6.1

## CI/CD et industrialisation

- Jenkins 2.575 (JDK 21)
- Jenkinsfile
- Jenkins Multibranch Pipeline
- Docker Compose 5.3.1 pour l'environnement CI
- GitHub Webhooks
- ngrok 3.39.10 pour l'exposition locale de Jenkins

## Versionnement

- Git
- GitHub

---

# Prérequis

## Développement local

Avant de lancer le projet localement, installer :

- Git ;
- Docker Desktop ;
- Python sur la machine hôte pour installer et exécuter `pre-commit`.

L'application Django et les principaux outils de développement sont exécutés dans Docker.

Un environnement virtuel Python local `.venv` est utilisé pour les outils Git, notamment `pre-commit`.

## CI/CD

Pour reproduire l'environnement CI, une infrastructure Jenkins est nécessaire avec :

- Jenkins ;
- Docker ;
- Docker Compose ;
- un accès au dépôt GitHub ;
- des credentials Jenkins pour fournir l'environnement CI sans versionner les secrets.

La configuration de Jenkins est externe au projet et n'est pas nécessaire pour exécuter l'application en développement local.

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/esprit-24/helpdesk-api.git
cd helpdesk-api
```

## 2. Préparer `pre-commit`

Créer l'environnement virtuel :

```bash
python -m venv .venv
```

Installer `pre-commit` :

```powershell
.venv\Scripts\python.exe -m pip install pre-commit==4.6.1
```

Installer le hook Git :

```powershell
.venv\Scripts\pre-commit.exe install
```

Vérifier :

```powershell
.venv\Scripts\pre-commit.exe --version
```

## 3. Créer `.env`

Copier :

```text
.env.example
```

vers :

```text
.env
```

Puis adapter les valeurs si nécessaire.

Le fichier `.env` ne doit jamais être versionné.

## 4. Construire et démarrer les conteneurs

```bash
docker compose up --build -d
```

Vérifier :

```bash
docker compose ps
```

Le projet utilise actuellement :

```text
web  → localhost:8000
db   → localhost:5432
```

## 5. Appliquer les migrations

```bash
docker compose exec web python src/manage.py migrate
```

## 6. Vérifier Django

```bash
docker compose exec web python src/manage.py check
```

Le résultat attendu est :

```text
System check identified no issues (0 silenced).
```

## 7. Initialiser les données de développement

Créer les utilisateurs de démonstration :

```bash
docker compose exec web python src/manage.py seed_users
```

Créer les données de référence :

```bash
docker compose exec web python src/manage.py seed_tickets
```

Ces commandes créent notamment :

- utilisateurs de démonstration ;
- statuts ;
- priorités ;
- catégories.

Les commandes de seed sont idempotentes : elles peuvent être exécutées plusieurs fois sans créer de doublons.

## 8. Créer un superutilisateur

Optionnel :

```bash
docker compose exec web python src/manage.py createsuperuser
```

## 9. CI Jenkins

Le projet fournit un `Jenkinsfile` qui définit le pipeline CI.

Le pipeline réalise notamment les étapes suivantes :

1. construit l'image Docker dédiée à la CI ;
2. démarre les services nécessaires ;
3. exécute les tests Pytest ;
4. vérifie la qualité du code avec Black, isort et Flake8 ;
5. analyse le code avec Bandit ;
6. nettoie l'environnement CI après l'exécution.

L'environnement CI utilise un fichier `.env.ci` fourni temporairement par Jenkins Credentials.

Ce fichier n'est pas versionné dans Git.

L'infrastructure Jenkins est indépendante du projet et peut être configurée dans un environnement dédié. Elle n'est pas nécessaire pour exécuter l'application en développement local.

---

# Tests

## Suite complète

```bash
docker compose exec web pytest
```

Résultat actuel :

```text
120 passed
```

## Tests `users`

```bash
docker compose exec web pytest tests/users/
```

## Tests `tickets`

```bash
docker compose exec web pytest tests/tickets/
```

## Vérification Django

```bash
docker compose exec web python src/manage.py check
```

## Tests dans la CI

La même suite de tests est exécutée automatiquement par le pipeline CI Jenkins :

```bash
docker compose -f compose.yaml -f compose.ci.yaml run --rm web pytest
```

Les tests doivent réussir avant que le pipeline puisse être considéré comme valide.

---

# Qualité du code

Le projet utilise `pre-commit` pour exécuter automatiquement les contrôles qualité avant les commits.

Les hooks actuels sont :

- Black ;
- isort ;
- Flake8 ;
- Bandit.

Exécuter tous les hooks manuellement :

```powershell
.venv\Scripts\pre-commit.exe run --all-files
```

Les hooks sont exécutés automatiquement lors des commits. Si un hook échoue, le commit est interrompu jusqu'à ce que le problème soit corrigé.

---

# API

Les routes principales sont exposées sous `/api/`.

## Authentification

### Obtenir un JWT

```http
POST /api/token/
```

Corps :

```json
{
    "username": "votre_username",
    "password": "votre_mot_de_passe"
}
```

Réponse :

```json
{
    "access": "...",
    "refresh": "..."
}
```

Utiliser ensuite le token d'accès :

```http
Authorization: Bearer <access_token>
```

### Rafraîchir un token

```http
POST /api/token/refresh/
```

---

## Ressources API

### Users

```text
/api/users/
```

Gestion de la consultation des utilisateurs selon les permissions et rôles.

### Statuses

```text
/api/statuses/
```

Gestion des statuts des tickets.

### Priorities

```text
/api/priorities/
```

Gestion des priorités.

### Categories

```text
/api/categories/
```

Gestion des catégories.

### Tickets

```text
/api/tickets/
```

Gestion des tickets.

### Assignments

```text
/api/assignments/
```

Gestion des affectations de techniciens.

---

# Rôles utilisateurs

Le modèle utilisateur définit quatre rôles métier :

| Rôle | Description |
|------|-------------|
| `REQUESTER` | Crée et consulte ses propres tickets |
| `TECHNICIAN` | Consulte les tickets qui lui sont affectés |
| `MANAGER` | Accès élargi aux ressources métier |
| `ADMIN` | Accès administrateur |

Les permissions sont appliquées au niveau des endpoints et des objets afin de contrôler l'accès aux ressources selon le rôle de l'utilisateur.

---

# Principales règles métier

## Tickets

Lorsqu'un ticket est créé via l'API, le demandeur est automatiquement associé à l'utilisateur authentifié.

Un demandeur ne peut consulter que ses propres tickets.

Un technicien peut consulter les tickets qui lui sont affectés.

Les managers et administrateurs disposent d'un accès plus large selon les permissions définies.

## Affectations

Une affectation associe :

- un ticket ;
- un technicien ;
- l'utilisateur ayant effectué l'affectation.

Un utilisateur affecté comme technicien doit avoir le rôle :

```text
TECHNICIAN
```

Un ticket ne peut avoir qu'une seule affectation primaire.

Cette règle est également protégée au niveau de la base de données par une contrainte d'unicité conditionnelle.

---

# Administration Django

L'interface d'administration est disponible à :

```text
http://localhost:8000/admin/
```

Elle permet notamment de gérer :

- utilisateurs ;
- statuts ;
- priorités ;
- catégories ;
- tickets ;
- affectations.

L'accès à l'interface nécessite un compte disposant des droits d'administration.

---

# Documentation de l'API

## Swagger UI

```text
http://localhost:8000/api/docs/
```
Swagger UI permet d'explorer et de tester les endpoints de l'API directement depuis le navigateur.

## ReDoc

```text
http://localhost:8000/api/redoc/
```
ReDoc fournit une présentation structurée de la documentation OpenAPI.

## Schéma OpenAPI

```text
http://localhost:8000/api/schema/
```
Cette route expose le schéma OpenAPI de l'API.

---

# Variables d'environnement

Le fichier `.env.example` sert de modèle pour créer le fichier `.env`.

Le fichier `.env` contient les valeurs spécifiques à l'environnement et ne doit jamais être versionné.

Exemple :

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

## SECRET_KEY

Une clé secrète Django peut être générée avec :

```bash
docker compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Puis renseigner la valeur générée dans `.env` :

```env
DJANGO_SECRET_KEY=<clé_générée>
```

## DEFAULT_USER_PASSWORD

Cette variable définit le mot de passe utilisé par `seed_users` pour les utilisateurs de démonstration.

Exemple :

```env
DEFAULT_USER_PASSWORD=change_me
```

---

# Workflow Git

Chaque fonctionnalité est développée dans une branche dédiée.

Workflow recommandé :

1. Créer une branche `feature/...` depuis `main`.
2. Développer la fonctionnalité.
3. Ajouter ou adapter les tests.
4. Exécuter la suite de tests.
5. Exécuter les contrôles qualité.
6. Faire un commit atomique.
7. Pousser la branche sur GitHub.
8. Ouvrir une Pull Request.
9. Jenkins détecte la Pull Request et exécute automatiquement la CI.
10. Vérifier le résultat de la CI.
11. Effectuer la revue de code.
12. Fusionner la Pull Request dans `main`.
13. Synchroniser la branche `main` locale avec `origin/main`.
14. Supprimer les branches devenues inutiles.

## CI lors d'une Pull Request

Lorsqu'une Pull Request est créée ou mise à jour, Jenkins utilise le Multibranch Pipeline pour détecter la Pull Request et exécuter le `Jenkinsfile`.

La CI vérifie notamment :

- le build de l'image Docker CI ;
- les tests Pytest ;
- Black ;
- isort ;
- Flake8 ;
- Bandit.

La Pull Request peut ensuite être revue et fusionnée lorsque les vérifications nécessaires sont satisfaisantes.

---

# Convention de commits

Le projet utilise la convention **Conventional Commits** pour structurer les messages de commit.

| Type | Description |
|------|-------------|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `refactor` | Refactorisation sans changement fonctionnel |
| `test` | Ajout ou modification de tests |
| `ci` | Modification de la configuration d'intégration continue |
| `chore` | Maintenance |

Exemples :

```text
feat(users): create custom user model

feat(tickets): implement ticket management domain

feat(api): expose reference models API

test(tickets): improve assignment coverage

refactor(tickets): improve viewset structure

ci: configure Jenkins pipeline

docs: update README
```

Les commits doivent être :

- atomiques ;
- explicites ;
- centrés sur une seule modification ;
- rédigés en anglais.

---

# Roadmap

La roadmap est volontairement progressive.

Les éléments cochés correspondent au travail réellement réalisé.

Les éléments non cochés correspondent à des étapes futures d'apprentissage et d'industrialisation.

---

## Sprint 1 — Infrastructure

### ✅ US-101 — Initialisation du projet

- [x] Structure du projet
- [x] README
- [x] Docker

### ✅ US-102 — Configuration

- [x] PostgreSQL
- [x] Variables d'environnement
- [x] Configuration Django

### ✅ US-103 — Utilisateurs

- [x] Application `users`
- [x] Modèle utilisateur personnalisé
- [x] Interface d'administration Django

**État :** ✅ Terminé

---

## Sprint 2 — Domaine métier

### ✅ US-201 — Modèles de référence

- [x] Statuts
- [x] Priorités
- [x] Catégories

### ✅ US-202 — Tickets

- [x] Modèle `Ticket`
- [x] Relations métier
- [x] Gestion du demandeur
- [x] Gestion du propriétaire

### ✅ US-203 — Affectations

- [x] Modèle `Assignment`
- [x] Affectation d'un technicien
- [x] Affectation primaire
- [x] Un seul assignment primaire par ticket

### ✅ US-204 — Administration

- [x] Configuration de l'administration Django

**État :** ✅ Terminé

---

## Sprint 3 — API REST

### ✅ US-301 — Django REST Framework

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
- [x] Seeds idempotents

### ✅ US-304 — API des tickets

- [x] Serializer
- [x] ViewSet
- [x] Endpoints
- [x] Permissions métier

### ✅ US-305 — API des affectations

- [x] Serializer
- [x] ViewSet
- [x] Endpoints
- [x] Validation du rôle technicien

### ✅ US-306 — Authentification JWT

- [x] Simple JWT
- [x] Endpoint d'obtention du token
- [x] Endpoint de refresh
- [x] Authentification par défaut
- [x] Protection des endpoints
- [x] Utilisation de `request.user`

### ✅ US-307 — API des utilisateurs

- [x] `UserReadSerializer`
- [x] `UserViewSet`
- [x] Endpoints
- [x] Permissions d'accès

### ✅ US-308 — Rôles et permissions

- [x] Permissions basées sur les rôles
- [x] Contrôle d'accès selon le rôle
- [x] Permissions sur les tickets
- [x] Permissions sur les affectations
- [x] Permissions sur les données de référence

### ✅ US-309 — Documentation OpenAPI

- [x] drf-spectacular
- [x] Schéma OpenAPI
- [x] Swagger UI
- [x] ReDoc
- [x] Documentation de l'authentification JWT

**État :** ✅ Terminé

---

## Sprint 4 — Qualité et tests

### ✅ US-401 — Pytest

- [x] Installation de Pytest
- [x] Configuration de Pytest
- [x] `pytest.ini`
- [x] `conftest.py`
- [x] Fixtures
- [x] Organisation des tests

### ✅ US-402 — Tests du domaine métier

- [x] Tests des modèles
- [x] Tests des règles métier
- [x] Tests des contraintes
- [x] Tests unitaires

### ✅ US-403 — Tests de l'API

- [x] Tests des serializers
- [x] Tests des permissions
- [x] Tests des ViewSets
- [x] Tests d'intégration de l'API

### ✅ US-404 — Validation de la suite

- [x] 120 tests automatisés
- [x] 120 tests passent

### ✅ US-405 — Formatage

- [x] Black
- [x] isort
- [x] Configuration du formatage

### ✅ US-406 — Analyse statique et sécurité

- [x] Flake8
- [x] Bandit
- [x] Configuration des outils

### ✅ US-407 — pre-commit

- [x] Configuration de `.pre-commit-config.yaml`
- [x] Installation de pre-commit
- [x] Hook Git
- [x] Exécution automatique avant les commits
- [x] Black
- [x] isort
- [x] Flake8
- [x] Bandit

**État :** ✅ Terminé

---

## Sprint 5 — CI/CD & Industrialisation

Objectif : comprendre et mettre en place progressivement une chaîne d'industrialisation pour l'application HelpDesk API.

Ce sprint ne se limite pas à écrire un fichier de pipeline. Il doit permettre de comprendre les concepts, les outils et le workflow complet allant du code jusqu'à une application vérifiée après déploiement.

### 🟡 US-501 — Comprendre CI/CD

- [x] Comprendre l'intégration continue
- [ ] Comprendre la livraison continue
- [ ] Comprendre le déploiement continu
- [x] Comprendre les notions de pipeline, job, stage, runner et agent
- [ ] Comprendre les artefacts
- [x] Comprendre les environnements
- [x] Comprendre les secrets et credentials
- [x] Comprendre les déclencheurs de pipeline

### 🟡 US-502 — Jenkins

- [x] Comprendre l'architecture Jenkins
- [ ] Comprendre controller et agent
- [x] Installer Jenkins
- [x] Configurer Jenkins
- [x] Gérer les credentials
- [x] Créer un premier job
- [x] Créer une pipeline
- [x] Comprendre le Jenkinsfile
- [x] Lire et diagnostiquer les logs Jenkins
- [x] Configurer un Multibranch Pipeline
- [x] Découvrir les branches Git avec Jenkins
- [x] Découvrir les Pull Requests avec Jenkins
- [x] Configurer l'intégration GitHub avec Jenkins
- [x] Configurer le webhook GitHub

### ✅ US-503 — Pipeline CI HelpDesk API

- [x] Checkout du code
- [x] Installation des dépendances
- [x] Exécution des tests Pytest
- [x] Exécution de Black
- [x] Exécution de isort
- [x] Exécution de Flake8
- [x] Exécution de Bandit
- [x] Build de l'image Docker
- [x] Gestion de l'environnement CI
- [x] Gestion des secrets CI avec Jenkins Credentials
- [x] Nettoyage de l'environnement CI
- [x] Comprendre l'intégration de la CI dans un workflow de Pull Request

### ⬜ US-504 — GitHub Actions

- [ ] Comprendre GitHub Actions
- [ ] Comprendre workflow, job, step et runner
- [ ] Comparer GitHub Actions avec Jenkins
- [ ] Comprendre les limites liées aux quotas et à la facturation
- [ ] Créer un exemple simple sans rendre le projet dépendant d'un abonnement payant

### ⬜ US-505 — Image Docker de production

- [ ] Comprendre la différence entre image de développement et image de production
- [ ] Créer un Dockerfile de production
- [ ] Optimiser l'image
- [ ] Configurer un utilisateur non-root
- [ ] Séparer la configuration de développement et de production

### ⬜ US-506 — Gunicorn

- [ ] Comprendre pourquoi `runserver` n'est pas utilisé en production
- [ ] Installer et configurer Gunicorn
- [ ] Lancer Django avec Gunicorn
- [ ] Comprendre le rôle du serveur d'application

### ⬜ US-507 — Nginx

- [ ] Comprendre le rôle d'un reverse proxy
- [ ] Configurer Nginx devant Gunicorn
- [ ] Gérer les fichiers statiques
- [ ] Comprendre le flux Internet → Nginx → Gunicorn → Django → PostgreSQL

### ⬜ US-508 — Configuration et secrets de production

- [ ] Séparer les environnements dev, test et prod
- [ ] Gérer les variables d'environnement
- [ ] Gérer les secrets
- [ ] Éviter l'exposition de secrets dans le dépôt
- [ ] Vérifier la configuration Django pour la production

### ⬜ US-509 — Déploiement

- [ ] Préparer un environnement de déploiement
- [ ] Déployer l'application
- [ ] Vérifier l'application après déploiement
- [ ] Documenter le processus
- [ ] Comprendre le workflow Git push → CI → tests → qualité → build Docker → déploiement → vérification

**État :** 🟡 En cours

---

## Sprint 6 — Intégration GLPI

### US-601 — Découverte de l'API GLPI

- [ ] Comprendre l'API REST de GLPI
- [ ] Identifier les ressources pertinentes
- [ ] Comprendre l'authentification
- [ ] Identifier les données à échanger

### US-602 — Client GLPI

- [ ] Créer un client REST GLPI
- [ ] Gérer l'authentification
- [ ] Gérer les requêtes API
- [ ] Gérer les erreurs
- [ ] Gérer les timeouts

### US-603 — Synchronisation des tickets

- [ ] Récupérer les tickets GLPI
- [ ] Créer les tickets dans notre application
- [ ] Mettre à jour les tickets
- [ ] Synchroniser les statuts
- [ ] Synchroniser les priorités et catégories

### US-604 — Synchronisation utilisateurs et affectations

- [ ] Synchroniser les utilisateurs
- [ ] Synchroniser les techniciens
- [ ] Synchroniser les demandeurs
- [ ] Synchroniser les affectations

### US-605 — Gestion de la synchronisation

- [ ] Définir le sens des synchronisations
- [ ] Gérer les conflits
- [ ] Éviter les doublons
- [ ] Garantir l'idempotence
- [ ] Gérer les erreurs de synchronisation

### US-606 — Tests d'intégration GLPI

- [ ] Tests du client GLPI
- [ ] Tests des synchronisations
- [ ] Tests des erreurs API
- [ ] Tests des conflits
- [ ] Tests d'intégration avec une instance GLPI

**État :** ⚪ À venir

---

## Sprint 7 — PostgreSQL et SQL avancé

> PostgreSQL est déjà utilisé par l'application.
>
> Ce sprint correspond à l'approfondissement de PostgreSQL et SQL avancé et sera réalisé ultérieurement, après l'intégration GLPI.

### US-701 — Transactions et atomicité

- [ ] Comprendre les transactions
- [ ] Comprendre ACID
- [ ] Comprendre l'atomicité
- [ ] Comprendre `COMMIT`
- [ ] Comprendre `ROLLBACK`
- [ ] Comprendre les niveaux d'isolation
- [ ] Identifier un cas métier nécessitant une transaction
- [ ] Utiliser `transaction.atomic()` avec Django
- [ ] Tester les scénarios de succès et de rollback

### US-702 — Fonctions PostgreSQL

- [ ] Comprendre les fonctions PostgreSQL
- [ ] Comprendre les paramètres et valeurs de retour
- [ ] Créer une fonction PostgreSQL
- [ ] Tester une fonction
- [ ] Appeler une fonction depuis Django

### US-703 — Procédures stockées

- [ ] Comprendre la différence entre fonction et procédure
- [ ] Comprendre `CREATE PROCEDURE`
- [ ] Déclarer des paramètres
- [ ] Utiliser `CALL`
- [ ] Créer une procédure stockée
- [ ] Utiliser une procédure dans un cas métier du HelpDesk
- [ ] Gérer les erreurs
- [ ] Tester une procédure stockée

### US-704 — Intégration avec Django

- [ ] Appeler une procédure PostgreSQL depuis Django
- [ ] Utiliser le curseur Django pour exécuter du SQL
- [ ] Gérer les paramètres
- [ ] Récupérer les résultats
- [ ] Gérer les exceptions PostgreSQL
- [ ] Intégrer proprement les opérations SQL avancées dans la couche métier

### US-705 — Cas métier du HelpDesk

- [ ] Identifier un cas métier pertinent
- [ ] Définir les règles métier
- [ ] Implémenter la solution PostgreSQL
- [ ] L'intégrer avec Django
- [ ] Garantir l'atomicité de l'opération
- [ ] Ajouter les tests automatisés
- [ ] Documenter les choix techniques

**État :** ⚪ À venir

---

## Sprint 8 — Kubernetes

### US-801 — Découverte de Kubernetes

- [ ] Comprendre les concepts Kubernetes
- [ ] Pods
- [ ] Deployments
- [ ] Services
- [ ] ConfigMaps
- [ ] Secrets

### US-802 — Déploiement de l'application

- [ ] Conteneuriser l'application pour Kubernetes
- [ ] Déployer Django
- [ ] Déployer PostgreSQL
- [ ] Configurer les services
- [ ] Configurer les variables et secrets
- [ ] Health checks

### US-803 — Exposition et scaling

- [ ] Ingress
- [ ] Exposition de l'API
- [ ] Scaling horizontal
- [ ] Gestion des ressources
- [ ] Vérification du déploiement

**État :** ⚪ À venir

---

# État global

| Sprint | État |
|--------|------|
| Sprint 1 — Infrastructure | ✅ Terminé |
| Sprint 2 — Domaine métier | ✅ Terminé |
| Sprint 3 — API REST | ✅ Terminé |
| Sprint 4 — Qualité & tests | ✅ Terminé |
| Sprint 5 — CI/CD & Industrialisation | 🟡 En cours |
| Sprint 6 — Intégration GLPI | ⚪ À venir |
| Sprint 7 — PostgreSQL et SQL avancé | ⚪ À venir |
| Sprint 8 — Kubernetes | ⚪ À venir |

Le projet évolue progressivement : chaque sprint ajoute une nouvelle compétence technique ou une nouvelle dimension d'industrialisation sans anticiper les étapes qui n'ont pas encore été étudiées.

---

# À propos du projet

HelpDesk API est avant tout un projet d'apprentissage orienté vers une pratique professionnelle du développement Backend.

Il permet de travailler progressivement :

- Django ;
- Django REST Framework ;
- conception d'API REST ;
- architecture Backend ;
- authentification et autorisation ;
- règles métier ;
- PostgreSQL ;
- Docker ;
- tests automatisés ;
- qualité et sécurité du code ;
- Git et workflow collaboratif ;
- CI/CD et industrialisation.

Les prochaines étapes du projet portent notamment sur l'intégration GLPI, l'approfondissement de PostgreSQL et SQL avancé, ainsi que Kubernetes.

L'objectif final est de disposer d'une application Backend suffisamment structurée pour servir de support à l'apprentissage et à la préparation à un environnement professionnel.
