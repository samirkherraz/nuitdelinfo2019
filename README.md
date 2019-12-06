# nuitdelinfo2019

## Présentation de notre application

##### A quoi ça sert ?

Notre application Web cherche à offrir les services suivant:

* Stockage centralisé des documents
* Détection des aides auxquels l'étudiant a le droit
* Automatisation des démarches administratives
* Carte indiquant les bons plans culturels et sportifs ainsi que les magasins les moins chers (classifiés par couleurs/catégories)

##### Fonctionnalités implémentées

* API Restful accessible à `/api`
* Page `Mes documents` recensant les documents envoyés par l'utilisateur par catégorie
* Page `Carte` centrée sur l'université
* Page `Mes démarches` permettant de renseigner les informations et d'envoyer les documents manquants pour lancer une démarche automatiquement (ex: demande de bourse crous)
* ChatBot répondant "Bonjour" lorsque l'on entame la conversation et comprend lorsque l'on cherche à contacter la caf et permet de se faire rickroller (en tapant un message contenant rickroll)

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

##### Image docker

Notre image docker est disponible à l'adresse suivante : https://hub.docker.com/r/samirkherraz/nuitinfo2019
