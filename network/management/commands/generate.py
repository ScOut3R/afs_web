from django.core.management.base import NoArgsCommand
from network.models import Host
import yaml
from optparse import make_option


class Command(NoArgsCommand):
	help = "Generate network.yml file."

	option_list = NoArgsCommand.option_list + (
											make_option('--config',
													default="/etc/afs/config.yml",
													help='afs main config file'),
											)

	def handle_noargs(self, *args, **kwargs):
		
		configfile = open(kwargs['config'], 'r')
		options = yaml.load(configfile)
		configfile.close()
		
		network = {}
		
		for host in Host.objects.filter(enabled=True):
			network[str(host.entry)] = { 'ip': host.ip, 'mac': str(host.mac), 'host': str(host.host), 'radius': host.wifi }
		
		output = open(options['network'],'w')
		yaml.dump(network, output, default_flow_style=False)
		output.close()
