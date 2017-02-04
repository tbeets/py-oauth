#!/usr/bin/env bash

ACCESSTOKEN=SX7vr5P2hkExvjR3ppRVv5nLjlndkn
RESOURCESITE=https://localhost:5000/endpoint

curl -k -H "Authorization: Bearer ${ACCESSTOKEN}" ${RESOURCESITE}
