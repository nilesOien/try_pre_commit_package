#!/bin/bash

# This starts the uvicorn server, which in turn
# runs the code in the_fast_api.py. The syntax is :
# uvicorn path:appName
#
# So that
# uvicorn the_fast_api:theApp
# means look in the_fast_api.py and start the application theApp in there
#
# Run the server under UV management.
uv run uvicorn the_fast_api:theApp --host localhost --port 8004 --workers 1

exit 0

