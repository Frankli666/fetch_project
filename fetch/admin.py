from django.contrib import admin
from fetch.models import MasterUser, Sharer, Getter, Connection

admin.site.register(MasterUser)
admin.site.register(Sharer)
admin.site.register(Getter)
admin.site.register(Connection)
