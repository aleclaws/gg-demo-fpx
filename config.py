import cgi

gg_admin_url = "http://gluu.local.org:8001" # unused

# RS CONFIG
gg_proxy_url = "https://rs-moh.fpe.dev.identos.ca" # RS URL
api_path = "api/immunization" # RS Resource Path
# Kong route register with below host
# Our host is the same as the gg_proxy_url because our RS isn't a gateway
host_with_claims = "rs-moh.fpe.dev.identos.ca" # gluu value: "gathering.example.com"
host_without_claims = "rs-moh.fpe.dev.identos.ca" # gluu value: "non-gathering.example.com"
# used to demonstrate PAT request (not part of client responsibility)
rs_client_id = "moh-client-id"
rs_client_secret = "moh-client-secret"

# AS CONFIG
oxd_host = "https://idnserver.fpe.dev.identos.ca" # AS URL 
as_uri=oxd_host #default as_uri, should pull from www-authenticate header
pat_endpoint="transaction/token" # gluu value: get-client-token
rpt_endpoint="transaction/token" # gluu value: uma-rp-get-rpt

# CLIENT CONFIG
ce_url = "https://gluu.local.org" # gluu specific, required for client auth
ce_token_path="token" # unused
client_oxd_id = "91b14554-17ac-4cf4-917d-f1b27e95902a" # gluu token endpoint
client_id="canimmunize-client-id"
client_secret="canimmunize-client-secret"
# You need to add this URL in your consumer client in CE
claims_redirect_url = "http://localhost:8000/cgi-bin/index.py"
# gluu value: claims_redirect_url = "https://gluu.local.org/cgi-bin/index.py"


def is_ticket_in_url():
    arguments = cgi.FieldStorage()
    return 'ticket' in arguments


def is_claim_in_url():
    arguments = cgi.FieldStorage()
    if 'claim' in arguments or 'ticket' in arguments:
        return host_with_claims
    else:
        return host_without_claims

