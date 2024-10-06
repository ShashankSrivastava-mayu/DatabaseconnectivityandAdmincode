from . import views
from django.urls import path


urlpatterns = [
    path("",views.index),
  #  path("<int:id>",views.book_next, name="Book")
  #  now we have declare slug for getting author name in place of number we have to change 
  #  slug in place of id everywhere
    path("<slug:slug>",views.book_next, name="Book")
]
