# openapi-flask

This repository shows how to use the connexion libraries to
create a simple application from a swagger/openapi swagger file.
The code will read the swagger file and generate the bindings from
the routes described in the swagger file to the actual
implementation. This is not a comprehensive demo, but will be
enough to quickly get started.

There is 2 swagger files:

- `demo.yaml` is the first demo and is based on the swaggerhub
inventory demo.
- `demo2.yaml` adds one extra route which shows a problem in
the default RestyResolver. The included ApiResolver will work
correctly with this file.

The bindings are made using two different methods. The first
method will use the routes to create the name of the functions
for example the route `GET /inventory` will be implemented in
module `api` (from the resolver), filename `inventory` (from
the route) and function `search` (from the resolver and this
can be changed). The route `GET /inventory/{inventoryId}` will
be in the file inventory as the `get` function, and will take
`inventoryId` as an argument. The route `POST /inventory` will
be in the same file, but the function will `post`, same pattern
applies to all other HTTP methods. All query parameters are
passed in as arguments to the functions.

Another way that the routes can be bound to functions is to
use the `operationId` in the swagger file. The value for
`operationId` will point to the function. For this to work
the module name needs to be included in the `operationId`. In
the demo.yaml file the route is `POST /inventory` uses the
`operationId` to specify the implementation called `addItem`
in the inventory file.

This demo does use any authentication. You can find more
information about this and other features of the connexion
library at https://connexion.readthedocs.io.

The included Dockerfile can be used to create a docker image.
To create the docker image use  `docker build -t 
openapi-flask .` and to run it the server  you can use:
`docker run -ti -rm  -p 5000:5000 openapi-flask` Once started
you can connect to http://localhost:5000/ui/ to see the swagger 
documentation and try the endpoints from the documentation.
