# puppetdb-dashapi

[![Docker Pulls](https://img.shields.io/docker/pulls/camptocamp/puppetdb-dashapi.svg)](https://hub.docker.com/r/camptocamp/puppetdb-dashapi/)
[![Build Status](https://img.shields.io/travis/camptocamp/puppetdb-dashapi/master.svg)](https://travis-ci.org/camptocamp/puppetdb-dashapi)
[![By Camptocamp](https://img.shields.io/badge/by-camptocamp-fb7047.svg)](http://www.camptocamp.com)

This is a wsgi script returning very simple statistics from PuppetDB and meant
to drive a Javascript dashboard.

It returns only the number of nodes for each run status and doesn't handle any
user input, so it can be exposed without much restrictions.

