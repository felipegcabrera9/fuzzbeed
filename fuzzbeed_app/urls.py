from django.urls import path
from . import views
urlpatterns = [
    path('profile', views.profile),
    path('new', views.new),
    path('new/create', views.createQuiz),
    path('quiz', views.quiz),
    path('rankings', views.rankings),
]
