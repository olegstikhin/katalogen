#from django.db import models

# Create your models here.
#class Member(models.Model):
#    member_type = models.CharField(max_length=200)
#    given_names = models.CharField(max_length=200)
#    preferred_name = models.CharField(max_length=200)
#    surname = models.CharField(max_length=200)
#    maiden_name = models.CharField(max_length=200)
#    nickname = models.CharField(max_length=200)
#    birthdate = models.DateTimeField(null=True)
#    student_number = models.CharField(max_length=10)
#    gender = models.CharField(max_length=10)
#    graduated = models.CharField(max_length=10)
#    title = models.CharField(max_length=200)
#    dead = models.CharField(max_length=10)
#    no_publish = models.CharField(max_length=10)
#    username = models.CharField(max_length=10)
#    address = models.CharField(max_length=500)
#    postcode = models.CharField(max_length=100)
#    city = models.CharField(max_length=500)
#    phone = models.CharField(max_length=100)
#    mobile_phone = models.CharField(max_length=100)
#    groups = models.TextField()
#    posts = models.TextField()
#    membership = models.TextField()
#    email = models.EmailField()
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Awardreceptiontable(models.Model):
    award_fld = models.ForeignKey('Awardtable', db_column='award_fld', blank=True, null=True)
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    received_fld = models.DateTimeField(blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'AwardReceptionTable'


class Awardtable(models.Model):
    awardtype_fld = models.ForeignKey('Awardtypetable', db_column='awardType_fld', blank=True, null=True)  # Field name made lowercase.
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=60, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    abbreviation_fld = models.CharField(max_length=10, blank=True, null=True)
    photo_fld = models.TextField(blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'AwardTable'


class Awardtypetable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=30, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'AwardTypeTable'


class Contactinformationtable(models.Model):
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    location_fld = models.CharField(max_length=20, blank=True, null=True)
    streetaddress_fld = models.CharField(db_column='streetAddress_fld', max_length=60, blank=True, null=True)  # Field name made lowercase.
    postalcode_fld = models.CharField(db_column='postalCode_fld', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city_fld = models.CharField(max_length=30, blank=True, null=True)
    country_fld = models.CharField(max_length=30, blank=True, null=True)
    phone_fld = models.CharField(max_length=30, blank=True, null=True)
    cellphone_fld = models.CharField(db_column='cellPhone_fld', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax_fld = models.CharField(max_length=30, blank=True, null=True)
    url_fld = models.CharField(max_length=60, blank=True, null=True)
    email_fld = models.CharField(max_length=50, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'ContactInformationTable'


class Departmentmembershiptable(models.Model):
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    department_fld = models.ForeignKey('Departmenttable', db_column='department_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    studytype_fld = models.CharField(db_column='studyType_fld', max_length=40, blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'DepartmentMembershipTable'


class Departmenttable(models.Model):
    departmenttype_fld = models.ForeignKey('Departmenttypetable', db_column='departmentType_fld', blank=True, null=True)  # Field name made lowercase.
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=60, blank=True, null=True)
    abbreviation_fld = models.CharField(max_length=10, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'DepartmentTable'


class Departmenttypetable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=30, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'DepartmentTypeTable'


class Groupmembershiptable(models.Model):
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    post_fld = models.ForeignKey('Posttable', db_column='post_fld', blank=True, null=True)
    group_fld = models.ForeignKey('Grouptable', db_column='group_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'GroupMembershipTable'


class Grouptable(models.Model):
    grouptype_fld = models.ForeignKey('Grouptypetable', db_column='groupType_fld', blank=True, null=True)  # Field name made lowercase.
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=40, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    abbreviation_fld = models.CharField(max_length=10, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'GroupTable'


class Grouptypetable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=40, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'GroupTypeTable'


class Membertable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    givennames_fld = models.CharField(db_column='givenNames_fld', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preferredname_fld = models.CharField(db_column='preferredName_fld', max_length=30, blank=True, null=True)  # Field name made lowercase.
    surname_fld = models.CharField(db_column='surName_fld', max_length=40, blank=True, null=True)  # Field name made lowercase.
    maidenname_fld = models.CharField(db_column='maidenName_fld', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nickname_fld = models.CharField(db_column='nickName_fld', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate_fld = models.DateTimeField(db_column='birthDate_fld', blank=True, null=True)  # Field name made lowercase.
    studentid_fld = models.CharField(db_column='studentId_fld', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender_fld = models.IntegerField(blank=True, null=True)
    graduated_fld = models.IntegerField(blank=True, null=True)
    occupation_fld = models.CharField(max_length=30, blank=True, null=True)
    photo_fld = models.TextField(blank=True, null=True)
    title_fld = models.CharField(max_length=30, blank=True, null=True)
    nationality_fld = models.CharField(max_length=3, blank=True, null=True)
    primarycontactid_fld = models.CharField(db_column='primaryContactId_fld', max_length=33, blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.
    dead_fld = models.IntegerField(blank=True, null=True)
    subscribedtomodulen_fld = models.IntegerField(blank=True, null=True)
    lastsync_fld = models.DateTimeField(blank=True, null=True)
    username_fld = models.CharField(unique=True, max_length=150, blank=True, null=True)
    nopublishcontactinfo = models.IntegerField()
    nopublishcontactinfo_fld = models.IntegerField(db_column='noPublishContactInfo_fld')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'MemberTable'


class Membershiptable(models.Model):
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    membershiptype_fld = models.ForeignKey('Membershiptypetable', db_column='membershipType_fld', blank=True, null=True)  # Field name made lowercase.
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'MembershipTable'


class Membershiptypetable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=30, blank=True, null=True)
    abbreviation_fld = models.CharField(max_length=10, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'MembershipTypeTable'


class Postmembershiptable(models.Model):
    post_fld = models.ForeignKey('Posttable', db_column='post_fld', blank=True, null=True)
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'PostMembershipTable'


class Posttable(models.Model):
    posttype_fld = models.ForeignKey('Posttypetable', db_column='postType_fld', blank=True, null=True)  # Field name made lowercase.
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=30, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    abbreviation_fld = models.CharField(max_length=10, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'PostTable'


class Posttypetable(models.Model):
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    name_fld = models.CharField(max_length=30, blank=True, null=True)
    description_fld = models.CharField(max_length=255, blank=True, null=True)
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'PostTypeTable'


class Presencetable(models.Model):
    member_fld = models.ForeignKey('Membertable', db_column='member_fld', blank=True, null=True)
    created_fld = models.DateTimeField(blank=True, null=True)
    createdby_fld = models.CharField(db_column='createdBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    modified_fld = models.DateTimeField(blank=True, null=True)
    modifiedby_fld = models.CharField(db_column='modifiedBy_fld', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime_fld = models.DateTimeField(db_column='startTime_fld', blank=True, null=True)  # Field name made lowercase.
    endtime_fld = models.DateTimeField(db_column='endTime_fld', blank=True, null=True)  # Field name made lowercase.
    eventstatus_fld = models.IntegerField(db_column='eventStatus_fld', blank=True, null=True)  # Field name made lowercase.
    eventtype_fld = models.IntegerField(db_column='eventType_fld', blank=True, null=True)  # Field name made lowercase.
    attf_fld = models.IntegerField(db_column='atTF_fld', blank=True, null=True)  # Field name made lowercase.
    attky_fld = models.IntegerField(db_column='atTKY_fld', blank=True, null=True)  # Field name made lowercase.
    athut_fld = models.IntegerField(db_column='atHUT_fld', blank=True, null=True)  # Field name made lowercase.
    notes_fld = models.CharField(max_length=255, blank=True, null=True)
    objectid = models.CharField(db_column='objectId', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'PresenceTable'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        #managed = False
        db_table = 'django_migrations'


class JosComprofiler(models.Model):
    user_id = models.AutoField(primary_key=True)
    lastupdatedate = models.DateTimeField(blank=True, null=True)
    cb_streetaddress = models.CharField(max_length=255, blank=True, null=True)
    cb_postalcode = models.CharField(max_length=255, blank=True, null=True)
    cb_city = models.CharField(max_length=255, blank=True, null=True)
    cb_country = models.CharField(max_length=255, blank=True, null=True)
    cb_phone = models.CharField(max_length=255, blank=True, null=True)
    cb_subscribedtomodulen = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'jos_comprofiler'


class JosComprofilerFields(models.Model):
    fieldid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'jos_comprofiler_fields'


class JosComprofilerPrivacy(models.Model):
    userid = models.ForeignKey('JosComprofiler', db_column='userid')
    type = models.CharField(max_length=8, blank=True, null=True)
    xid = models.ForeignKey('JosComprofilerFields', db_column='xid')
    rule = models.IntegerField(blank=True, null=True)
    params = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'jos_comprofiler_privacy'
        unique_together = (('userid', 'xid'),)


class JosUsers(models.Model):
    id = models.ForeignKey('JosComprofiler', db_column='id', primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'jos_users'


class MembersSequence(models.Model):
    next = models.DecimalField(max_digits=19, decimal_places=0)
    objectname = models.CharField(primary_key=True, max_length=64)

    class Meta:
        #managed = False
        db_table = 'members_sequence'
