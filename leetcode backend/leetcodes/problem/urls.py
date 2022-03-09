from django.urls import path
from problem import views


urlpatterns = [




    path('',views.problemGetOrCreate.as_view()),
    path('<int:id>/',views.problemDetailsGetPutDelete.as_view()),



]