# Handling routes
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src'))
import queries
import SimpleHTTPServer
import json

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler # module not instance


class BrainHandler(Handler):
	# overriding POST method? because js router is handling GET requests...
	def do_POST(self):
		if self.path == '/testme':
			# get database query?
			c = queries.dbStats()
			res = {'data':c}
			self.wfile.write(json.dumps(res))
		elif self.path == '/hippovol': 
			c = queries.hipVols()
			res = {'data':c}
			self.wfile.write(json.dumps(res))
