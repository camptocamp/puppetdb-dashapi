FROM grahamdumpleton/mod-wsgi-docker:python-3.3-onbuild

CMD [ "--mount-point", "/dashapi", "dashapi.py" ]
