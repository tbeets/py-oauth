
# SENTINEL_ROUTE_PREFIX
# Default prefix for OAuth endpoints. Defaults to /oauth. Prepends both token and management urls.

# SENTINEL_TOKEN_URL
# Url for token creation endpoint. Set to False to disable this feature. Defaults to /token, so the complete url is /oauth/token.

# SENTINEL_MANAGEMENT_URL
# Url for management endpoint. Set to False to disable this feature. Defaults to /management, so the complete url is /oauth/management.

# SENTINEL_REDIS_URL
# Url for the redis server. Defaults to redis://localhost:6379/0.

# SENTINEL_MONGO_DBNAME
# Mongo database name. Defaults to oauth.

SENTINEL_MANAGEMENT_USERNAME='jdoe'
# Username needed to access the management page.

SENTINEL_MANAGEMENT_PASSWORD='notasecret'
# Password needed to access the management page.

# OAUTH2_PROVIDER_ERROR_URI
# The error page when there is an error, default value is /oauth/errors.

# OAUTH2_PROVIDER_TOKEN_EXPIRES_IN
# Default Bearer token expires time, default is 3600.

# OAUTH2_PROVIDER_ERROR_ENDPOINT
# You can also configure the error page uri with an endpoint name.

"""
Other standard PyMongo settings such as MONGO_HOST, MONGO_PORT, MONGO_URI are also supported;
just prefix them with SENTINEL_ as seen above.
"""
