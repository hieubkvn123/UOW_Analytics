from django.urls import path
from . import views

urlpatterns = [
    path('nlp_text_summarization', views.nlp_text_summarization, name = 'nlp_text_summarization'),
]
