from django.urls import path
from . import views

app_name = 'locacoes'

urlpatterns = [
    path('', views.LocacaoListView.as_view(), name='lista'),
    path('nova/', views.LocacaoCreateView.as_view(), name='nova'),
]
