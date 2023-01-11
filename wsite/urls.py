from django.urls import path
from wsite import views


app_name = 'wsite'

urlpatterns = [
    path('', views.ListWebsiteView.as_view(), name='wsites'),
    path('create-site/', views.CreateWebsiteView.as_view(), name='create-site'),
    path('<slug:str>/', views.RetrieveWebsiteView.as_view(), name='site'),
    path('<slug:str>/delete/', views.DeleteWebsiteView.as_view(), name='delete-site'),
    path('<slug:str>/view/', views.DeleteWebsiteView.as_view(), name='delete-site'),
    path("<slug:str>/profile/", views.DetailWebsiteView.as_view(), name='websites'),
]