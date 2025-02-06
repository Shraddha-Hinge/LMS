from django.urls import path
from .views import Add_StudentView,Add_StaffView

urlpatterns = [
	path('Addstudent/', Add_StudentView.as_view()),
	path('Addstaff/', Add_StaffView.as_view()),

]
