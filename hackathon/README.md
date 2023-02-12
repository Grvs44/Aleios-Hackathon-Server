# `hackathon` Django project
## `urls.py`
Contains the root url mapping for the site

## `settings.py`
Contains the global settings for the project
- DEBUG is enabled when the user passes in `-d` when running `/manage.py`
  - When in debug mode (`DEBUG = True`), static files and uploads are served by Django (slow)
  - When in production mode (`DEBUG = False`), it is expected that the web server will statically serve static files and uploads
- CORS is allowed so the React app hosted on a different server is allowed access to this server's resources
  - In real-life production, CORS would be limited to a single domain, or disabled if the React app is served from this server
