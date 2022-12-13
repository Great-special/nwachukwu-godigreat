from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    # path('<str:path>/', views.download_file, name='download_file')
]



