from django.urls import path
from app2 import views
app2_name='app2'
urlpatterns=[
    path('gx/',views.the,name='gx')
]