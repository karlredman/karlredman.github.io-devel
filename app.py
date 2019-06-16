#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from app import app
from flask_frozen import Freezer


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        app.config.setdefault('FREEZER_DESTINATION', '../docs')
        freezer = Freezer(app)
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)
