from django.contrib import admin
from fetch.models import MasterUser, Sharer, Getter, Connection


class MasterUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('username',)}


admin.site.register(MasterUser)
admin.site.register(Sharer)
admin.site.register(Getter)
admin.site.register(Connection)
