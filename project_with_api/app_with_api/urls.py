from django.urls import path

from app_with_api.views import AdCreateView, AdListView, AdView

app_name = 'ads'

urlpatterns = [
    path('create/', AdCreateView.as_view()),
    path('', AdListView.as_view()),
    path('<int:pk>/', AdView.as_view()),
]
