"""

Problem:

You need to access various services via HTTP as a client. 
For example, downloading data or interacting with a REST-based API.

Beazley, D. and B. K. Jones (2013). Python Cookbook, 3rd Edition, O'Reilly Media, Inc
"""

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()