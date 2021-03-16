from .views import RegistrationForm
from django.urls import path

urlpatterns = [
    path('signup/', RegistrationForm.as_view(), name='signup')
]
