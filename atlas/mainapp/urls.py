from django.urls import path
from mainapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('info',views.info,name='info'),
    path('info_ai/<int:id>',views.info_ai,name='info_ai'),
    path('archive/<int:id>',views.archive,name='archive')
]