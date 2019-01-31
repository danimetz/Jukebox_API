# Jukebox_API

## JUKEBOX - API
This project is the django backend that utilizes the spotify API to help user collaborate on a single spotify playlist.

## Motivation

Have you ever had a song request that you want your friends to play but couldn't do it because the phone connected to the speaker was locked? Or maybe you needed to download an application, well with Jukebox you can collaborate on a single spotify playlist to queue up the next song!

This is a Capstone project for [Ada Developers Academy](https://www.adadevelopersacademy.org/).
 
## Tech/framework used
<b>Built with</b>
- [React](https://reactjs.org/) (This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).)
- [Django/Python](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Features
By having one user login they can share a room-code with friends to enter on the same url and they will be able to contribute to a single playlist

## Installation
To download and edit this project:

1. Clone this repository:
```
git clone https://github.com/danimetz/Jukebox_API.git
```
2. In the "project" directory, install all the required packages run the following command in the command line:
```
python requirements.txt
```
3. Create a Spotify Developers Account, go to [https://developer.spotify.com](Spotify Developers) webpage and login with your Spotify account. A new app will need to be created so that you can setup your own SPOTIFY SECRET and SPOTIFY CLIENT ID. Make sure to set up the Spotify callback to match the appropriate url, if you are running it with the react application locally it will be [http://loacalhost:3000/callback/] or the Django application will be [http://loacalhost:8000/callback/] if running locally. (Note: DO NOT FORGET THE ‘/‘ AT THE END OF THE CALLBACK URL)

4. Next you will need to set up a local database using PostgreSQL. To do this locally you can run the commands
‘’’
brew install postgresql
createdb database_name
psql database_name
‘’’

  * Remember the DB name, user, password, host and port (usually ‘5432’) because those will need to be updated in the .env.

5. Create a file named <b>.env</b> in the main project directory with the following information:
```
DEBUG=True // or False
SECRET_KEY=<YOUR-DJANGO-SECRET-KEY>
SPOTIPY_CLIENT_ID=<YOUR-SPOTIFY-CLIENT-ID>
SPOTIPY_CLIENT_SECRET=<YOUR-SPOTIFY-CLIENT-SECRET>
SPOTIPY_REDIRECT_URI=<YOUR-SPOTIFY-URL-CALLBACK>
DB_NAME=‘<YOUR-DB-NAME>’
DB_USER=‘<YOUR-DB-USER>’
DB_PASSWORD=‘<YOUR-DB-PASSWORD>’
DB_HOST=‘<YOUR-DB-HOST>’
DB_PORT=‘<YOUR-DB-PORT>’
```
6. Then run the migrations by running the command:
```
python manage.py migrate
```

7. Now everything should be set up to run:

```
python manage.py runserver
```

And go to: [http://loacalhost:8000/](http://loacalhost:8000/)

## How to use?
* See API calls here

