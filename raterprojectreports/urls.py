from django.urls import path
from .views import topfivegames_list

urlpatterns = [
    path('reports/top5games', topfivegames_list),
]
