from django.urls import path
from .views import TaskCreate, TaskD

urlpatterns = [
    path('task/', TaskCreate.as_view()),
    path('task/<int:id>', TaskD.as_view()),

]
