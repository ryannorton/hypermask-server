from django.urls import re_path

from .views import (
    UserRegistrationPage,
)


urlpatterns = [
    re_path(r'^register$', UserRegistrationPage.as_view()),
]
