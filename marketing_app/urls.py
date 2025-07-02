from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('campaign/create/', views.campaign_create, name='campaign_create'),
    path('leads/<int:campaign_id>/', views.lead_list, name='lead_list'),
    path('leads/create/<int:campaign_id>/', views.lead_create, name='lead_create'),
]
