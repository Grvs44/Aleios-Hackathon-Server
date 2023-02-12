# Aleios-Hackathon-Server
See the `hackathon` and `sustainabilityapp` folders for documentation
- The Django project is hosted at https://sustainabilityoncampus.eu.pythonanywhere.com/
- The React frontend is hosted at https://alieos.vercel.app/
- The React repository is at https://github.com/Abdul-Asa/Alieos

## Installation
- Configure the virtualenv
  ```cmd
  pip install pipenv
  pipenv --python 3.10
  pipenv install
  ```

- Enter virtualenv
  ```cmd
  pipenv shell
  ```

- Build the database
  ```cmd
  python manage.py migrate
  ```

- Run the server in debug mode (remove the `-d` for production mode - uploads and static won't be served by Django)
  ```cmd
  python manage.py runserver -d
  ```

## API endpoints
Path | Description
-|-
`/` | API root
`/auth/login/` | Login with BasicAuthentication username and password
`/auth/logout/` | Logout this token
`/auth/logoutall/` | Logout all tokens for this user
`/comment/?ordering=<field>&post=<post-id>` | Comment list
`/comment/<id>` | Comment object
`/image/?ordering=<field>` | Image list
`/image/<id>` | Image object
`/tag/?ordering=<field>` | Tag list
`/tag/<id>` | Tag object
`/user/?ordering=<field>` | User list
`/user/<id>` | User object
`/post/?ordering=<field>` | Post list
`/post/<id>` | Post object
