import web, yql

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')



class Index:
	def GET(self):
		
		return render.helloform()
		
	def POST(self):	
		form = web.input(name="Nobody", greet="Hello")
		
		greeting = "%s, %s" % (form.greet, form.name + '12s')
		return render.index(greeting = greeting)
		
if __name__ == '__main__':
	app.run()
	
	
	
	# y = yql.Public()

	# query = """select dockStation from xml where url='http://api.bike-stats.co.uk/service/rest/bikestats?format=xml';"""

	# result = y.execute(query)
	
	# stations = []

	# for row in result.rows:	
		# stations.push( '%s has %d slots' % \
		# ( row.get('dockStation').get('name'), int(row.get('dockStation').get('emptySlots')) ) )
	