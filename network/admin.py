from django.contrib import admin
from network.models import Host

class HostAdmin(admin.ModelAdmin):
	list_display = ( 'entry', 'host', 'ip', 'wifi', 'mac', 'enabled' )
	list_filter = ( 'wifi', 'enabled' )
	
admin.site.register(Host, HostAdmin)
