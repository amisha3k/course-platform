
from django.urls import path,include
from . import views

urlpatterns = [
    path("<slug:course_id>/lessons/<slug:lesson_id>/",views.lesson_detail_view),
    path("<slug:course_id>/",views.course_detail_view,),
    path("",views.course_list_view),     # Root path for /courses/
   
]