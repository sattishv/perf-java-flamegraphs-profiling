cpu_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'stack': {
        'type': 'string',
        'minlength': 1,
	'required': True,
    },
    'value': {
        'type': 'integer',
        'min': 1,
        'required': True,
    },
    'timestamp': {
	'type': 'integer',
	'min': 1490778413,
	'required': True,

    },
    'hostname': {
        'type': 'string',
	'minlength' : 1,
        #'required': True,
    },
}

cpu = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'cpu_sample',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': cpu_schema
}

experiments_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'experiment_id': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'start_time': {
        'type': 'integer',
        'min': 1,
    },
    'end_time': {
        'type': 'integer',
        'min': 1,
    },
}

tests_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'experiment_id': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'required': True,
    },
    'start_time': {
        'type': 'integer',
        'min': 1,
        'required': True,
    },
    'end_time': {
        'type': 'integer',
        'min': 1,
        'required': True,
    },
    'test_name': {
         'type': 'string',
          'minlength': 1,
         'required': True,
    },
    'test_id': {
         'type': 'string',
          'minlength': 1,
         'required': True,
     },
}

experiments = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'experiment',

    'additional_lookup': {
        'url': 'regex("[\w_0-9]+")',
        'field': 'experiment_id'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': experiments_schema
}

tests = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'test',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],


    'schema': tests_schema
}



DOMAIN = {'cpu': cpu, 'experiments': experiments, 'tests': tests}

# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = "192.168.56.111"
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'profiling'
# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


X_DOMAINS = ['*']
