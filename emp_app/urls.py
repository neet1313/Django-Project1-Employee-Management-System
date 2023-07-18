from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('allEmp', views.allEmp, name='allEmp'),
    path('addEmp', views.addEmp, name='addEmp'),
    path('removeEmp', views.removeEmp, name='removeEmp'),
    path('filterEmp', views.filterEmp, name='filterEmp')
]
