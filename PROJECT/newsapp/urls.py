from django.urls import path
from newsapp.views import *

from .views import add_news


urlpatterns = [
    # render html
    path('', index,name='index'),
    path('addnews',add_news,name='addnews'),
    

]