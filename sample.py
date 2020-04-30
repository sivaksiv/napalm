import json
from napalm.base import get_network_driver
driver=get_network_driver('nxos')
dev = driver(hostname='10.197.174.68', username='admin',password="cisco!123")
dev.open()
bgp_neighbors = dev.cli(['show clock'])
print(dev.get_facts())
dev.close()
print(json.dumps(bgp_neighbors, sort_keys=True, indent=4))

#####	ADD CONFIG  #####
with driver(hostname='10.197.174.68', username='admin',password="cisco!123") as device:
  device.load_merge_candidate(filename='add_acl.cfg')
  print(device.compare_config())
  device.commit_config()
