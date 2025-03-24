from django.urls import path
from companywebsite import views

app_name = 'companywebsite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),  # Add this line for add_page URL mapping

]