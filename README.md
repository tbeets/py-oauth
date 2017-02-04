# py-oauth

Some investigation of OAuth2 with [Flask-Sentinel](https://pypi.python.org/pypi/Flask-Sentinel) framework.



## Pre-Requisites

CLI
```bash
brew install curl
brew install jq
```

MongoDB
```bash
docker pull mongo
docker run --name some-mongo -p 27017:27017  -d mongo

# access by shell
docker run -it --link some-mongo:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'
```

Redis
```bash
docker pull redis
docker run --name some-redis -p 6379:6379 -d redis

# access by shell
docker run -it --link some-redis:redis --rm redis redis-cli -h redis -p 6379
```

## Execution

```bash
# Assume Python 2.7 environment
pip install -r /path/to/requirements.txt
python mysite.py
```

## Manage

* Edit `settings.py` for admin user/pass
* Default management site:
https://localhost:5000/oauth/management
* Create users and clients

## Test

```bash
# Manuel edit as required
# TODO: Automate
generate-token.sh
get-protected-resource.sh
```
