from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class CSVPageView(TemplateView):
    template_name = "csv_home.html"


import csv
from django.http import HttpResponse

# SuperUser username - admin password - admin

# Simple CSV Write Operation
def csv_simple_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'phone_number', 'country'])
    writer.writerow(['Huzaif', 'Sayyed', '+919954465169', 'India'])
    writer.writerow(['Adil', 'Shaikh', '+91545454169', 'India'])
    writer.writerow(['Ahtesham', 'Shah', '+917554554169', 'India'])

    return response


# Writing CSV File From a Dictionary 
def csv_dictionary_write(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_dictionary_write.csv"'

    fieldnames = ['first_name', 'last_name', 'phone_number', 'country']
    writer = csv.DictWriter(response, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name':'Huzaif', 'last_name':'Sayyed', 'phone_number':'+919954465169', 'country':'India'})
    writer.writerow({'first_name':'Adil', 'last_name':'Shaikh', 'phone_number':'+91545454169', 'country':'India'})
    writer.writerow({'first_name':'Ahtesham', 'last_name':'Shah', 'phone_number':'+917554554169', 'country':'India'})

    return response


# Database Data CSV Write Operation
from .models import UserDetail

def csv_database_write(request):

    # Get all data from UserDetail Databse Table
    users = UserDetail.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'phone_number', 'country'])

    for user in users:
        writer.writerow([user.first_name, user.last_name, user.phone_number, user.country])

    return response


# Simple CSV Read Operation
import os

def csv_simple_read(request):

    path = os.path.dirname(__file__)
    file = os.path.join(path, 'csv_readfile.csv')

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # See your console/terminal
        for row in csv_reader:
            if line_count == 0:
                print('\n\nColumn names are {}, {}, {}'.format(row[0], row[1], row[3], row[2]))
                line_count += 1
            else:
                print('\t{} {} lives in {}, and his phone number is {}.'.format(row[0], row[1], row[3], row[2]))
                line_count += 1
        print('Processed {} lines.\n\n'.format(line_count))

        return redirect('/') # Redirect to home
