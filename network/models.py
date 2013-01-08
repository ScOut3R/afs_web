from django.db import models
from django.forms import fields
from django.utils.translation import ugettext as _
import re
from south.modelsinspector import add_introspection_rules

MAC_RE = r'^([0-9a-fA-F]{2}([:-]?|$)){6}$'
mac_re = re.compile(MAC_RE)

add_introspection_rules([], ["^network\.models\.MACAddressField"])

class MACAddressFormField(fields.RegexField):
	default_error_messages = {
		'invalid': _(u'Enter a valid MAC address.'),
	}

	def __init__(self, *args, **kwargs):
		super(MACAddressFormField, self).__init__(mac_re, *args, **kwargs)

class MACAddressField(models.Field):
	empty_strings_allowed = False
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 17
		super(MACAddressField, self).__init__(*args, **kwargs)

	def get_internal_type(self):
		return "CharField"

	def formfield(self, **kwargs):
		defaults = {'form_class': MACAddressFormField}
		defaults.update(kwargs)
		return super(MACAddressField, self).formfield(**defaults)

class Host(models.Model):
	entry = models.CharField(max_length=64, unique=True)
	host = models.CharField(max_length=64)
	ip = models.IPAddressField(verbose_name=("IP"))
	mac = MACAddressField(unique=True, verbose_name=("MAC"))
	wifi = models.BooleanField(default=False, verbose_name=("WiFi"))
	enabled = models.BooleanField(default=True)
	last_seen = models.DateTimeField(blank=True, null=True, editable=False)

	def __unicode__(self):
		return self.entry

POLICIES = (
	('A', 'ACCEPT'),
	('R', 'REJECT'),
	('D', 'DROP'),
)

class Group(models.Model):
	name = models.CharField(max_length=64, unique=True)
	policy = models.CharField(max_length=1, choices=POLICIES)
	hosts = models.ManyToManyField(Host, related_name='grouphosts')
	enabled = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name
