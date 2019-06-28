from django.urls import path

from csv_app import views

urlpatterns = [
    path('', views.CSVPageView.as_view(), name='csv_home_page'),

    # CSv Write URLS
    path('export/csv-simple-write/', views.csv_simple_write, name='csv_simple_write'),
    path('export/csv-dictionary-write/', views.csv_dictionary_write, name='csv_dictionary_write'),
    path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),

    # CSV Read URLS
    path('export/csv-simple-read/', views.csv_simple_read, name='csv_simple_read'),

]