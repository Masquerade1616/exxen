from django.urls import path
from .views import *

#  buraya yazdıgımız her şey movies den sonra gelicek
urlpatterns = [
    path('', index, name='index')
]