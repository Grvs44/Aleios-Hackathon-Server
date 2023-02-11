# Aleios-Hackathon-Server
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

- Run the server
  ```cmd
  python manage.py runserver
  ```

## API endpoints
Path | Description
-|-
`/` | API root
`/user/?ordering=<field>` | user list
`/user/<id>` | user object
`/post/?ordering=<field>` | post list
`/post/<id>` | post object
`/image/?ordering=<field>` | image list
`/image/<id>` | image object
`/comment/?ordering=<field>&post=<post-id>` | comment list
`/comment/<id>` | comment object
