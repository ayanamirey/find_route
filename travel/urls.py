from django.contrib import admin
from django.urls import path, include
from routes.views import home, find_routes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find_routes/', find_routes, name='find_routes'),
    path('', home, name='home'),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),

]
