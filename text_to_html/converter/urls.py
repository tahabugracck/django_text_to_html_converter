from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_text_to_html, name='convert_text_to_html'),
]
