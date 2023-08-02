from django.urls import path

from api.views import get_prime_numbers

urlpatterns = [
    path('numbers/get_prime/', get_prime_numbers, name='prime_api'),
]