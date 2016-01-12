#!/bin/env/python

import pypuppetdb
import json
import os

import settings

def application(environ, start_response):

  db = pypuppetdb.connect(host=settings.PUPPETDB_HOST,
                          port=settings.PUPPETDB_PORT,
                          ssl_key=settings.PUPPETDB_KEY,
                          ssl_cert=settings.PUPPETDB_CERT,
                          ssl_verify=settings.PUPPETDB_SSL_VERIFY)

  if 'DASHAPI_OVERVIEW_FILTER' in os.environ:
    filter_query = os.environ['DASHAPI_OVERVIEW_FILTER']
  else:
    filter_query = None

  statuses = {'failed':0, 'changed':0, 'unchanged':0, 'unreported':0}
  for node in db.nodes(with_status=True, query=filter_query):
    statuses[node.status] += 1

  headers = [('Content-type', 'text/plain'),
             ('Access-Control-Allow-Origin', '*')]
  start_response('200 OK', headers)

  return [json.dumps(statuses).encode('utf8')]

