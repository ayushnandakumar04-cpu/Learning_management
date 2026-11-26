from django.urls import path
from module_manage.views import ModuleCreateView
urlpatterns=[
    path('<int:pk>/course/',ModuleCreateView.as_view()),

]