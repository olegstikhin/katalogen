from django.shortcuts import render
from django.http import HttpResponse
from table_query_app.models import *
import csv


# Create your views here.
def import_db(request):
    filename = 'alltut.csv'
    reader = csv.reader(open(filename), delimiter=',', quotechar='"')

    for line in reader:
        if line:
            tmp = Member.objects.create()
            tmp.member_type = line[2]
            tmp.given_names = line[9]
            tmp.preferred_name = line[10]
            tmp.surname = line[11]
            tmp.maiden_name = line[12]
            tmp.nickname = line[13]
            #tmp.birthdate = line[14]
            tmp.student_number = line[15]
            tmp.gender = line[16]
            tmp.graduated = line[17]
            tmp.title = line[20]
            tmp.dead = line[23]
            tmp.no_publish = line[25]
            tmp.username = line[26]
            tmp.address = line[36]
            tmp.postcode = line[37]
            tmp.city = line[38]
            tmp.phone = line[40]
            tmp.mobile_phone = line[41]
            tmp.email = line[44]
            tmp.groups = line[45]
            tmp.posts = line[46]
            tmp.membership = line[47]
            tmp.save()

    return HttpResponse("Färdigt")
