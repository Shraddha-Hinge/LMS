from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

GOOGLE_CLIENT_ID = "your-google-client-id"

def google_authenticate(id_token_str):
    try:
        payload = id_token.verify_oauth2_token(id_token_str, requests.Request(), GOOGLE_CLIENT_ID)
        email = payload.get('email')
        name = payload.get('name')

        user, created = User.objects.get_or_create(email=email, defaults={'username': name, 'role': 'student'})
        return user
    except:
        raise AuthenticationFailed("Invalid Google Token")
