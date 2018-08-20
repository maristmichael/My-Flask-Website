#!/usr/bin/env python3
from app import mywebsite

port = int(5000)
mywebsite.run(host='0.0.0.0', port=port, debug=True)
