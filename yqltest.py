#! /usr/bin/env python
import yql
from operator import itemgetter, attrgetter

y = yql.Public()

class Boris():
        def bget(self,field,place,limit=5):
                query = "select dockStation from xml where url='http://api.bike-stats.co.uk/service/rest/bikestats?format=xml' and dockStation.name like '%s' limit 5;" % ( '%' + place + '%' )

                try:
                        result = y.execute(query)

                        if int(result.count) == 0:
                                raise Exception("No results")
                        
                        
                        d = []

                        
                        for row in result.rows:

                                name = row.get('dockStation').get('name')
                                ID = int(row.get('dockStation').get('ID'))
                                slots = int(row.get('dockStation').get('emptySlots'))
                                bikes = int(row.get('dockStation').get('bikesAvailable'))

                                if 'slots' == field:
                                        d.append ( ( name,slots ) )
                                else:
                                        d.append ( ( name,bikes ) )

                        try:
                                sortedStations = sorted(d, key=itemgetter(1), reverse=True)
                                return sortedStations
                        except:
                                raise Exception('Can\'t sort stations')
                                
                        
                except Exception, e:
                        print e


        def getDestination(self,place):
                try:
                        sortedStations = self.bget('slots',place)

                        for station in sortedStations:
                                 print '> %s has %d parking slots' % \
                                 ( station[0], station[1] )
                except Exception,e:
                        print e
                        print 'Can\'t find any stations for that name'
                    

                        
        def getStart(self,place):
                try:
                        sortedStations = self.bget('bikes',place)

                        for station in sortedStations:
                                 print '> %s has %d bikes available' % \
                                 ( station[0], station[1] )
                except:
                        print 'Can\'t find any stations for that name'                
                        

location = raw_input('Where are you?')
destination = raw_input('Where are you going?')

print 'Sooo, you\'re going to %s from %s are ya?' % ( destination, location )

Boris = Boris()
print 'So near %s there are bikes at:' % location
Boris.getStart( location )
print 'and to park at %s, how about:' % destination
Boris.getDestination( destination )
