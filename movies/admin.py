from django.contrib import admin
from .models import *
# Register your models here.
#  admin sitemize Movie modelimizi clasımızı eklıyoruz
# model claslarımız buraya eklenıcek

admin.site.register(Movie)
