#!/usr/bin/python
from helper import *
from config import *

display_header()

ticket = ''


def handle_claims_gathering_response():
    global ticket
    if is_ticket_in_url():
        arguments = cgi.FieldStorage()
        ticket = arguments['ticket'].value

        # Here is my PCT token!
        # Client attempts to get RPT at UMA /token endpoint, this time presenting the PCT
        # display_action_name("Client attempts to get RPT at UMA /token endpoint, this time presenting the PCT")

host = is_claim_in_url()
handle_claims_gathering_response()

# Client calls API without RPT token
if not is_ticket_in_url():
    (as_uri, ticket) = get_as_and_ticket(host=host)

# Get Permission access token
# (remove. this is RS->AS, performed by RS internally in call above: get_as_and_ticket)
# access_token = get_permission_access_token_fpx(as_uri)

# Client calls AS UMA /token endpoint with permission ticket and client credentials
need_info, token, redirect_url, ticket_two = get_rpt_fpx(as_uri, ticket)

# Client calls API Gateway with RPT token
if not need_info:
    call_gg_rpt(host=host, rpt=token)

# No RPT for you!  Go directly to Claims Gathering!
# AS returns needs_info with claims gathering URI, which the user should
# put in his browser. Link shorter would be nice if the user has to type it in.
if need_info:
    display_redirect_link_fpx(redirect_url, ticket_two)

display_footer()
