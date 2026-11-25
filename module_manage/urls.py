from django.urls import path
from module_manage.views import ModuleCreateView
urlpatterns=[
    path('course/<int:pk>/create/',ModuleCreateView.as_view()),

]