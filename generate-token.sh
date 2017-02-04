#!/usr/bin/env bash

CLIENTID=VFFGwK433iQchxB0j0reXCPf4q44bwfV7rxqrmV1
USERNAME=user1
USERPASS=password1
OAUTHPROVIDER="https://localhost:5000/oauth/token"

curl -k -s -X POST \
-d "client_id=${CLIENTID}&grant_type=password&username=${USERNAME}&password=${USERPASS}" \
${OAUTHPROVIDER} \
| jq .

# {"access_token": "NYODXSR8KalTPnWUib47t5E8Pi8mo4", "token_type": "Bearer", "refresh_token": "s6L6OPL2bnKSRSbgQM3g0wbFkJB4ML", "scope": ""}
