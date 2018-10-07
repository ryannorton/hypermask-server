from django.http import JsonResponse

from rest_framework.views import APIView


class UserRegistrationPage(APIView):
    def get(self, request):
        return JsonResponse({
            'success': True
        })
