from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from table_query_app.models import *
from django.template import RequestContext

import csv


# Create your views here.
#def import_db(request):
#    return HttpResponse("Färdigt")

def get_member_info(request):
    if request.user.is_authenticated():
        member = Contactinformationtable.objects.get(pk=request.GET['id'])
        name = member.member_fld.preferredname_fld + " " + member.member_fld.surname_fld
        address = member.streetaddress_fld + ", " + member.postalcode_fld + " " + member.city_fld
        cellphone = member.cellphone_fld
        phone = member.phone_fld
        email = member.email_fld
        return render_to_response("memberinfo.html", {'name': name, 'address': address, 'cellphone': cellphone, 'phone': phone, 'email': email, }, context_instance=RequestContext(request))
    else:
        return render_to_response("memberinfo.html", {}, context_instance=RequestContext(request))

def get_member_name(request):
    if request.user.is_authenticated():
        member = Contactinformationtable.objects.get(pk=request.GET['id'])
        name = member.member_fld.preferredname_fld + " " + member.member_fld.surname_fld
        return HttpResponse("<a href='#'>" + name + "</a>")
    else:
        return HttpResponse("<a href='#'>" + "</a>")
