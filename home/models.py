# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vouchers(models.Model):

    #__Vouchers_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)
    kategori = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Vouchers_FIELDS__END

    class Meta:
        verbose_name        = _("Vouchers")
        verbose_name_plural = _("Vouchers")


class Users(models.Model):

    #__Users_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    nama = models.CharField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Voucher_Claims(models.Model):

    #__Voucher_Claims_FIELDS__

    #__Voucher_Claims_FIELDS__END

    class Meta:
        verbose_name        = _("Voucher_Claims")
        verbose_name_plural = _("Voucher_Claims")



#__MODELS__END
