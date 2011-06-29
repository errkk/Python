#! /usr/bin/env python
import yql
from operator import itemgetter, attrgetter

y = yql.Public()

class Boris():
        def getDestination(self,place):
                query = "select dockStation from xml where url='http://api.bike-stats.co.uk/service/rest/bikestats?format=xml' and dockStation.name like '%s' limit 5;" % ( '%' + place + '%' )

                try:
                        result = y.execute(query)

                        if 0 == int(result.count):
                                raise Exception("No results")
                        elif None == result.count:
                                raise Exception("No results")

                        d = []
                        
                        for row in result.rows:

                                name = row.get('dockStation').get('name')
                                ID = int(row.get('dockStation').get('ID'))
                                slots = int(row.get('dockStation').get('emptySlots'))

                                d.append ( ( name,slots ) )
                            

                        sortedStations = sorted(d, key=itemgetter(1), reverse=True)

                        for station in sortedStations:
                                 print '> %s has %d parking slots' % \
                                 ( station[0], station[1] )
                        


                    
                        
                except Exception, e:
                        print e

                        
        def getStart(self,place):
                query = "select dockStation from xml where url='http://api.bike-stats.co.uk/service/rest/bikestats?format=xml' and dockStation.name like '%s' limit 5;" % ( '%' + place + '%' )

                try:
                        result = y.execute(query)

                        if 0 == int(result.count):
                                raise Exception("No results")
                        elif None == result.count:
                                raise Exception("No results")

                        d = []
        
                        for row in result.rows:

                                name = row.get('dockStation').get('name')
                                ID = int(row.get('dockStation').get('ID'))
                                bikes = int(row.get('dockStation').get('bikesAvailable'))

                                d.append ( ( name,bikes ) )
                            

                        sortedStations = sorted(d, key=itemgetter(1), reverse=True)

                        for station in sortedStations:
                                 print '> %s has %d bikes' % \
                                 ( station[0], station[1] )
                                 

                except Exception, e:
                        print e
                        

location = raw_input('Where are you?')
destination = raw_input('Where are you going?')

print 'Sooo, you\'re going to %s from %s are ya?' % ( destination, location )

Boris = Boris()
print 'So near %s there are bikes at:' % location
Boris.getStart( location )
print 'and to park at %destination, how about:'
Boris.getDestination( destination )
