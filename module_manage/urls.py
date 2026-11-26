from django.urls import path
from module_manage.views import ModuleCreateView,ModuleRetriveUpdateDeleteView
urlpatterns=[
    path('<int:pk>/course/',ModuleCreateView.as_view()),
    path('course/<int:pk>',ModuleRetriveUpdateDeleteView.as_view())

]