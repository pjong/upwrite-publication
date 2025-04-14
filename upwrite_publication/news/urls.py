from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Home
    path('regional/', views.section_view, {'section': 'regional'}, name='regional'),
    path('national/', views.section_view, {'section': 'national'}, name='national'),
    path('editorial/', views.section_view, {'section': 'editorial'}, name='editorial'),
    path('provincial/', views.section_view, {'section': 'provincial'}, name='provincial'),
    path('legal/', views.section_view, {'section': 'legal'}, name='legal'),
    path('section/<str:section>/', views.section_view, name='section'),  # THIS IS NEEDED
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]
