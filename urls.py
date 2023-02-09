from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('videos', views.videos, name='videos'),
    path('images/<str:eventName>', views.images, name='images'),
    path('preview/<str:fileName>', views.preview, name='preview'),
    path('images/download/', views.download, name='download')
    # path('loadmore/<int:id>', views.loadmore, name = 'loadmore'),
    #path('load_page/<int:id>', views.loadmore, name = 'load_page'),
]