from django.urls import path
from . import views
urlpatterns = [
    path('profile', views.profile),
    path('new', views.new),
    path('new/create', views.createQuiz),
    path('quizpage/<int:quiz_id>', views.quizpage),
    path('quizpage/<int:quiz_id>/takequiz', views.takeQuiz),
    path('rankings', views.rankings),
]
