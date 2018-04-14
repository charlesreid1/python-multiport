from twisted.internet import reactor
from twisted.web import resource, server


"""
Python Multiport Examples:
Dead Simple

This is a dead simple multiport example.
It shows how to create multiple twisted
Resource objects, and serve up each on a 
different port.
"""


class Resource8k(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return "<html><h2>Hello, 8k world!<h2></html>".encode('utf-8')

site8k = server.Site(Resource8k())

class Resource9k(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return "<html><h2>Hello, 9k world!<h2></html>".encode('utf-8')

site9k = server.Site(Resource9k())

reactor.listenTCP(8000, site8k)
reactor.listenTCP(9000, site9k)
reactor.run()

