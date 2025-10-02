
from django.urls import path
from .views import home, about ,posts , post_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/' , about , name='about'),
    path('blog/' , posts , name='blog'),
    path('blog/<int:id>/', post_detail, name='post_detail'),
]

