from django.contrib import admin
from.models import registration
from.models import login
from.models import woregi
from.models import entry
from.models import chosse
from.models import booking
from .models import ufeed
# Register your models here.
admin.site.register(registration)
admin.site.register(login)
admin.site.register(woregi)
admin.site.register(entry)
admin.site.register(chosse)
admin.site.register(booking)
admin.site.register(ufeed)