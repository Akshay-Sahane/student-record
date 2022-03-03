from re import T
from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('',TemplateView.as_view(template_name="student/index.html"),name="Home"),
    path('addstud/',addstud,name="addstud"),
    path('studlist/',studlist,name="studlist"),
    path('deletestud/<str:SId>',deletestud,name="deletestud"),
    path('updatestud/<str:SId>',editstud,name="editstud"),
    path('studsearch',studsearch),
    path('studsortasc',asc),
    path('studsortdesc',desc),
]