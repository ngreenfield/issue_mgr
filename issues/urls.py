from django.urls import path
from issues import views


urlpatterns = [
    path("", views.BoardView.as_view(), name="board"),
]