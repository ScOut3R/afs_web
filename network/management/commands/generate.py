from django.core.management.base import NoArgsCommand
from network.models import Host, Group
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
		
		if options.has_key('shorewall'):
			if options['shorewall'].has_key('groups'):
			
				groups = {}
			
				for group in Group.objects.filter(enabled=True):
					groups[str(group.name)] = { 'policy': str(group.get_policy_display()), 'ips': list(set([ host.ip for host in group.hosts.all() ])) }

				output = open(options['shorewall']['groups']['config'], 'w')
				yaml.dump(groups, output, default_flow_style=False)
				output.close()
