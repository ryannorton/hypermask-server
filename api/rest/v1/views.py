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

        if not username:
            return JsonResponse({
                'error': 'Missing username in POST body.'
            }, status=400)

        if not password_hash:
            return JsonResponse({
                'error': 'Missing password_hash in POST body.'
            }, status=400)

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


class EncryptedKeyPage(APIView):
    def get(self, request):
        """
        Get a user's encrypted key.

        Query Parameters: username, password_hash

        Example Response (Success):
        {
            "encrypted_key": "<encrypted_key>"
        }

        Example Response (Failure):
        {
            "error": "Error message."
        }
        """
        username = request.GET.get('username')
        password_hash = request.GET.get('password_hash')

        if not username:
            return JsonResponse({
                'error': 'Missing username query parameter.'
            }, status=400)

        if not password_hash:
            return JsonResponse({
                'error': 'Missing password_hash query parameter.'
            }, status=400)

        try:
            user = HypermaskUser.objects.get(username=username)
        except HypermaskUser.DoesNotExist:
            return JsonResponse({
                'error': 'User does not exist.'
            }, status=404)

        if not user.check_password(password_hash):
            return JsonResponse({
                'error': 'Invalid password.'
            }, status=400)

        return JsonResponse({
            'encrypted_key': user.encrypted_key
        })

    def post(self, request):
        """
        Update a user's encrypted key.

        Query Parameters: username, password_hash, encrypted_key

        Example Response (Success):
        {
            "success": true
        }

        Example Response (Failure):
        {
            "success": false,
            "error": "Error message."
        }
        """
        username = request.GET.get('username')
        password_hash = request.GET.get('password_hash')
        encrypted_key = request.GET.get('encrypted_key')

        if not username:
            return JsonResponse({
                'error': 'Missing username query parameter.'
            }, status=400)

        if not password_hash:
            return JsonResponse({
                'error': 'Missing password_hash query parameter.'
            }, status=400)

        if not encrypted_key:
            return JsonResponse({
                'error': 'Missing encrypted_key query parameter.'
            }, status=400)

        try:
            user = HypermaskUser.objects.get(username=username)
        except HypermaskUser.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'User does not exist.'
            }, status=404)

        if not user.check_password(password_hash):
            return JsonResponse({
                'success': False,
                'error': 'Invalid password.'
            }, status=400)

        if not encrypted_key:
            return JsonResponse({
                'success': False,
                'error': 'No encrypted key provided.'
            }, status=400)

        user.set_encrypted_key(encrypted_key)

        return JsonResponse({
            'success': True
        })
