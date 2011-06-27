#! /usr/bin/env python
import yql


y = yql.Public()

query = """select dockStation from xml where url='http://api.bike-stats.co.uk/service/rest/bikestats?format=xml';"""

result = y.execute(query)

for row in result.rows:	
	print '%s has %d slots' % \
	( row.get('dockStation').get('name'), int(row.get('dockStation').get('emptySlots')) )
