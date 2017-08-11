import os
import sys

from lunch import create_app
app = create_app()

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 5000

# heroku support
if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
app.run(host="0.0.0.0", threaded=True, port=port)