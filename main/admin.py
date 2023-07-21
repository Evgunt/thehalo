from django.contrib import admin

from django.contrib.auth.models import Group

from . import models
admin.site.unregister(Group)

admin.site.register(models.Size)
admin.site.register(models.About)
admin.site.register(models.Slider)
admin.site.register(models.Sertificate)
