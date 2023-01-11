from django.urls import path
from wsite import views, ajax_views


app_name = 'wsite'

urlpatterns = [
    path('', views.ListWebsiteView.as_view(), name='wsites'),
    path('create-site/', views.CreateWebsiteView.as_view(), name='create-site'),
    path('<str:slug>/', views.RetrieveWebsiteView.as_view(), name='site'),
    path('<str:slug>/add-email/', ajax_views.AddEmailView.as_view(), name='add-email'),
    path('<str:slug>/remove-email/', ajax_views.RemoveEmailView.as_view(), name='remove-email'),
    path('<str:slug>/delete/', views.DeleteWebsiteView.as_view(), name='delete-site'),
]