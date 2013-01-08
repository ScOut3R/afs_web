from django.shortcuts import redirect
from django.conf import settings
import yaml
from network.models import Host, Group
from afs.config import parse_config, Config
from afs.main import generate
from afs.errors import Error
from django.contrib import messages


class Object(object):
	
	def __init__(self, object):
		pass


def apply(request):
	#do generate
	configfile = open(settings.AFS_CONFIG, 'r')
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

	args = Object(object)
	args.config = settings.AFS_CONFIG
	args.noreload = False
	parse = parse_config(args)
	config = Config(parse['options'], parse['network'], parse['doreload'])
	try:
		config.validate()
		generate(config, False)
		messages.success(request, "Success")
	except Error as e:
		messages.error(request, e.msg)
	
	
	return redirect("/admin/network")
