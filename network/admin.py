from django.contrib import admin
from network.models import Host
from django.utils.translation import ugettext as _

class HostAdmin(admin.ModelAdmin):
	list_display = ( 'entry', 'host', 'ip', 'mac', 'wifi', 'enabled' )
	list_filter = ( 'wifi', 'enabled' )
	ordering = ( 'entry', )
	actions = [ 'set_enabled', 'unset_enabled', 'set_wifi', 'unset_wifi' ]
	search_fields = [ 'entry', 'host', 'ip', 'mac' ]
	
	def set_enabled(self, request, queryset):
		rows_updated = queryset.update(enabled=True)
		if rows_updated == 1:
			message_bit = _("1 host was")
		else:
			message_bit = _("%s hosts were") % rows_updated
		self.message_user(request, "%s enabled" % message_bit)
	set_enabled.short_description = _("Enable host")
	
	def unset_enabled(self, request, queryset):
		rows_updated = queryset.update(enabled=False)
		if rows_updated == 1:
			message_bit = _("1 host was")
		else:
			message_bit = _("%s hosts were") % rows_updated
		self.message_user(request, "%s disabled" % message_bit)
	unset_enabled.short_description = _("Disable host")
	
	def set_wifi(self, request, queryset):
		rows_updated = queryset.update(wifi=True)
		if rows_updated == 1:
			message_bit = _("1 host was")
		else:
			message_bit = _("%s hosts were") % rows_updated
		self.message_user(request, "%s modified" % message_bit)
	set_wifi.short_description = _("Enable WiFi")
	
	def unset_wifi(self, request, queryset):
		rows_updated = queryset.update(wifi=False)
		if rows_updated == 1:
			message_bit = _("1 host was")
		else:
			message_bit = _("%s hosts were") % rows_updated
		self.message_user(request, "%s modified" % message_bit)
	unset_wifi.short_description = _("Disable WiFi")
	
admin.site.register(Host, HostAdmin)
