# README - Projet Mercadona - PromoWeb

Ce projet concerne la création d'une application web pour Mercadona, une entreprise du secteur du retail, désireuse de remplacer ses tracts publicitaires par une plateforme numérique pour afficher et gérer ses promotions. PromoWeb, en charge du développement, travaillera en trois parties distinctes : Front-end, Back-end et Base de données.

## Objectifs

L'application doit permettre aux administrateurs de gérer les promotions via une interface sécurisée, en créant et en affichant des produits avec des offres promotionnelles. Pour les utilisateurs, tous les produits (même sans promotion) sont visibles dans le catalogue avec des filtres par catégorie. 

## Technologies utilisées

- **Front-end :** Utilisation de HTML/CSS pour les templates 
- **Back-end :** Utilisation de Python avec Django, PostgreSQL pour la base de données.
- **Déploiement :** Heroku

## Mise en œuvre sur votre machine (avec Django)

1. **Clonage du projet :**

```bash
git clone https://github.com/noraikem/mercadona.git
````

2. **Installation des dépendances :**
```bash
cd mercadona
pip install -r requirements.txt
````

3. **Configuration du .env :**

Créez un fichier .env à la racine du projet.
Ajoutez les configurations sensibles :
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
````

4. **Lancer le serveur Django :**
```bash
python manage.py runserver
````

5.**Accéder à l'application :**
Ouvrez votre navigateur web et accédez à l'URL : http://localhost:8000/

---

### Liens Utiles
- **Dépôt Git :** [GIT Mercadona](https://github.com/noraikem/mercadona)
- **Application déployée :** [Application Mercadona](https://mercadona-projet-c09f88ec7478.herokuapp.com)
- **Outil de gestion de projet utilisé :** [Trello Projet Mercadona](https://trello.com/invite/b/UHA3gN3B/ATTI23bfc0b4ea68d3acb23490657e143b3d8FFACD1B/mercadona)

---

