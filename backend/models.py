from django.db import models

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
