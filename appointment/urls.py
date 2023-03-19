from django.urls import path
from .views import generate_text_view,me

urlpatterns = [
    path("",me,name=""),
    path('generate_text/', generate_text_view, name='generate_text'),
]