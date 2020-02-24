from django.urls import path
from . import views
urlpatterns = [
    path('profile', views.profile),
    path('quiz', views.quiz),
    path('rankings', views.rankings),
    path('create', views.create)
]
