from django.urls import path
from issues import views


urlpatterns = [
    path("", views.BoardView.as_view(), name="board"),
    path("<int:pk>/issues/edit/", views.IssueUpdateView.as_view(), name ="edit"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/issues/delete", views.IssueDeleteView.as_view(), name="delete"),
    path('detail/', views.DetailView.as_view(), name='detail'),
]