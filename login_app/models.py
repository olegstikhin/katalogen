from django.db import models
from django.contrib.auth.models import User
from table_query_app.models import Member

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    member = models.ForeignKey(Member)
