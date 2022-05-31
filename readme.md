
# Epic Event

Est une API qui aide a géré des événéménts

## Technologies :
- Python
- Django REST
- Django JWT / Simple JWT

* ### Prérequis
	- il faut installer un Shell sur votre ordinateur, sinon vous pouvez utiliser le terminal préinstallé avec votre système d'exploitation:

	- WINDOWS:
		-  touche Windows + R puis tapez 'cmd' puis ENTRER 

	- MAC:
		- Cliquez sur l’icône Launchpad dans le Dock, saisissez Terminal dans le champ de recherche, puis cliquez sur Terminal.
		- Dans le Finder, ouvrez le dossier /Applications/Utilitaires, puis cliquez deux fois sur Terminal.
	 
	- LINUX: 
		- ctrl + alt + t

* ### Démarrage
	- télécharger l'application: https://github.com/oussamaabid82/Epic-Events.
	- Démarrer votre terminal et diriger vous dans le dossier télécharger (projet).

    - Créer un environnement virtuel en tapant dans votre terminal:
        ```bash
        python -m venv venv
        ```

    - Activer l'environnement en tapant dans votre terminal:
        ```bash
        source venv/Scripts/activate
        ```

	- Installez Django et les modules nécessaires pour le bon fonctionnement du programme
		```bash
		pip install -r requirements.txt
		```

	- Créer la migration des models dans la base des données en tapant dans votre terminal:
		```bash
		python manage.py migrate
		```

### 3. Installer PostGreSQL

Téléchargement : 
- [Download PostGreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

-[Comment bien configuré PostGreSQL](https://www.postgresqltutorial.com/postgresql-getting-started/) :

Sous SQL Shell:
- server [localhost] : faire ENTRER
- Database [postgres]: faire ENTRER
- Port [5432] : faire ENTRER
- Username [postgres]: faire ENTRER
- Mot de passe pour l'utilisateur postgres : Entrez le mot de passe que vous avez saisi lors de l'installation
- saisir et valider pour chaque ligne :
```
  - CREATE DATABASE epic_event;
  - CREATE USER epicevent_admin WITH ENCRYPTED PASSWORD 'openclassrooms00';
  - GRANT ALL PRIVILEGES ON DATABASE epic_event TO epicevent_admin;
```
Dans le cas où le nom de la database ou celui de l'utilisateur sont différents de ceux ci-dessus, veillez à modifier les paramètres dans `epicevent/settings.py` dans la variable `DATABASE`.

## **Lancement du projet**

### 1. Lancer le serveur Django sous l'environnement virtuel, dans le terminal:

Se positionner dans l'application LITReview:

`cd epicevent`

Lancer le serveur :
```
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

### 2. Fonctionnalités de l'API:
L'application vous propose les fonctionnalités suivantes :
- Créer des utilisateurs suivant 3 profiles : MANAGER, SALES, SUPPORT
- suivant le profile de l'utilisateur connecté, il pourra :
  - Des clients
  - Des contrats
  - Des évènements
 
 Pour plus de détails :
 [Exigences fonctionnalités](https://s3-eu-west-1.amazonaws.com/course.oc-static.com/projects/Python+FR/P10+-+BDD/CRM+-+Exigences+fonctionnelles.pdf)
 
 ## Postman:
 
    
