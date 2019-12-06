# nuitdelinfo2019

## Présentation de notre application

##### A quoi ça sert ?

Notre application Web cherche à offrir les services suivant:

* Stockage centralisé des documents
* Détection des aides auxquels l'étudiant à le droit
* Automatisation de démarches administratives
* Carte indiquant les bons plans culturels et sportifs ainsi que les magasins les moins chers

##### Fonctionnalités implémentées

* API Restful accessible à `/api`
* Page `Mes documents` recensant les documents envoyés par l'utilisateur par catégorie
* Page `Carte` centrée sur l'université
* Page `Mes démarches` permettant de renseigner les informations et d'envoyer les documents manquants pour lancer une démarche automatiquement (ex: demande de bourse crous)

## Développement

### Installation des dépendances

```bash
sudo make install
sudo apt install npm
npm i
make update
```

### Déploiement de l'application

##### Lancer le serveur Django

`make run`

Le serveur se déploit en local sur le port 8000

