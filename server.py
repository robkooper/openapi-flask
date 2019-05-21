#!/usr/bin/env python

import logging

import connexion
from resolver import ApiResolver
from connexion import RestyResolver


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)

    # create the flask application
    app = connexion.FlaskApp(__name__, debug=True)

    # create the bindings, if you use demo2.yaml you will need to use ApiResolver
    app.add_api('demo.yaml',
                arguments={'title': 'Demo Server'},
                resolver=RestyResolver('api'),
                resolver_error=501)

    # start the application, in debug mode this will auto reload.
    app.run(port=5000, host=None, server='flask', debug=True)
