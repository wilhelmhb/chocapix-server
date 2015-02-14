from django.contrib import admin
from django.contrib.auth.models import Group
from bars_core.models.user import User
from bars_core.models.bar import Bar
from bars_core.models.role import Role

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Bar)
admin.site.register(Role)