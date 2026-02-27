from django.urls import path
from .views import home,about


urlpatterns = [
    path('home', home, name='homepage'),
    path('about', about, name='aboutpage')
    
]

