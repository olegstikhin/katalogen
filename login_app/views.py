from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.template import RequestContext
from django.core.validators import validate_email
from django import forms
import string
import random
import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from login_app.models import *

import table_query_app

def index(request):
    if request.user.is_authenticated():
        member = table_query_app.models.Contactinformationtable.objects.get(email_fld=request.user.username).member_fld
        #profile = UserProfile.objects.filter(user_id=request.user.id).get()
        #member = table_query_app.models.Member.objects.filter(pk=profile.member_id).get()
        name = member.preferredname_fld + " " + member.surname_fld
        return render_to_response("login_app/first_page.html", {'name': name, }, context_instance=RequestContext(request))
    else:
        return render_to_response("login_app/first_page.html", {}, context_instance=RequestContext(request))


def login_attempt(request):
    if request.method == 'POST':
        email = request.POST['main_input']
        try:
            validate_email(email)
        except forms.ValidationError:
            return HttpResponse("<p>Din e-postadress är inte giltig, vänligen försök på nytt</p><p><a href='./'>Tillbaka</a></p>")
        try:
            member = table_query_app.models.Contactinformationtable.objects.get(email_fld=email).member_fld
            pw = id_generator()
            if User.objects.filter(username=email).exists():
                existing_user = get_object_or_404(User, username=email)
                existing_user.set_password(pw)
                existing_user.save()
            else:
                new_user = User.objects.create_user(email, email, pw)
                new_user.save()
            subject, sender, recipient = 'Lösenord till katalogen.fi', 'Katalogen <katalogen@teknologforeningen.fi>', email

            content = "Hej " + member.preferredname_fld + " " + member.surname_fld + ",\nFör att logga in till Katalogen följ länken: http://localhost:8000/auth?email=" + email + "&key=" + pw
            send_mail(subject, content, sender, [email], fail_silently=False)

            return HttpResponse("<p>Hej " + member.preferredname_fld + " " + member.surname_fld + "!<br/>Din registrering har lyckats! Din inloggningslänk skickades till <strong>"+email+"</strong>.</p>")

        except table_query_app.models.Contactinformationtable.DoesNotExist:
            return HttpResponse("<p>Adressen finns inte i medlemsregistret.</p><p><a href='./'>Tillbaka</a></p>")
    return HttpResponse("<p>Fel</p>")

def login_from_link(request):
    if request.method == 'GET':
        email = request.GET['email']
        key = request.GET['key']

        user = authenticate(username=email, password=key)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/medlemmar/')
        else:
            return HttpResponse("<p>Fel inloggningsinformation, vänligen försök på nytt</p>")
    else:
        return HttpResponse("<p>Inte tillgängligt</p>")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/medlemmar/')

# Generates a random activation key consisting of alfabethic lower case characters
def id_generator(size=64, chars=string.ascii_letters+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
