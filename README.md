# puppetdb-dashapi

This is a wsgi script returning very simple statistics from PuppetDB and meant
to drive a Javascript dashboard.

It returns only the number of nodes for each run status and doesn't handle any
user input, so it can be exposed without much restrictions.

