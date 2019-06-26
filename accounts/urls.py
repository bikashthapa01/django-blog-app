from django.urls import path
from . import views 

urlpatterns = [
	path('',views.index,name='restindex'),
	path('register/',views.RegisterUserView.as_view(),name='register'),
]