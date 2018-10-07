from django.urls import re_path

from .views import (
    UserRegistrationPage,
    EncryptedKeyPage
)


urlpatterns = [
    re_path(r'^register$', UserRegistrationPage.as_view()),
    re_path(r'^key$', EncryptedKeyPage.as_view()),
]
