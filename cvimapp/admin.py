import cvimapp.models
from django.contrib import admin

admin.site.register(cvimapp.models.User)
admin.site.register(cvimapp.models.CV)
admin.site.register(cvimapp.models.Section)
admin.site.register(cvimapp.models.Experience)