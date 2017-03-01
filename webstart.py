"""
URL routing & initialization for webapp
"""

from os.path import join
from main import app
from flask import send_from_directory, Blueprint, send_file
import os

print "Starting webapp!"

# splash
from splash.views import splash
app.register_blueprint(splash)

# modules manage their own static files. This serves them all up.
@app.route("/<blueprint_name>/static/<path:fn>")
def _return_static(blueprint_name, fn='index.html'):
    path = join(*app.blueprints[blueprint_name].import_name.split('.')[:-1]) 
    return send_file('%s/static/%s' % (path, fn)) 

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))