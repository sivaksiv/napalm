import json
from napalm.base import get_network_driver
driver=get_network_driver('nxos')
dev = driver(hostname='10.197.174.68', username='admin',password="cisco!123")
dev.open()
bgp_neighbors = dev.cli(['show version'])
dev.close()
print(json.dumps(bgp_neighbors, sort_keys=True, indent=4))
