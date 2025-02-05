from django.urls import path
from . import views as codhr_views


urlpatterns = [
    path('corpus/<str:corpus_id>/codhr-report/', codhr_views.report),
]