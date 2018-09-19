# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GambleBat(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    gb_date = models.CharField(max_length=100, blank=True, null=True)
    gb_round = models.CharField(max_length=100, blank=True, null=True)
    gb_leftright = models.CharField(max_length=100, blank=True, null=True)
    gb_threefour = models.CharField(max_length=100, blank=True, null=True)
    gb_evenodd = models.CharField(max_length=100, blank=True, null=True)
    bat_money = models.IntegerField(blank=True, null=True)
    success = models.CharField(max_length=100, blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamble_bat'


class GambleResult(models.Model):
    gb_date = models.CharField(max_length=100, blank=True, null=True)
    gb_round = models.CharField(max_length=100, blank=True, null=True)
    gb_leftright = models.CharField(max_length=100, blank=True, null=True)
    gb_threefour = models.CharField(max_length=100, blank=True, null=True)
    gb_evenodd = models.CharField(max_length=100, blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamble_result'


class GambleUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    money = models.IntegerField()
    regist_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamble_user'


class WebBoard(models.Model):
    seq = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=50000)
    view = models.IntegerField()
    regist_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    webuser = models.ForeignKey('WebUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_board'


class WebChat(models.Model):
    seq = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    regist_date = models.DateTimeField()
    webuser = models.ForeignKey('WebUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_chat'


class WebProblem(models.Model):
    seq = models.AutoField(primary_key=True)
    problem = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    auth = models.CharField(max_length=50000)
    regist_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_problem'


class WebReply(models.Model):
    seq = models.AutoField(primary_key=True)
    content = models.CharField(max_length=50000)
    regist_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    webuser = models.ForeignKey('WebUser', models.DO_NOTHING)
    board = models.ForeignKey(WebBoard, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_reply'


class WebSolved(models.Model):
    seq = models.AutoField(primary_key=True)
    solved = models.CharField(max_length=100)
    regist_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    webproblem = models.ForeignKey(WebProblem, models.DO_NOTHING)
    webuser = models.ForeignKey('WebUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_solved'


class WebUser(models.Model):
    seq = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ip = models.CharField(max_length=300)
    level = models.IntegerField()
    msg = models.CharField(max_length=300, blank=True, null=True)
    regist_date = models.DateTimeField()
    auth_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_user'
