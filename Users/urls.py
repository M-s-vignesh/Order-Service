from django.urls import path
from .login import LogInAPIView


urlpatterns = [
    path('login/', LogInAPIView.as_view(),
         name='login')
]
