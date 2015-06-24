from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.core.validators import validate_email
from django import forms
import string
import random
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from login_app.models import *

import table_query_app

def search(request):
    query = request.GET.get('q', '')
    members = Membertable.objects.filter(name__icontains=query)
    return JsonResponse("search.html", {'query': query, 'members': members, }, context_instance=RequestContext(request))


def get_members(request):
    if request.user.is_authenticated():
        member = table_query_app.models.Contactinformationtable.objects.get(email_fld=request.user.username).member_fld
        #profile = UserProfile.objects.filter(user_id=request.user.id).get()
        #member = table_query_app.models.Membertable.objects.filter(pk=profile.member_id).get()
        name = member.preferredname_fld + " " + member.surname_fld
        # ordinarie = table_query_app.models.Membertable.objects.order_by('surname_fld')
        ordinarie_id = table_query_app.models.Membershiptable.objects.filter(membershiptype_fld="00000000000000000000000000000002").filter(endtime_fld__isnull=True).values_list('member_fld', flat=True)
        ordinarie = table_query_app.models.Contactinformationtable.objects.filter(member_fld__in=ordinarie_id).select_related().order_by('member_fld__surname_fld')
        stalmar_id = table_query_app.models.Membershiptable.objects.filter(membershiptype_fld="00000000000000000000000000000005").values_list('member_fld', flat=True)
        stalmar = table_query_app.models.Contactinformationtable.objects.filter(member_fld__in=stalmar_id).select_related().order_by('member_fld__surname_fld')
        return render_to_response("homeview.html", {'name': name, 'ordinarie': ordinarie, 'stalmar': stalmar, }, context_instance=RequestContext(request))
    else:
        return render_to_response("homeview.html", {}, context_instance=RequestContext(request))
