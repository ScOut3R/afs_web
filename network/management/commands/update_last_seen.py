from django.core.management.base import NoArgsCommand
import subprocess
from network.models import Host
import datetime


class Command(NoArgsCommand):
	help = "Updates last seen field of hosts."
	
	def handle_noargs(self, *args, **kwargs):
		
		command = subprocess.Popen(["arp -n -i eth0 | tail -n +2 | awk '{ print $3 }'"], shell=True, stdout=subprocess.PIPE)
		
		for mac in command.stdout.readlines():
			if Host.objects.filter(mac=mac.rstrip('\n')):
				host = Host.objects.get(mac=mac.rstrip('\n'))
				host.last_seen = datetime.datetime.now()
				host.save()
