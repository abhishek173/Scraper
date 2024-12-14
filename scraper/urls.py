from django.contrib import admin
from django.urls import path
from home.views import * 

urlpatterns = [
    path('',index),
    path('run_scraper/',run_scraper),
    path('admin/', admin.site.urls),

]
