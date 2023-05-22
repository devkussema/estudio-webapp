from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="home"),
    path('sobre', views.sobre, name="sobre"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('blog', views.blog, name="blog"),
    path('contato', views.contato, name="contato"),
]
