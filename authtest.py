import requests
import base64


def login():
    print('Logging in...')
    request = requests.post(
        'http://localhost:8000/auth/login/',
        auth=('admin', 'admin'),
    )
    print('Authorization header:', request.request.headers['Authorization'])
    print('Encode "admin:admin" in base64:', base64.b64encode(bytes('admin:admin', 'utf-8')).decode())
    response = request.json()
    print(response)
    return response


def logout(logout_url):
    print('\nLogging out...')
    request = requests.post(
        logout_url,
        headers={'Authorization': 'Token ' + response['token']},
    )
    print(request.status_code)


response = login()

logout_choice = input(
    'Logout all tokens (a), just this one (b), or stay logged in (default)? '
).lower()

if logout_choice == 'a':
    logout('http://localhost:8000/auth/logoutall/')
elif logout_choice == 'b':
    logout('http://localhost:8000/auth/logout/')
