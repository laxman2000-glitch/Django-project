
from django.urls import path
from.import views


urlpatterns = [
    path('contactin/', views.contact_page, name= 'contact_page'),
    path('search/', views.search_page, name = 'search_bar'),
    path('register/',views.register_page, name= 'register_user'),
]
