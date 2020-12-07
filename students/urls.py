from django.urls import path

from students import views
from students.views import index

urlpatterns = [
    path('', views.index)
]
