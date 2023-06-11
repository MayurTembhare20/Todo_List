
from django.urls import  path
from todo import views
urlpatterns = [
    path('',views.todo, name='todo'),
    path('update/<id>',views.update, name='update'),
    path('uncross/<id>',views.uncross, name='uncross'),
    path('delete/<id>',views.delete, name='delete'),
   
]