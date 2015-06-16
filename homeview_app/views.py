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
    members = Member.objects.filter(name__icontains=query)
    return JsonResponse("search.html", {'query': query, 'members': members, }, context_instance=RequestContext(request))


def get_members(request):
    if request.user.is_authenticated():
        profile = UserProfile.objects.filter(user_id=request.user.id).get()
        member = table_query_app.models.Member.objects.filter(pk=profile.member_id).get()
        name = member.preferred_name + " " + member.surname
        ordinarie = table_query_app.models.Member.objects.filter(member_type__contains='Ordinarie medlem').order_by('surname')
        stalmar = table_query_app.models.Member.objects.filter(member_type__contains='StÄlM').exclude(member_type__contains='JuniorStÄlM').order_by('surname')
        return render_to_response("homeview.html", {'name': name, 'ordinarie': ordinarie, 'stalmar': stalmar, }, context_instance=RequestContext(request))
    else:
        return render_to_response("homeview.html", {}, context_instance=RequestContext(request))
