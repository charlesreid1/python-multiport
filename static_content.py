import os

"""
Python Multiport Examples:
Static Content

This is a multiport example that uses twisted
to serve up different static content 
on different ports.

See https://twistedmatrix.com/documents/current/web/howto/web-in-60/static-content.html

Bonus example! For those times when you don’t actually want to write a new program, the above implemented functionality is one of the things the command line twistd tool can do. In this case, the command

twistd -n web --path /tmp
"""

# Site, an IProtocolFactory which glues a listening server port (IListeningPort) to the HTTPChannel implementation:
from twisted.web.server import Site
# File, an IResource which glues the HTTP protocol implementation to the filesystem:
from twisted.web.static import File
# The reactor, which drives the whole process, actually accepting TCP connections and moving bytes into and out of them:
from twisted.internet import reactor
# And the endpoints module, which gives us tools for, amongst other things, creating listening sockets:
from twisted.internet import endpoints

# ------------------
# Site 1: 8000

# We create an instance of the File resource pointed at the directory to serve:
resource = File(os.path.join(os.getcwd(),'site1'))

# Then we create an instance of the Site factory with that resource:
factory = Site(resource)

# Now we glue that factory to a TCP port:
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000)
endpoint.listen(factory)

# -----------------
# Site 2: 9000
resource = File(os.path.join(os.getcwd(),'site2'))
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 9000)
endpoint.listen(factory)

# -----------------
# Site 3: 9001
resource = File(os.path.join(os.getcwd(),'site3'))
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 9001)
endpoint.listen(factory)


reactor.run()




