from django.urls import path
from . import views


urlpatterns = [
    path('Dashboard', views.Dashboard_Main_Page, name='dashboard_page'),
    path('api/dashboard',views.Dashboard_API_View.as_view()),
    path('api/list-instrument',views.Instruments_List_API_View.as_view()),
]
