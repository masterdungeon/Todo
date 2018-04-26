from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns=[
    url(r'^$', views.fetch_todo, name = 'fetch_todo'),
    url(r'^add', views.main, name = 'main'),
    # url(r'^delete/[0-9]+/$', views.delete_item, name = 'delete'),
    url(r'^delete/', views.delete, name = 'delete'),
]