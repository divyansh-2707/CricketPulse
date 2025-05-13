from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with the form
    path('result', views.predict_score, name='result'),  # API for predictions
]
