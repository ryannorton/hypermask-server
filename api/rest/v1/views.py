import json

from django.http import JsonResponse
from rest_framework.views import APIView

from user.models import HypermaskUser
from user.exceptions import UserCreationError


class UserRegistrationPage(APIView):
    def post(self, request):
        """
        Example Request:
        {
            "username": "<username>",
            "password_hash": "<password_hash>",
            "encrypted_key": "<encrypted_key>"  // optional
        }

        Example Response (Success):
        {
            "created": true
        }

        Example Response (Failure):
        {
            "created": false,
            "error": "Error message."
        }
        """
        request_json = json.loads(request.body)
        username = request_json.get('username')
        password_hash = request_json.get('password_hash')
        encrypted_key = request_json.get('encrypted_key')

        try:
            HypermaskUser.create(username, password_hash, encrypted_key=encrypted_key)
        except UserCreationError as e:
            return JsonResponse({
                'created': False,
                'error': str(e)
            }, status=400)

        return JsonResponse({
            'created': True
        })
