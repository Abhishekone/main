from django.urls import path
from app import views
app_name='app'
urlpatterns=[
    path('lx/',views.zero,name='lx')
]