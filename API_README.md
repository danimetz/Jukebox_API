# JukeboxAPI
This Jukebox API implementation is based on using the Spotify API with Spotipy package.

## Functionality
This API comes pre-packaged with the functionality that the MVP will require. The following endpoints are impemented, based off of the MVP requirements of the Capstone Project.

### Tracks

```
GET /callback/
```
Logs in with Spotify OAuth

```
GET /playlists/
```
List all the current users Spotify playlists

```
GET /search?q=<search term>&type=track
```
Search for songs in the Spotify DB

```
GET /playlist?playlist_id=<playlist_id>
```
Show details for a single playlist by `playlist_id`

### Playlist
```
POST /playlist_save?playlistId=<playlist id>
```
Saves current playlist to local DB with playlist ID and generates room code

```
POST /add_track?track_id=<track_id>&room_code=<room_code>
```
Add single track to current selected playlist (room code is required)



